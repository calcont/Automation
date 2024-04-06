from selenium.webdriver.common.by import By


class PostfixCalculatorLocators:
    POSTFIX_INPUT = (By.ID, 'Postfix')
    SPACE_SEPARATION_CHECKBOX = (By.ID, 'postfix-switch')
    ANS = (By.ID, 'Ans')
    CALCULATE_BUTTON = (By.CLASS_NAME, 'cal')


class PrefixCalculatorLocators:
    PREFIX_INPUT = (By.ID, 'Prefix')
    SPACE_SEPARATION_CHECKBOX = (By.ID, 'prefix-switch')
    ANS = (By.ID, 'Ans')
    CALCULATE_BUTTON = (By.CLASS_NAME, 'cal')
