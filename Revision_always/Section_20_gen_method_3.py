from selenium import webdriver
from selenium.webdriver.common.by import By
from Section_20_gen_method_2 import ExplicitWaitType
import time

class ExplicitWaitDemo2():

    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        wait = ExplicitWaitType(driver)
        driver.get(baseUrl)
        driver.find_element(By.CSS_SELECTOR, "#tab-flight-tab-hp > span.icons-container").click()
        driver.find_element(By.CSS_SELECTOR, "#flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.CSS_SELECTOR, "#flight-destination-hp-flight").send_keys("NYC")

        driver.find_element(By.CSS_SELECTOR, '#flight-departing-hp-flight').click()
        cal_month1=driver.find_element(By.XPATH, '//div[@id="flight-departing-wrapper-hp-flight"]/div/div/div[2]')
        all_dates1=cal_month1.find_elements(By.TAG_NAME, 'button')

        time.sleep(12)

        for date in all_dates1:
            if "26" in date.text:
                date.click()
                break


        return_date=driver.find_element(By.CSS_SELECTOR, '#flight-returning-hp-flight')
        return_date.click()
        return_date.clear()
        time.sleep(4)
        cal_month1 = driver.find_element(By.XPATH, '//*[@id="flight-returning-wrapper-hp-flight"]/div/div/div[2]')
        all_dates1 = cal_month1.find_elements(By.TAG_NAME, 'button')

        time.sleep(10)

        for date in all_dates1:
            if "30" in date.text:
                date.click()
                break

        search=driver.find_element(By.CSS_SELECTOR, '#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button')
        search.click()
        time.sleep(12)
        element = wait.waitForElement("stopFilter_stops-0")
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()
