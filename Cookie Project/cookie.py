from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = time.time()+5
five_min = time.time()+ 60*5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options = chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR,value="#cookie")


while time.time()<five_min:
    cookie.click()

    if time.time() > timeout:
        money = int(driver.find_element(By.CSS_SELECTOR,"#money").text.replace(",",""))
        str_val = ""
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for item in store:
            item = item.text.split()
            if int(item[2].replace(",","")) <= money:
                str_val = item[0]
            else:
                break
        driver.find_element(By.CSS_SELECTOR,f"#buy{str_val}").click()
        timeout = time.time() + 5

print("Cookies per second:", driver.find_element(By.ID, "cps").text)
driver.quit()