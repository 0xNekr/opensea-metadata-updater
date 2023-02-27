from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

collection_link = 'https://opensea.io/assets/ethereum/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/'
collection_supply = 10


def main():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36")

    browser = webdriver.Chrome(executable_path="chromedriver", options=options)
    update_metadata(browser)


def update_metadata(browser):

    for i in range(collection_supply):
        to_update = collection_link + str(i)
        browser.get(to_update)
        browser.implicitly_wait(10)
        try:
            more = browser.find_element(By.XPATH, "//button[@aria-label='More']")
            more.click()
            browser.implicitly_wait(10)
            refresh = browser.find_element(By.XPATH, "//button[contains(., 'Refresh metadata')]")
            refresh.click()
        except NoSuchElementException:
            pass


main()