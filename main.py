import pytest
import argparse
from conf import readYaml, selectProfileEndpoint


def readArgs():
    parser = argparse.ArgumentParser(description="Run Selenium tests with environment-specific configurations")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--local", action="store_true", help="Run tests on the local environment")
    group.add_argument("--production", action="store_true", help="Run tests on the production environment")
    group.add_argument("--stage", action="store_true", help="Run tests on the stage environment")

    parser.add_argument("--filename", type=str, help="Run test on a specific file")
    args = parser.parse_args()
    if sum([args.local, args.production, args.stage]) <= 1:
        pass
    else:
        parser.error("Exactly one of --local, --production, or --stage must be specified")
    return args


def selectProfile(args):
    if args.local:
        return "local"
    elif args.production:
        return "production"
    elif args.stage:
        return "stage"
    else:
        return "local"


def init():
    args = readArgs()
    profile = selectProfile(args)
    readYaml()
    selectProfileEndpoint(profile)
    if args.filename:
        pytest.main(["tests/", "-s", "-k", args.filename])
    else:
        pytest.main(["tests/"])


if __name__ == "__main__":
    init()
