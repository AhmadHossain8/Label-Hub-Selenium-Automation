import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.keys import Keys
options = webdriver.EdgeOptions()
options.add_argument('--log-level=OFF')
def clear_input_field(input_element):
    input_element.send_keys(Keys.CONTROL + 'a')
    input_element.send_keys(Keys.DELETE)

class annotator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://182.163.99.86/login")
        cls.wait = WebDriverWait(cls.driver, 30)

    def test_login(self):
        username = "a1@gmail.com"
        password = "Abc@123"

        username_input = self.wait.until(EC.presence_of_element_located((By.ID, 'username')))
        password_input = self.wait.until(EC.presence_of_element_located((By.ID, 'password'))) 
        button = self.driver.find_element(By.XPATH, "//button[text()='Sign in']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        button.click()

        self.wait.until(EC.url_to_be("http://182.163.99.86/dashboard"))
        #self.assertEqual(self.driver.current_url, "http://182.163.99.86/dashboard", "Login Failed")
        time.sleep(1)

        self.driver.find_element(By.XPATH, "/html/body/div/section/main/aside/div/div/div/div[2]/a/div/span[2]").click()
        time.sleep(3)
        self.wait.until(EC.url_to_be("http://182.163.99.86/projects"))
        time.sleep(3)
        group = self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/section/main/div[2]/div[2]/section/div/div[1]/div/input')))
        group.send_keys("SZ1001")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section/div/div[2]/div/table/tbody/tr[1]/td[9]/div/a").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section/section[4]/div/div/div[2]/div/table/tbody/tr/td[9]/div/a").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section[2]/div/div/span[1]").click()
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div/span[1]")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, "/html/body/div/section/main/div[2]/div[2]/section[3]/div/div/div/span[2]")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div[2]/div[2]/section[3]/div/div/footer/button[1]").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/button[1]").click()
        time.sleep(3)
    def test_logout(self):
        # Assuming user is already logged in
        
        button1 = self.wait.until(EC.presence_of_element_located((By.ID, "radix-:r5:")))
        button1.click()
        logout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-radix-collection-item] > img[alt='logout']")))
        logout_button.click()

        self.wait.until(EC.url_to_be("http://182.163.99.86/login"))
        self.assertEqual(self.driver.current_url, "http://182.163.99.86/login", "Logout Failed")
        
        

      
    def test_logout(self):
        # Assuming user is already logged in
        
        button1 = self.wait.until(EC.presence_of_element_located((By.ID, "radix-:r5:")))
        button1.click()
        logout_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-radix-collection-item] > img[alt='logout']")))
        logout_button.click()

        self.wait.until(EC.url_to_be("http://182.163.99.86/login"))
        self.assertEqual(self.driver.current_url, "http://182.163.99.86/login", "Logout Failed") 
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
