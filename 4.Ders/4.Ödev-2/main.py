from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from locators import *


class Test_Sauce:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.url ="https://www.saucedemo.com/"


    def test_goto_page(self):
        self.driver.maximize_window()
        self.driver.get(url=self.url)

    def test_username_and_password_empty_message(self):
        self.test_goto_page()
        self.clear_username_text()
        self.clear_password_text()
        self.login_buttton_click()
        current_message = "Epic sadface: Username is required"
        print(self.view_error_message(current_message))


    def test_password_empty_message(self):
        self.test_goto_page()
        self.clear_username_text()
        self.clear_password_text()
        self.input_locked_username()
        self.login_buttton_click()
        current_message = "Epic sadface: Password is required"
        print(self.view_error_message(current_message))

    
    def test_locked_out_message(self):
        self.test_goto_page()
        self.clear_username_text()
        self.clear_password_text()
        self.input_locked_username()
        self.input_password()
        self.login_buttton_click()
        current_message = "Epic sadface: Sorry, this user has been locked out."
        print(self.view_error_message(current_message))
        

    def test_close_icon(self):
        self.test_goto_page()
        self.clear_username_text()
        self.clear_password_text()
        self.login_buttton_click()
        errorBtn = self.driver.find_element(By.XPATH,MESSAGE_CLOSED)
        errorBtn.click()
        print("Successfully closed")   


    def test_success_login(self):
        self.test_goto_page()
        self.clear_username_text()
        self.input_unlocked_username()
        self.clear_password_text()
        self.input_password()
        self.login_buttton_click()
        if "inventory.html" in self.driver.current_url:
            print("Successfully")

        
        
    def test_count_of_product(self):
        self.test_goto_page()
        self.clear_username_text()
        self.input_unlocked_username()
        self.clear_password_text()
        self.input_password()
        self.login_buttton_click()
        inventoryItems = self.driver.find_elements(By.CLASS_NAME,INVENTORY_ITEM)
        numberOfInventory = len(inventoryItems)
        if numberOfInventory == 6:
            print(f"Success! Number of invertory: {numberOfInventory}")
        
        
    def view_error_message(self,message):
        errorMessage = self.driver.find_element(By.XPATH,ERROR_MESSAGE)
        testResult = errorMessage.text == f"{message}"
        return f"Test Sonucu : {testResult}"

    def login_buttton_click(self):
        login_btn = self.driver.find_element(By.ID,LOGINN_BUTTON)
        login_btn.click()
        sleep(2)

    def input_locked_username(self):
        input_userName = self.driver.find_element(By.ID,INPUT_USERNAME)
        input_userName.send_keys(LOCKED_USERNAME)
    
    def input_unlocked_username(self):
        input_userName = self.driver.find_element(By.ID,INPUT_USERNAME)
        input_userName.send_keys(UNLOCKED_USERNAME)
    
    def input_password(self):
        input_password = self.driver.find_element(By.ID,INPUT_PASSWORD)
        input_password.send_keys(PASSWORD)

    def clear_username_text(self):
        input_userName = self.driver.find_element(By.ID,INPUT_USERNAME)
        input_userName.clear()
        sleep(1)
    
    def clear_password_text(self):
        input_password = self.driver.find_element(By.ID,INPUT_PASSWORD)
        input_password.clear()
        sleep(1)

    def test_case_run(self):
        self.test_username_and_password_empty_message()
        self.test_password_empty_message()
        self.test_locked_out_message()
        self.test_close_icon()
        self.test_success_login()
        self.test_count_of_product()


test_sauce = Test_Sauce()
test_sauce.test_case_run()