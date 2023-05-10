import openpyxl as xl
import selenium.common.exceptions
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import StaleElementReferenceException
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.carrefour.fr/r/surgeles/pizzas-quiches-tartes/pizzas")

page = driver.find_elements(by=By.CLASS_NAME, value="product-grid-item")

prices = []
for i in page:
    data = i.text
    splitting_data = data.split("\n€")
    price = splitting_data[0] + "€"
    if price.__contains__("NOUVEAUTÉ"):
        price = price.split("\n")[1] + "€"
    splitting_data = data.split("\n")
    for i in splitting_data:
        if i.lower().__contains__("pizza"):
            names = i
            break
    for i in splitting_data:
        if i.lower().startswith("la "):
            bottle_size = i
            break
    for i in splitting_data:
        if i.lower().__contains__(" € "):
            quantity = i
            break

    print(f'{names:60} : {price:5} : {bottle_size:20} : {quantity:20}')

driver.get("https://www.carrefour.fr/r/surgeles/pizzas-quiches-tartes/pizzas?noRedirect=1&page=2")

page = driver.find_elements(by=By.CLASS_NAME, value="product-grid-item")

prices = []
for i in page:
    data = i.text
    splitting_data = data.split("\n€")
    price = splitting_data[0] + "€"
    if price.__contains__("NOUVEAUTÉ"):
        price = price.split("\n")[1] + "€"
    splitting_data = data.split("\n")
    for i in splitting_data:
        if i.lower().__contains__("pizza"):
            names = i
            break
    for i in splitting_data:
        if i.lower().startswith("la "):
            bottle_size = i
            break
    for i in splitting_data:
        if i.lower().__contains__(" € "):
            quantity = i
            break

    print(f'{names:60} : {price:5} : {bottle_size:20} : {quantity:20}')

driver.get("https://www.carrefour.fr/r/surgeles/pizzas-quiches-tartes/pizzas?noRedirect=1&page=3")

page = driver.find_elements(by=By.CLASS_NAME, value="product-grid-item")

prices = []
for i in page:
    data = i.text
    splitting_data = data.split("\n€")
    price = splitting_data[0] + "€"
    if price.__contains__("NOUVEAUTÉ"):
        price = price.split("\n")[1] + "€"
    splitting_data = data.split("\n")
    for i in splitting_data:
        if i.lower().__contains__("pizza"):
            names = i
            break
    for i in splitting_data:
        if i.lower().startswith("la "):
            bottle_size = i
            break
    for i in splitting_data:
        if i.lower().__contains__(" € "):
            quantity = i
            break

    print(f'{names:60} : {price:5} : {bottle_size:20} : {quantity:20}')




