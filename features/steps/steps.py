from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# PATH to chromedriver
PATH = r"c:\Program Files (x86)\chromedriver.exe"

@given(u'Open main page')
def open_main_page(context):
    context.driver = webdriver.Chrome(PATH)
    context.driver.maximize_window()
    context.driver.get("https://turbotlumaczenia.pl/")

@when(u'Click Wycena page')
def click_wycena_page(context):
    context.driver.find_element(By.LINK_TEXT, "Wycena").click()

@when(u'Click tłumaczenia pisemne')
def click_wycena_page(context):
    context.driver.find_element(By.LINK_TEXT, "Tłumaczenie pisemne").click()

@when(u'Choose translation from Polish into German')
def choose_translation(context):
    if not context.driver.find_element(By.ID, "dropdown-col-from1").text == 'z POLSKI':
        context.driver.find_element(By.ID, "dropdown-col-from1").click()
        context.driver.find_element(By.XPATH, '//li[@data-cc="pl"]').click()

    context.driver.find_element(By.ID, "dropdown-col-to1").click()
    el = context.driver.find_elements(By.XPATH, '//input')
    for x in el:    # clear all selected checkboxes
        if x.is_selected():
            x.click()
    context.driver.find_element(By.XPATH, '//input[@data-cc="de"]').click()

@when(u'Choose proofreading option')
def choose_proofreading(context):
    if not context.driver.find_element(By.ID, "proofreading").is_selected():
        context.driver.find_element(By.ID, "proofreading").click()


@when(u'Enter a text between 250 and 400 sings into textarea')
def enter_text(context):
    textarea = context.driver.find_element(By.NAME, "content")
    textarea.clear()
    textarea.send_keys("""Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.
Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim.
Donec pede justo, fringilla vel, aliquet nec, vulputate.
""")


@when(u'Email fields should be ampty')
def check_emailfield(context):
    context.driver.find_element(By.ID, "email").clear()


@then(u'Check if expected price is calculated')
def estimated_price(context):
    sleep(3)
    text = context.driver.find_element(By.XPATH, '//span[@data-bind-expected-realisation-time]').text
    print(text)
    assert text == '3 godziny'


@then(u'Check if expected time is calculated')
def estimated_time(context):
    price = context.driver.find_element(By.XPATH, '//span[@data-bind-expected-price]').text
    print(price)
    assert price == '20.14 zł'
    context.driver.close()
