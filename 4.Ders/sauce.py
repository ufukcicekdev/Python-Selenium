from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class TestSauce:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")


    def test_invlaid_login(self):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))   #maksimum 5 sn. çift parantez var
        usernameeinput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))   #maksimum 5 sn. çift parantez var
        passwordinput = self.driver.find_element(By.ID,"password")
        usernameeinput.send_keys("xxuseer")
        passwordinput.send_keys("xxpassword")
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        erormessages = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        textResult = erormessages.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu: {textResult}")


    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))   #maksimum 5 sn. çift parantez var
        usernameeinput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))   #maksimum 5 sn. çift parantez var
        passwordinput = self.driver.find_element(By.ID,"password")
        #Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameeinput,"standard_user")
        actions.send_keys_to_element(passwordinput,"secret_sauce")
        actions.perform()
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(20)






testClass = TestSauce()
testClass.test_invlaid_login()
testClass.test_valid_login()

