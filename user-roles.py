from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Fatoorah test configuration
loginUrl = "https://new-new.fatoorah.sa/login"
targetUrl = "https://new-new.fatoorah.sa/add-user-roles"
fatoorahPhone = "0555008564"
fatoorahPassword = "321998"

# Roles list
roleName = ["Kashier", "sales invoice", "purchase invoice", "store keeper", "admin"]

roleKey = roleName[0]


def login(driver, phone, password):
    driver.get(loginUrl)
    time.sleep(5)
    driver.find_element(
        By.XPATH, "//input[@placeholder='...أدخل رقم الجوال']"
    ).send_keys(phone)
    driver.find_element(By.ID, "password-input").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(8)


def addRole(driver, role):
    driver.get(targetUrl)
    time.sleep(8)  # wait for the page to load
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys(role)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#pos").click()
    time.sleep(5)
    saveBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dropdownMenuButton"))
    )
    saveBtn.click()
    time.sleep(8)


def main():
    driver = webdriver.Chrome()
    roleNumber = roleName[0]

    try:
        login(driver, fatoorahPhone, fatoorahPassword)
        addRole(driver, roleNumber)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
