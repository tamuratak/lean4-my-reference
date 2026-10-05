#!/usr/bin/env python3
"""Check complete Lean examples embedded in the Japanese reference."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BLOCK = re.compile(r'^```lean\s*\n(.*?)^```\s*$', re.MULTILINE | re.DOTALL)


def changed_paths():
    """Select existing docs Markdown files changed from HEAD, including untracked files."""
    commands = [
        ['git', 'diff', '--name-only', '-z', 'HEAD', '--', 'docs/'],
        ['git', 'ls-files', '--others', '--exclude-standard', '-z', '--', 'docs/'],
    ]
    paths = set()
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, check=True, timeout=30)
        for name in result.stdout.split(b'\0'):
            if name:
                path = ROOT / os.fsdecode(name)
                if path.suffix == '.md' and path.is_file():
                    paths.add(path)
    return sorted(paths)


def check(path, library_command):
    try:
        text = path.read_text()
    except OSError as error:
        return 0, [f'{path}: cannot read: {error}']
    blocks = list(BLOCK.finditer(text))
    errors = []
    for number, match in enumerate(blocks, 1):
        code = match.group(1)
        imports = re.findall(r'^import .+$', code, re.MULTILINE)
        code = re.sub(r'^import .+\n', '', code, flags=re.MULTILINE)
        if re.search(r'\b(sorry|admit)\b', code):
            errors.append(f'{path.relative_to(ROOT)}: example {number}: unfinished proof')
            continue
        # Preserve the common import for existing tactic pages only.
        common_import = 'import Std.Tactic\n' if path.parent == ROOT / 'docs/tactics' else ''
        source = common_import + '\n'.join(imports) + '\n' + code
        external = any(re.match(r'import (Mathlib|Aesop)(\.|\s|$)', line) for line in imports)
        command, working_directory = library_command if external else (['lean'], ROOT)
        with tempfile.TemporaryDirectory(prefix='lean-reference-') as directory:
            source_path = Path(directory) / 'Example.lean'
            source_path.write_text(source)
            try:
                result = subprocess.run(
                    command + [str(source_path)], cwd=working_directory, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=90,
                )
            except (subprocess.TimeoutExpired, OSError) as error:
                errors.append(f'{path.relative_to(ROOT)}: example {number}: {error}')
                continue
            if result.returncode or re.search(r"declaration uses [`']sorry[`']", result.stdout):
                line = text[:match.start()].count('\n') + 1
                errors.append(f'{path.relative_to(ROOT)}:{line}: example {number}\n{result.stdout}')
    return len(blocks), errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='*', type=Path)
    parser.add_argument('--changed', action='store_true',
                        help='Check docs Markdown files changed from HEAD, including staged and untracked files')
    parser.add_argument('--library-project', type=Path, default=ROOT,
                        help='Lake project providing Mathlib and Aesop (default: this repository)')
    parser.add_argument('--allow-library-toolchain-mismatch', action='store_true',
                        help='Explicitly allow an additional compatibility check with another Lean version')
    args = parser.parse_args()
    if args.changed and args.paths:
        parser.error('--changed cannot be combined with explicit paths')
    if args.changed:
        try:
            paths = changed_paths()
        except subprocess.CalledProcessError as error:
            parser.error(f'Cannot select changed files: {os.fsdecode(error.stderr).strip()}')
        except (subprocess.TimeoutExpired, OSError) as error:
            parser.error(f'Cannot select changed files: {error}')
        print(f'Selected {len(paths)} changed Markdown files under docs/ (relative to HEAD, including untracked):')
        for path in paths:
            print(f'  {str(path.relative_to(ROOT))!r}')
        if not paths:
            print('No changed Markdown files to check.')
            return False
    else:
        paths = [path.resolve() for path in args.paths] if args.paths else sorted((ROOT / 'docs').rglob('*.md'))
    library_project = args.library_project.resolve()
    library_command = (['lake', 'env', 'lean'], library_project)
    try:
        external = any(re.search(r'^import (Mathlib|Aesop)(\.|\s|$)', path.read_text(), re.MULTILINE)
                       for path in paths)
    except OSError as error:
        print(f'Cannot read Markdown file: {error}')
        return True
    if external:
        try:
            standard_version = subprocess.check_output(['lean', '--version'], cwd=ROOT, text=True)
            library_version = subprocess.check_output(
                ['lake', 'env', 'lean', '--version'], cwd=library_project, text=True,
                stderr=subprocess.STDOUT, timeout=90)
        except (subprocess.SubprocessError, OSError) as error:
            print(f'Cannot initialize library project: {error}')
            if isinstance(error, subprocess.CalledProcessError):
                print(error.output)
            return True
        # Lake may print configuration warnings before Lean's version line.
        library_version_line = next((line for line in library_version.splitlines()
                                     if line.startswith('Lean (version ')), None)
        if library_version_line is None:
            print(f'Cannot determine library Lean version:\n{library_version}')
            return True
        print(f'Library examples: {library_version_line}')
        if library_version_line != standard_version.strip():
            print('Library toolchain differs from the repository toolchain.')
            if not args.allow_library_toolchain_mismatch:
                return True
            print('Compatibility check only; the pinned toolchain remains unverified for library examples.')
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(lambda path: check(path, library_command), paths))
    errors = [error for _, failures in results for error in failures]
    for error in errors:
        print(error)
    print(f'Checked {sum(count for count, _ in results)} examples in {len(paths)} files; {len(errors)} failures.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
