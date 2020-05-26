from selenium.webdriver.common.by import By
import time
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        loginLink = self.driver.find_element(By.LINK_TEXT, "Login")
        loginLink.click()
        time.sleep(6)
        emailField = self.driver.find_element(By.ID, "user_email")
        emailField.send_keys(username)
        time.sleep(6)
        passwordField = self.driver.find_element(By.ID, "user_password")
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.NAME, "commit")
        loginButton.click()
