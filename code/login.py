import pickle
import time
from selenium import webdriver
"""
driver = webdriver.Chrome('C:\\Users\\maeli\\chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

"""
browser = webdriver.Chrome('C:\\Users\\maeli\\chromedriver.exe')


def get_cookies():
    browser.get("https://login.aliexpress.com/buyer.htm?return=https%3A%2F%2Fwww.aliexpress.com%2F&random=CEA73DF4D81D4775227F78080B9B6126")
    print('input your username and password in Firefox and hit Submit')
    input('Hit Enter here if you have summited the form: <Enter>')
    cookies = browser.get_cookies()
    print(cookies)
    pickle.dump(cookies, open("cookies.pickle", "wb"))


def set_cookies():
    browser.get("https://aliexpress.com")
    cookies = pickle.load(open("cookies.pickle", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get("https://bestselling.aliexpress.com/en")


if __name__ == '__main__':
    get_cookies()
