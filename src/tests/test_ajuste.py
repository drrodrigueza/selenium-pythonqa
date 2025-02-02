# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAjuste():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_ajuste(self):
    self.driver.get("https://qa-tiendas-frontend.titan.com.pa/seguridad/login")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.ID, "usuario").click()
    self.driver.find_element(By.ID, "usuario").send_keys("6334")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("titan123")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(7) .subtitle").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted:nth-child(4) .card-menu").click()
    self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-arrow-wrapper").click()
    time.sleep(10)
    self.driver.find_element(By.ID, "a59d45e023e2-0").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-sm-7 > input").send_keys("C:\\fakepath\\ajuste_inventario (7).csv")
    time.sleep(10)
    self.driver.find_element(By.CSS_SELECTOR, ".btn-safe").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-safe")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".mt-3 > h4").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mt-3 > h4").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".mt-3 > h4")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "codigo_confirmacion").click()
    self.driver.find_element(By.ID, "codigo_confirmacion").send_keys("5312")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success:nth-child(1)").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".btn-success:nth-child(1)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Auditoría").click()
  
