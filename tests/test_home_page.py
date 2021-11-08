import pytest

from pageObject.home_page import HomePage
from test_data.home_page_data import HomePageData
from utilities.base_class import BaseClass


class TestHomePage(BaseClass):

    def test_from_sub(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        log.info("first name is " + get_data["first_name"])
        home_page.get_name().send_keys(get_data["first_name"])
        home_page.get_email().send_keys(get_data["email"])
        home_page.get_check().click()
        self.select_option_by_text(home_page.get_gender(), get_data["gender"])

        home_page.get_submit_form().click()

        alert_text = home_page.get_success_message().text

        assert "success" in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("testcase2"))
    def get_data(self, request):
        return request.param
