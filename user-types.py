from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fatoorah test configuration
login_url = "login URL"
taget_url = "Taregt URL"
fatoorah_phone = "********"
fatoorah_password = "********"

userTypes = ["جمله", "قطاعي", "موزع", "مستورد", "مصنع"]

# 0 for جمله, 1 for قطاعي, 2 for موزع, 3 for مستورد
userNumber = 3


def login(driver, phone, password):
    driver.get(loginUrl)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='...أدخل رقم الجوال']")
        )
    ).send_keys(phone)
    driver.find_element(By.ID, "password-input").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.url_changes(loginUrl))


def addUserType(driver, userType):
    driver.get(targetUrl)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#name"))
    ).send_keys(userType)
    driver.find_element(By.CSS_SELECTOR, "#dropdownMenuButton").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#dropdownMenuButton"))
    )


def main():
    driver = webdriver.Chrome()
    try:
        login(driver, fatoorahPhone, fatoorahPassword)
        addUserType(driver, userTypes[userNumber])
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
