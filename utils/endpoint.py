from conf import PROFILE_ENDPOINT, getSuiteEndpoint


def generateEndpoint(suite_name, tool_name):
    return PROFILE_ENDPOINT + getSuiteEndpoint(suite_name, tool_name)
