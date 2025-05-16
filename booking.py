from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_booking():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    driver.get("https://booking.kai.id")
    driver.implicitly_wait(10)
    driver.maximize_window()

    departure= driver.find_element(By.ID, "origination-flexdatalist")
    departure.send_keys("Bandung")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "origination-flexdatalist-results"))
    )
    dropdown_items_d = driver.find_elements(By.CSS_SELECTOR, "#origination-flexdatalist-results li.item")
    dropdown_items_d[0].click()

    arrival = driver.find_element(By.ID, "destination-flexdatalist")
    arrival.send_keys("Jakarta")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "destination-flexdatalist-results"))
    )
    dropdown_items_a = driver.find_elements(By.CSS_SELECTOR, "#destination-flexdatalist-results li.item")
    dropdown_items_a[0].click()

    date_departure = driver.find_element(By.XPATH, "//input[@id='departure_dateh']")
    date_departure.click()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ui-datepicker-div")))
        holiday = driver.find_element(By.XPATH, '//td[@class=" holiday"]')
        holiday.click()
    except TimeoutException:
        pass

    button = driver.find_element(By.XPATH, '//input[@id="submit"]')
    button.click()
