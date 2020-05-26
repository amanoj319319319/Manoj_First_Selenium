from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):

        emailField = self.driver.find_element(By.ID, "email")
        emailField.send_keys(username)

        passwordField = self.driver.find_element(By.ID, "pass")
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.XPATH, '//*[@id="u_0_b"]')
        loginButton.click()

