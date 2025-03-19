from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import re


"""
driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/login") 



driver.find_element(By.ID, "email").send_keys("maria.gonzalez@urosario.edu.co")
driver.find_element(By.ID, "password").send_keys("Password123#")
driver.find_element(By.ID, "login").click()

time.sleep(2)


saldo_texto = driver.find_element(By.ID,"saldo_usuario").text 
saldo_inicial = float(saldo_texto.split(":")[-1].strip())


driver.find_element(By.ID, "deposit_button").click()

time.sleep(2)

driver.find_element(By.ID, "balance").send_keys("100")
driver.find_element(By.ID, "deposit").click()

time.sleep(2)

saldo_texto_final = driver.find_element(By.ID, "saldo_usuario").text
saldo_final = float(saldo_texto_final.split(":")[-1].strip())

assert saldo_final == saldo_inicial + 100,f"Error: saldo esperado {saldo_inicial +100}, pero se obtuvo {saldo_texto_final}"

time.sleep(2)
driver.quit()
"""


########################
# Prueba 1 - Test Feliz#
########################

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/login") 

driver.find_element(By.ID, "email").send_keys("maria.gonzalez@urosario.edu.co")
driver.find_element(By.ID, "password").send_keys("Password123#")
driver.find_element(By.ID, "login").click()

time.sleep(2)

saldo_texto = driver.find_element(By.ID,"saldo_usuario").text 
saldo_inicial = float(saldo_texto.split(":")[-1].strip())


driver.find_element(By.ID, "Withdraw_button").click()

time.sleep(2)

driver.find_element(By.ID, "balance").send_keys("10")
driver.find_element(By.ID, "password").send_keys("Password123#")
driver.find_element(By.ID, "withdraw_buttom").click()

time.sleep(2)


##########################
# Prueba 2 - Test InFeliz#
##########################

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5000/login") 

driver.find_element(By.ID, "email").send_keys("maria.gonzalez@urosario.edu.co")
driver.find_element(By.ID, "password").send_keys("-----------------")
driver.find_element(By.ID, "login").click()

time.sleep(20)

error_login = driver.find_element(By.ID, "error_login").text
print(error_login)
