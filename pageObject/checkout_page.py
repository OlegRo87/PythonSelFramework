from selenium.webdriver.common.by import By

from pageObject.confirm_page import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements_by_xpath('//div[@class="card h-100"]')
    card_title = (By.CSS_SELECTOR, '.card-title a')
    card_footer = (By.CSS_SELECTOR, '.card-footer button')
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_titles(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
