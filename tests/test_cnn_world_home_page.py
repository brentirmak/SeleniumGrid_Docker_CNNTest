import pytest

from pages.cnn_world_home_page import CNNWorldHomePage

@pytest.mark.smoke
class TestCNNWorldHomePage:

    def test_go_to_cnn_world_section(self, driver):
        URL = "https://www.cnn.com/world"
        world_home = CNNWorldHomePage(driver)
        world_home.go_to_cnn_world_section(URL)
        assert world_home.title_contains_world_news()

    def test_cnn_world_body_header(self, driver):
        URL = "https://www.cnn.com/world"
        world_home = CNNWorldHomePage(driver)
        world_home.go_to_cnn_world_section(URL)
        element = world_home.body_header_contains_world()
        assert element.is_displayed()

