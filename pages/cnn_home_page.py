class CNNHomePage:

    URL = "https://www.cnn.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def open_http(self):
        self.driver.get("http://www.cnn.com")

    def title_contains_cnn(self):
        return "CNN" in self.driver.title

    def title_not_empty(self):
        return len(self.driver.title) > 0

    def url_contains_cnn(self):
        return "cnn.com" in self.driver.current_url

    def redirected_to_https(self):
        return self.driver.current_url.startswith("https")