from pageObject.home_page import HomePage
from utilities.base_class import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.get_logger()
        home_page = HomePage(self.driver)
        check_out_page = home_page.shop_items()
        log.info("getting all the card titles")
        cards = check_out_page.get_card_titles()

        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            log.info(card.text)
            if card_text == "Blackberry":
                check_out_page.get_card_footer()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        # self.driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li/a").click()
        confirm_page = check_out_page.checkOutItems()
        log.info("Entering country name as Rus")
        self.driver.find_element_by_id('country').send_keys('rus')
        self.verify_link_presence("Russia")

        self.driver.find_element_by_link_text("Russia").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        success_text = self.driver.find_element_by_class_name("alert-success").text
        log.info("Text received from application is " + success_text)

        assert "Success! Thank you!" in success_text

