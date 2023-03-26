from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
class Test_DemoClass:
    #her testden önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        #günün tarihi ile klasör var mı kontrol et yoksa oluştur
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) #klasör yapısı

    #her testden sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    def test_demoFunc(self):
        # 3A Arrange Assert
        text = "hello"
        assert text =="hello"

    
    def test_demo2(self):
        assert False

    #@pytest.mark.skip()  # bu metodu çalıştırmamak için kullanılır
    @pytest.mark.parametrize("username,password",[("1","1"),("ass","ff")]) # ilgili parametler için teker teker kullanır
    def test_invalid_login(self,username,password):
        self.waitForElemtVisibil((By.ID,"user-name"))  #maksimum 5 sn. çift parantez var
        usernameeinput = self.driver.find_element(By.ID,"user-name")
        self.waitForElemtVisibil((By.ID,"password"))  #maksimum 5 sn. çift parantez var
        #maksimum 5 sn. çift parantez var
        passwordinput = self.driver.find_element(By.ID,"password")
        usernameeinput.send_keys(username)
        passwordinput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        erormessages = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_invalida_login-{username}-{password}.png")

        assert  erormessages.text == "Epic sadface: Username and password do not match any user in this service"


    def waitForElemtVisibil(self, locator):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator))