"""Check changed-file selection using temporary Git repositories."""

from contextlib import redirect_stdout, redirect_stderr
import io
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import check_examples


class ChangedPathsTest(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='check-examples-git-')
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.git('init', '-q')
        for name in ['docs/unchanged.md', 'docs/modified.md', 'docs/staged.md',
                     'docs/deleted.md', 'docs/renamed.md', 'docs/changed.txt',
                     'reference.md', '.gitignore']:
            self.write(name, 'original\n')
        self.git('add', '.')
        self.git('-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                 '-c', 'commit.gpgsign=false',
                 'commit', '-qm', 'Initial files')
        self.root_patch = patch.object(check_examples, 'ROOT', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def git(self, *args):
        return subprocess.run(['git', *args], cwd=self.root, check=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def test_changed_files_include_staged_untracked_and_renamed(self):
        self.write('docs/modified.md', 'modified\n')
        self.write('docs/staged.md', 'staged\n')
        self.git('add', 'docs/staged.md')
        self.git('mv', 'docs/renamed.md', 'docs/new name.md')
        (self.root / 'docs/deleted.md').unlink()
        self.write('docs/changed.txt', 'modified non-Markdown\n')
        self.write('reference.md', 'modified outside docs\n')
        self.write('docs/new.md', 'new file\n')
        self.write('docs/name with\na newline.md', 'new file\n')
        self.write('docs/ignored.md', 'ignored file\n')
        self.write('.gitignore', 'docs/ignored.md\n')
        expected = [self.root / name for name in [
            'docs/modified.md', 'docs/staged.md', 'docs/new name.md',
            'docs/new.md', 'docs/name with\na newline.md',
        ]]
        self.assertEqual(check_examples.changed_paths(), sorted(expected))

    def test_no_changes_skip_lean_initialization(self):
        with patch('sys.argv', ['check_examples.py', '--changed']), \
                patch.object(check_examples, 'check') as check, \
                patch.object(check_examples.subprocess, 'check_output') as initialize, \
                redirect_stdout(io.StringIO()):
            self.assertFalse(check_examples.main())
        check.assert_not_called()
        initialize.assert_not_called()

    def test_changed_mode_checks_only_selected_files(self):
        path = self.write('docs/new.md', '```lean\nexample : True := by trivial\n```\n')
        newline_path = self.write('docs/name with\na newline.md', 'text\n')
        with patch('sys.argv', ['check_examples.py', '--changed']), \
                patch.object(check_examples, 'check', return_value=(1, [])) as check, \
                redirect_stdout(io.StringIO()) as output:
            self.assertFalse(check_examples.main())
        self.assertEqual({call.args[0] for call in check.call_args_list}, {path, newline_path})
        self.assertIn("  'docs/new.md'\n", output.getvalue())
        self.assertIn("  'docs/name with\\na newline.md'\n", output.getvalue())

    def test_explicit_paths_cannot_be_combined_with_changed(self):
        with patch('sys.argv', ['check_examples.py', '--changed', 'docs/modified.md']), \
                redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            check_examples.main()
        self.assertEqual(error.exception.code, 2)

    def test_git_failure_is_reported(self):
        with tempfile.TemporaryDirectory(prefix='check-examples-no-git-') as directory, \
                patch.object(check_examples, 'ROOT', Path(directory)), \
                patch('sys.argv', ['check_examples.py', '--changed']), \
                redirect_stderr(io.StringIO()) as output, \
                self.assertRaises(SystemExit) as error:
            check_examples.main()
        self.assertEqual(error.exception.code, 2)
        self.assertIn('Cannot select changed files', output.getvalue())

    def test_check_reports_read_error(self):
        path = self.root / 'docs/missing.md'
        count, errors = check_examples.check(path, (['lake', 'env', 'lean'], self.root))
        self.assertEqual(count, 0)
        self.assertEqual(len(errors), 1)
        self.assertIn(f'{path}: cannot read:', errors[0])

    def test_read_error_before_library_detection_is_reported(self):
        with patch('sys.argv', ['check_examples.py', str(self.root / 'docs/missing.md')]), \
                patch.object(check_examples.subprocess, 'check_output') as initialize, \
                redirect_stdout(io.StringIO()) as output:
            self.assertTrue(check_examples.main())
        self.assertIn('Cannot read Markdown file:', output.getvalue())
        initialize.assert_not_called()


if __name__ == '__main__':
    unittest.main()
