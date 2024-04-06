import yaml
import os

PATH = "./conf.yml"
CONFIG = {}
PROFILE_ENDPOINT = None
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def readYaml():
    with open(PATH, "r") as file:
        config = yaml.safe_load(file)
    print("Read config from yaml")
    return dumpConfig(config)


def getSuiteEndpoint(suite_name, tool_name):
    return CONFIG["suites"][suite_name][tool_name]["endpoint"]


def selectProfileEndpoint(profile):
    global PROFILE_ENDPOINT
    PROFILE_ENDPOINT = CONFIG["profiles"][profile]["endpoint"]
    print("Selected profile endpoint", PROFILE_ENDPOINT)


def dumpConfig(config):
    for key, value in config.items():
        CONFIG[key] = value
    print("Dumped config to CONFIG", CONFIG)
