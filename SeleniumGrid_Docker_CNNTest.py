def test_cnn_loads(driver):
    #if driver.test_meta["browser"] == "firefox":
    #    assert False, "Intentional failure for Firefox"

    driver.get("https://www.cnn.com")
    assert "CNN" in driver.title

def test_cnn_title_not_empty(driver):
    driver.get("https://www.cnn.com")
    assert len(driver.title) > 0

def test_cnn_url(driver):
    driver.get("https://www.cnn.com")
    assert "cnn.com" in driver.current_url

def test_cnn_redirects_to_https(driver):
    driver.get("http://www.cnn.com")
    assert driver.current_url.startswith("https")