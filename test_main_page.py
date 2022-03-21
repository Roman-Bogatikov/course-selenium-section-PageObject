import time


def test_find_button_addbusket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    browser.implicitly_wait(10)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert button, 'Button not found'

    time.sleep(5)