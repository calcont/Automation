from selenium.webdriver.common.by import By


class InfixToPostfixPageLocators:
    INFIX_INPUT = (By.ID, 'Infix')
    POSTFIX_OUTPUT = (By.ID, 'Postfix')
    CONVERT_BUTTON = (By.CLASS_NAME, 'con')


class InfixToPrefixPageLocators:
    INFIX_INPUT = (By.ID, 'Infix')
    PREFIX_OUTPUT = (By.ID, 'prefix')
    CONVERT_BUTTON = (By.CLASS_NAME, 'con')


class PostfixToInfixPageLocators:
    POSTFIX_INPUT = (By.ID, 'Postfix')
    INFIX_OUTPUT = (By.ID, 'Infix')
    CONVERT_BUTTON = (By.CLASS_NAME, 'con')


class PrefixToInfixPageLocators:
    PREFIX_INPUT = (By.ID, 'prefix')
    INFIX_OUTPUT = (By.ID, 'infix')
    CONVERT_BUTTON = (By.CLASS_NAME, 'con')


class PrefixToPostfixPageLocators:
    PREFIX_INPUT = (By.ID, 'prefix')
    POSTFIX_OUTPUT = (By.ID, 'postfix')
    CONVERT_BUTTON = (By.CLASS_NAME, 'con')
