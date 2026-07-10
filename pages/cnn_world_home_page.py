from selenium.webdriver.common.by import By

class CNNWorldHomePage:

    URL = "https://www.cnn.com/world"

    def __init__(self, driver):
        self.driver = driver

    def go_to_cnn_world_section(self, URL):
        self.driver.get(URL)

    def title_contains_world_news(self):
        return "World news" in self.driver.title

    def body_header_contains_world(self):
        element = self.driver.find_element(By.XPATH, "//h1[contains(.,'World')]")
        #return "World" in self.driver.title
        return element
