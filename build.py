import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser("Build script for pypi and pypi test")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--test',
        action='store_true',
        help='Build to test.pypi.org'
    )
    group.add_argument(
        '--re',
        action='store_true',
        help='Build to pypi.org'
    )

    args = parser.parse_args()

    subprocess.call(['python3', 'setup.py', 'sdist', 'bdist_wheel'])
    if args.test:
        subprocess.call(['twine', 'upload', '--config-file', '.pypirc', '--repository', 'testpypi', 'dist/*'])
    elif args.re:
        subprocess.call(['twine', 'upload', '--config-file', '.pypirc', '--repository', 'pypi', 'dist/*'])


if __name__ == '__main__':
    main()
