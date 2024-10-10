from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# fatoorah configration
login_url = "login URL"
taget_url = "Taregt URL"
fatoorah_phone = "********"
fatoorah_password = "********"

# inotialize the driver
driver = webdriver.Chrome()

#  Set the window zoom to 25%
driver.execute_script("document.body.style.zoom='25%'")


# Generate random number for the reference number field 8 digits like = 12345678
def randomStringDigits(stringLength=8):
    import random
    import string

    lettersAndDigits = string.digits
    return "".join(random.choice(lettersAndDigits) for i in range(stringLength))


# Generate random SA number like = 0576806241
def randomSaNumber(stringLength=10):
    import random
    import string

    lettersAndDigits = string.digits
    return "05" + "".join(
        random.choice(lettersAndDigits) for i in range(stringLength - 2)
    )


# List of the customers names sa arabic names
customers = [
    "سعدون جابر",
    "إلهام المدفعي",
    "أصيل هميم",
    "حاتم العراقي",
    "سيف نبيل",
    "نور الزين",
    "محمد السالم",
    "أحلام وهبي",
    "رضا الخياط",
    "ليلى العطار",
    "أحمد المصلاوي",
]

next_customer = customers[0]

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

    # add supplier
    driver.get(taget_url)
    time.sleep(8)  # wait for the page to load

    driver.find_element("css selector", "#name").send_keys(
        next_customer
    )  # add the first supplier name
    time.sleep(1)
    driver.find_element("css selector", "#reference_number").send_keys(
        randomStringDigits()
    )
    time.sleep(1)
    driver.find_element("xpath", "//input[@id='taxNumber']").send_keys(
        randomStringDigits()
    )
    time.sleep(1)
    driver.find_element("xpath", "//input[@id='company_mobile']").send_keys(
        randomSaNumber()
    )
    time.sleep(1)
    driver.find_element("id", "credit_limit").send_keys("15000")
    time.sleep(5)

    # Wait for the dropdown menu button to be clickable
    save_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dropdownMenuButton"))
    )
    save_btn.click()
    time.sleep(6)


finally:
    driver.quit()
    # print("done")
