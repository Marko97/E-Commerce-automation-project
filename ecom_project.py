import random
from selenium.webdriver.support.select import Select
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

os.environ['PATH'] += r"D:\Marko\Selenium tutorials\Selenium Drivers"
driver = webdriver.Chrome()

driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()

#Click on Phones & PDAs button
phones = driver.find_element(
    By.XPATH, '//a[text()="Phones & PDAs"]'
)
phones.click()

#Click on classic phone
classic_phone = driver.find_element(
    By.XPATH, '//a[text()="Palm Treo Pro"]'
)
classic_phone.click()
time.sleep(1)

#Click on phone gallery
first_picture = driver.find_element(
    By.XPATH, '//ul[@class="thumbnails"]//li[1]'
)
first_picture.click()

#next picture
next_click = driver.find_element(
    By.XPATH, '//button[@title="Next (Right arrow key)"]'
)
for i in range(0, 2):
    next_click.click()
    time.sleep(1)

#save screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0, 101)) + '.png')

#close gallery
x_button = driver.find_element(
    By.XPATH, '//button[@title="Close (Esc)"]'
)
x_button.click()
time.sleep(1)

#phone quantity
quantity = driver.find_element(
    By.ID, "input-quantity"
)
quantity.click()
time.sleep(1)
quantity.clear()
time.sleep(1)
quantity.send_keys('2')
time.sleep(1)

add_to_cart_button = driver.find_element(
    By.ID, "button-cart"
)
add_to_cart_button.click()

#add laptop to cart
laptops = driver.find_element(
    By.XPATH, '//a[text()="Laptops & Notebooks"]'
)
action = ActionChains(driver)
action.move_to_element(laptops).perform()
time.sleep(2)
laptops_2 = driver.find_element(
    By.XPATH, '//a[text()="Show AllLaptops & Notebooks"]'
)
time.sleep(1)
laptops_2.click()

#choose HP laptop
HP = driver.find_element(
    By.XPATH, '//a[text()="HP LP3065"]'
)
HP.click()

#scroll
add_to_cart_button_2 = driver.find_element(
    By.XPATH, '//button[@id="button-cart"]'
)
add_to_cart_button_2.location_once_scrolled_into_view 
time.sleep(1)

#choose calendar
calendar = driver.find_element(
    By.XPATH, '//i[@class="fa fa-calendar"]'
)
calendar.click()
time.sleep(1)

#pick a year
next_click_calendar = driver.find_element(
    By.XPATH, '//th[@class="next"]'
)
month_year = driver.find_element(
    By.XPATH, '//th[@class="picker-switch"]'
)
while month_year.text != 'December 2023':
    next_click_calendar.click()
time.sleep(2)

#pick a date
calendar_date = driver.find_element(
    By.XPATH, '//td[text()="31"]'
)
calendar_date.click()
time.sleep(2)

add_to_cart_button_2.click()

#Checkout
go_to_cart=driver.find_element(
    By.ID, 'cart-total'
)
go_to_cart.click()
time.sleep(1)

checkout=driver.find_element(
    By.XPATH, '//p[@class="text-right"]/a[2]'
)
checkout.click()
time.sleep(1)



#click on guest button
guest=driver.find_element(
    By.XPATH, '//input[@value="guest"]'
)
guest.click()

#continue button
continue_1 = driver.find_element(
    By.ID, "button-account"
)
continue_1.click()
time.sleep(1)

#scroll
step_2 = driver.find_element(
    By.XPATH, '//a[text()="Step 2: Billing Details "]'
)
step_2.location_once_scrolled_into_view
time.sleep(1)

#first name
first_name = driver.find_element(
    By.ID, "input-payment-firstname"
)
first_name.click()
first_name.send_keys('test-name')
time.sleep(1)

#last name
last_name = driver.find_element(
    By.ID, "input-payment-lastname"
)
last_name.click()
last_name.send_keys('test-lastname')
time.sleep(1)

#e-mail
email = driver.find_element(
    By.ID, "input-payment-email"
)
email.click()
email.send_keys('test@test.com')
time.sleep(1)

#telephone
telephone = driver.find_element(
    By.ID, "input-payment-telephone"
)
telephone.click()
telephone.send_keys('123456789')
time.sleep(1)

#address
address = driver.find_element(
    By.ID, "input-payment-address-1"
)
address.click()
address.send_keys('test-address-1')
time.sleep(1)

#city
city = driver.find_element(
    By.ID, "input-payment-city"
)
city.click()
city.send_keys('test-city')
time.sleep(1)

#post code
post_code = driver.find_element(
    By.ID, "input-payment-postcode"
)
post_code.click()
post_code.send_keys('12345')
time.sleep(1)

#country
country = driver.find_element(
    By.ID, "input-payment-country"
)
dropdown_1 = Select(country)
time.sleep(1)
dropdown_1.select_by_visible_text('Croatia')
time.sleep(1)

#Region
region = driver.find_element(
    By.ID, "input-payment-zone"
)
dropdown_2 = Select(region)
time.sleep(1)
dropdown_2.select_by_visible_text('Brodsko-posavska')
time.sleep(1)

continue_2 = driver.find_element(
    By.XPATH, '//input[@id="button-guest"]'
)
continue_2.click()
time.sleep(1)

continue_3 = driver.find_element(
    By.ID, "button-shipping-method"
)
continue_3.click()
time.sleep(1)

#accept terms 
terms = driver.find_element(
    By.XPATH, '//input[@name="agree"]'
)
terms.click()
time.sleep(1)

#continue to confirmation
continue_4 = driver.find_element(
    By.XPATH, '//input[@id="button-payment-method"]'
)
continue_4.click()
time.sleep(2)

#final price
final_price = driver.find_element(
    By.XPATH, '//table[@class="table table-bordered table-hover"]/tfoot/tr[3]/td[2]'
)
print("The final price of both products is" + final_price.text)
time.sleep(1)


#confirm order
confirmation_button = driver.find_element(
    By.ID, "button-confirm"
)
confirmation_button.click()

#success test
success_text = driver.find_element(
    By.XPATH, '//div[@class="col-sm-12"]/h1'
)
print(success_text.text)
time.sleep(1)


driver.close()


