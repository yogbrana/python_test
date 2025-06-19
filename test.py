from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://youtube.com")

actual = driver.title
expected = "YouTube"

if expected in actual:
    print("Title matched")
else:
    print("Title unmatched")

driver.close()
