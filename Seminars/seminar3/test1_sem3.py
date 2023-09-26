import yaml
from testpage import OperationsHelper
import logging

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test_login_negative FAILED"


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pswd"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAILED"



def test_add_post(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["pswd"])
    # testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata["title"])
    testpage.add_description(testdata["description"])
    testpage.add_content(testdata["content"])
    testpage.click_save_post_button()
    testpage.find_new_post_title()
    assert testpage.find_new_post_title() == f"{testdata['title']}", "test add post FAILED"
