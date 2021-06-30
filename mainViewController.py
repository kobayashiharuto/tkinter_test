import chromedriver_binary
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def send_message(mail, password, id, message, callback):
    # WebDriver のオプションを設定する
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get('https://facebook.com')

    sleep(1)

    mail_form = driver.find_element_by_css_selector('#email')
    mail_form.send_keys(mail)
    pass_form = driver.find_element_by_css_selector('#pass')
    pass_form.send_keys(password)
    form = driver.find_element_by_css_selector('form')
    form.submit()

    sleep(3)

    driver.get('https://www.facebook.com/messages/t/' + id)

    sleep(5)

    actions = ActionChains(driver)
    actions.send_keys(message + Keys.ENTER)
    actions.perform()

    sleep(1)

    driver.quit()
    callback()
