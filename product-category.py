from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# fatoorah test configration
login_url = "https://new-new.fatoorah.sa/login"
taget_url = "https://new-new.fatoorah.sa/add-product-category"
fatoorah_phone = "0555008564"
fatoorah_password = "321998"

user_types = [
    "اجهزه كهربائيه",
    "ملابس",
    "احذيه",
    "اكسسوارات",
    "العاب",
    "ادوات منزليه",
    "اثاث",
]


# Start the driver
driver = webdriver.Chrome()

try:

    driver.get(login_url)
    time.sleep(5)

    # login
    driver.find_element(
        "xpath", "//input[@placeholder='...أدخل رقم الجوال']"
    ).send_keys(fatoorah_phone)
    driver.find_element("id", "password-input").send_keys(fatoorah_password)
    driver.find_element("css selector", "button[type='submit']").click()
    time.sleep(8)

    # add a new user type
    driver.get(taget_url)
    time.sleep(8)  # wait for the page to load

    driver.find_element("css selector", "#name").send_keys(
        user_types[5]
    )  # add the first supplier name
    time.sleep(1)

    # submit the form
    driver.find_element("css selector", "#dropdownMenuButton").click()
    time.sleep(3)


finally:
    driver.quit()
