#!/usr/bin/env python3
"""Check complete Lean examples embedded in the Japanese reference."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BLOCK = re.compile(r'^```lean\s*\n(.*?)^```\s*$', re.MULTILINE | re.DOTALL)


def check(path):
    blocks = list(BLOCK.finditer(path.read_text()))
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
        with tempfile.TemporaryDirectory(prefix='lean-reference-') as directory:
            source_path = Path(directory) / 'Example.lean'
            source_path.write_text(source)
            try:
                result = subprocess.run(
                    ['lean', str(source_path)], cwd=ROOT, text=True,
                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=90,
                )
            except (subprocess.TimeoutExpired, OSError) as error:
                errors.append(f'{path.relative_to(ROOT)}: example {number}: {error}')
                continue
            if result.returncode or re.search(r"declaration uses [`']sorry[`']", result.stdout):
                line = path.read_text()[:match.start()].count('\n') + 1
                errors.append(f'{path.relative_to(ROOT)}:{line}: example {number}\n{result.stdout}')
    return len(blocks), errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='*', type=Path)
    args = parser.parse_args()
    paths = [path.resolve() for path in args.paths] if args.paths else sorted((ROOT / 'docs').rglob('*.md'))
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(check, paths))
    errors = [error for _, failures in results for error in failures]
    for error in errors:
        print(error)
    print(f'Checked {sum(count for count, _ in results)} examples in {len(paths)} files; {len(errors)} failures.')
    return bool(errors)


if __name__ == '__main__':
    raise SystemExit(main())
