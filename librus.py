import sys
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


driverPath = r'C:\webdrivers\chromedriver.exe'

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(
        executable_path=driverPath, chrome_options=options)
except NoSuchElementException:
    print('Error 01: unable to initiate webdriver')


def log_into(username, password):
    try:
        driver.get('https://portal.librus.pl/rodzina')

        try:
            driver.find_element_by_id('dropdownTopRightMenuButton').click()
            driver.find_elements_by_link_text('Zaloguj')[1].click()
        except NoSuchElementException:
            driver.find_elements_by_link_text('LIBRUS Synergia')[0].click()
            driver.find_elements_by_link_text('Zaloguj')[0].click()

        sleep(1)
        iframe = driver.find_element_by_xpath('//iframe[@id="caLoginIframe"]')
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath(
            '//input[@name="login"]').send_keys(username)
        driver.find_element_by_xpath(
            '//input[@name="password"]').send_keys(password)
        sleep(0.3)
        driver.find_element_by_id('LoginBtn').click()

    except NoSuchElementException:
        print('Error 02: unable to log in')
        driver.quit()
        sys.exit()


def messages():
    driver.get('https://synergia.librus.pl/wiadomosci')
    sleep(10)
    try:
        table = driver.find_element_by_xpath(
            '//td[@style="font-weight: bold;"]//a')
        table.click()
        sleep(2)
        print('You have a new message')
        messages()
    except NoSuchElementException:
        print('No new messages')


def librus_auto(username, password, comments=True):
    if comments:
        print('Logging in')
    log_into(username, password)
    sleep(2)
    if comments:
        print('Loading messages')
    sleep(1)
    while True:
        url = driver.current_url
        if url == 'https://portal.librus.pl/rodzina':
            librus_auto(username, password, comments)
        messages()
        sleep(600)

    driver.quit()
