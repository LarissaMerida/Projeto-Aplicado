from pathlib import Path
import os
import sys


def main():
    in_virtual_environment = bool(os.getenv("VIRTUAL_ENV")) or (
        sys.prefix != sys.base_prefix
    )
    in_container = Path("/.dockerenv").exists()

    if in_virtual_environment or in_container:
        environment = "container" if in_container else "virtual environment"
        print(f"Environment check passed: {environment}")
        return 0

    print(
        "Pre-commit must run inside a virtual environment/Poetry environment "
        "or a container. Use 'poetry run pre-commit run --all-files'.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
