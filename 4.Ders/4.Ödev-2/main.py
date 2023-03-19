from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from locators import *

driver = webdriver.Chrome(ChromeDriverManager().install())
class Test_Sauce:
    def test_goto_page(self):
        driver.maximize_window()
        driver.get(url="https://www.saucedemo.com/")
        print("Successfully Navigated To The Page!!")

    def test_username_and_password_empty_message(self):
        self.login_buttton_click()
        current_message = "Epic sadface: Username is required"
        print(self.view_error_message(current_message))

    def test_password_empty_message(self):
        self.input_locked_username()
        self.login_buttton_click()
        current_message = "Epic sadface: Password is required"
        print(self.view_error_message(current_message))
    
    def test_locked_out_message(self):
        self.input_locked_username()
        self.input_password()
        self.login_buttton_click()
        current_message = "Epic sadface: Sorry, this user has been locked out."
        print(self.view_error_message(current_message))

    def test_close_icon(self):
        self.login_buttton_click()
        errorBtn = driver.find_element(By.XPATH,MESSAGE_CLOSED)
        errorBtn.click()
        print("Successfully closed")   

    def test_success_login(self):
        self.input_unlocked_username()
        self.input_password()
        self.login_buttton_click()
        if "inventory.html" in driver.current_url:
            print("Successfully")
        
    def test_count_of_product(self):
        self.input_unlocked_username()
        self.input_password()
        self.login_buttton_click()
        inventoryItems = driver.find_elements(By.CLASS_NAME,INVENTORY_ITEM)
        numberOfInventory = len(inventoryItems)
        if numberOfInventory ==6:
            print(f"Success! Number of invertory: {numberOfInventory}")


    def view_error_message(self,message):
        errorMessage = driver.find_element(By.XPATH,ERROR_MESSAGE)
        testResult = errorMessage.text == f"{message}"
        return f"Test Sonucu : {testResult}"

    def login_buttton_click(self):
        login_btn = driver.find_element(By.ID,LOGINN_BUTTON)
        login_btn.click()
        sleep(1)

    def input_locked_username(self):
        input_userName = driver.find_element(By.ID,INPUT_USERNAME)
        input_userName.send_keys(LOCKED_USERNAME)
    
    def input_unlocked_username(self):
        input_userName = driver.find_element(By.ID,INPUT_USERNAME)
        input_userName.send_keys(UNLOCKED_USERNAME)
    
    def input_password(self):
        input_password = driver.find_element(By.ID,INPUT_PASSWORD)
        input_password.send_keys(PASSWORD)




test_sauce = Test_Sauce()
test_sauce.test_goto_page()
#test_sauce.test_username_and_password_empty_message()
#test_sauce.test_password_empty_message()
#test_sauce.test_locked_out_message()
#test_sauce.test_close_icon()
#test_sauce.test_success_login()
test_sauce.test_count_of_product()

