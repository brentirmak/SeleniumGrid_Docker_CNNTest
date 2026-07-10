import pytest

from pages.cnn_home_page import CNNHomePage

@pytest.mark.smoke
class TestCNNHomePage:

    def test_cnn_loads(self, driver):
        home = CNNHomePage(driver)
        home.open()
        assert home.title_contains_cnn()

    def test_cnn_title_not_empty(self, driver):
        home = CNNHomePage(driver)
        home.open()
        assert home.title_not_empty()

    def test_cnn_url(self, driver):
        home = CNNHomePage(driver)
        home.open()
        assert home.url_contains_cnn()

    def test_cnn_redirects_to_https(self, driver):
        home = CNNHomePage(driver)
        home.open_http()
        assert home.redirected_to_https()




