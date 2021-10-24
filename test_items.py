from selenium import webdriver
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_basket(browser):
    browser.get(link)
    button = browser.find_elements_by_id('add_to_basket_form')
    time.sleep(15)
    assert button, 'No such button-basket here'
