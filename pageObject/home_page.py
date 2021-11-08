from selenium.webdriver.common.by import By
from pageObject.checkout_page import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')
    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    check = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.XPATH, '//input[@value="Submit"]')
    success_message = (By.CSS_SELECTOR, '[class*="alert-success"]')

    def shop_items(self):
        # driver.find_element_by_css_selector('a[href*="shop"]')
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_check(self):
        return self.driver.find_element(*HomePage.check)

    def get_submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)
