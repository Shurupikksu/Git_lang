from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

def test_guest_should_see_basket(browser):
    browser.get(link)
    browser.find_element_by_id('add_to_basket_form')