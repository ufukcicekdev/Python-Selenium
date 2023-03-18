from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class TestSauce:
    def test_invlaid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        usernameeinput = driver.find_element(By.ID,"user-name")
        passwordinput = driver.find_element(By.ID,"password")
        usernameeinput.send_keys("xxuseer")
        passwordinput.send_keys("xxpassword")
        sleep(1)
        loginBtn = driver.find_element(By.ID,"login-button")
        loginBtn.click()
        erormessages = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        textResult = erormessages.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {textResult}")
        sleep(100)



testClass = TestSauce()
testClass.test_invlaid_login()

