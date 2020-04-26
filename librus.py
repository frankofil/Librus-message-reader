from selenium import webdriver
from time import sleep
import os


try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    # options.add_argument("--incognito")
    # options.add_argument("--kiosk")
    # option.add_argument('window-size=1600,900')
    # options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path = r'C:\webdrivers\chromedriver.exe', chrome_options=options)
except:
    print('Error 01: unable to initiate webdriver')


def log_into(username, password):
    try:
        driver.get("https://portal.librus.pl/rodzina")

        try:
            driver.find_element_by_id('dropdownTopRightMenuButton').click()
            driver.find_elements_by_link_text("Zaloguj")[1].click()
            print("test1")
        except:
            driver.find_elements_by_link_text("LIBRUS Synergia")[0].click()
            driver.find_elements_by_link_text('Zaloguj')[0].click()
            print("test2")

        sleep(2)
        iframe = driver.find_element_by_xpath("//iframe[@id='caLoginIframe']")
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath(
            "//input[@name='login']").send_keys(username)
        driver.find_element_by_xpath(
            "//input[@name='password']").send_keys(password)
        sleep(0.3)
        driver.find_element_by_id('LoginBtn').click()
    except:
        print("Error 02: unable to log in")
        exit()


def messages():
    driver.get("https://synergia.librus.pl/wiadomosci")
    sleep(10)
    try:
        table = driver.find_element_by_xpath(
            '//td[@style="font-weight: bold;"]//a')
        table.click()
        sleep(2)
        print("You have a new message")
        messages()  
    except:
        print("No new messages")
        return True


def librus_auto(username, password, comments=True):
    if comments:
        print("Logging in")
    log_into(username, password)
    sleep(2)
    # driver.get('https://synergia.librus.pl/eksporty/ical/eksportuj/planUcznia')
    if comments:
        print("Loading messages")
    sleep(1)
    while True:
        url = driver.current_url
        if url == "https://portal.librus.pl/rodzina":
            librus_auto(username, password, comments)
        messages()
        sleep(600)
        
    driver.quit()

