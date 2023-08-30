from selenium.webdriver.common.by import By



class TextBoxPageLocators:


    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    MALE = (By.CSS_SELECTOR, "[value='Male']")
    FEMALE = (By.CSS_SELECTOR, "[value='Female']")
    OTHER = (By.CSS_SELECTOR, "[value='Other']")
