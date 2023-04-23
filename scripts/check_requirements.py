import re
import sys

import pkg_resources


def check_requirements(requirements_file):
    """
    Check if the packages listed in a requirements file are installed.

    :param requirements_file: path to the requirements file
    :type requirements_file: str
    """
    with open(requirements_file, "r") as f:
        requirements = list(pkg_resources.parse_requirements(f.read()))

    installed_packages = {package.key.lower() for package in pkg_resources.working_set}

    missing_packages = [
        requirement.name for requirement in requirements
        if requirement.name.lower() not in installed_packages
    ]

    if missing_packages:
        print("Missing packages:")
        print(", ".join(missing_packages))
        sys.exit(1)
    else:
        print("All packages are installed.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python check_requirements.py <requirements_file>")
        sys.exit(1)

    requirements_file = sys.argv[1]
    check_requirements(requirements_file)


if __name__ == "__main__":
    main()

