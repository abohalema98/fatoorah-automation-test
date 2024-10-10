from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Fatoorah test configuration
login_url = "login URL"
taget_url = "Taregt URL"
fatoorah_phone = "********"
fatoorah_password = "********"

# List of the suppliers names
suppliers = [
    "سامر احمد",
    "محمد علي",
    "علي احمد",
    "عبدالله محمد",
]


def randomStringDigits(length=8):
    """Generate a random string of digits."""
    return "".join(random.choice(string.digits) for _ in range(length))


def login(driver, phone, password):
    """Log in to the Fatoorah site."""
    driver.get(loginUrl)
    time.sleep(5)
    driver.find_element(
        By.XPATH, "//input[@placeholder='...أدخل رقم الجوال']"
    ).send_keys(phone)
    driver.find_element(By.ID, "password-input").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(8)


def addSupplier(driver, supplierName):
    """Add a supplier to the Fatoorah site."""
    driver.get(targetUrl)
    time.sleep(8)  # wait for the page to load

    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(supplierName)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#reference_number").send_keys(
        randomStringDigits()
    )
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='taxNumber']").send_keys(
        randomStringDigits()
    )
    time.sleep(1)
    driver.find_element(By.ID, "credit_limit").send_keys("5000")
    time.sleep(5)

    # Wait for the dropdown menu button to be clickable
    saveBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dropdownMenuButton"))
    )
    saveBtn.click()
    time.sleep(8)

    print("Successfully added supplier")


def main():
    driver = webdriver.Chrome()
    subNumber = 2

    try:
        login(driver, fatoorahPhone, fatoorahPassword)
        addSupplier(driver, suppliers[subNumber])
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
