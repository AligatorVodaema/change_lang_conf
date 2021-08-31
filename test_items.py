import time

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_button_for_add_item_exists(browser):
    """Сheck for existence add-button for shop cart."""
    browser.get(LINK)
    browser.implicitly_wait(5)
    browser.find_element_by_xpath("//form[@id='add_to_basket_form']/button[@type='submit']")
    time.sleep(5)
