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

from dateutil.parser import parse
import os
import csv
from csv import writer
import math
import PyPDF2
from PyPDF2 import PdfReader
import tabula


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

website_to_work = input("Enter URL: ")

desktop = os.path.expanduser("~\\Desktop\\Upwork\\")
PATH = "C:\Program Files (x86)\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option('prefs', {
    "download.default_directory": desktop,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(options=chrome_options)


# website_to_work = "https://knowthefactsmmj.com/2023/01/05/2023-ommu-updates/"
driver.get(website_to_work)

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
list_pdfs = {}

files_to_work_on = driver.find_elements(by=By.TAG_NAME, value="li")
for i, values in enumerate(files_to_work_on):
    if is_date(values.text):
        count = 0
        while count < 3:
            count += 1
            try:
                pdf_files = values
                pdf_files.click()
                date_element = values.find_element(By.TAG_NAME, "a")
                link = date_element.get_attribute("href").split("/")[-1]
                print(values.text)
                time.sleep(1)
                list_pdfs.update({values.text: link})
                count = 0
                break
            except selenium.common.exceptions.ElementClickInterceptedException:
                time.sleep(1)


for i in list_pdfs:
    try:
        os.rename(desktop + list_pdfs[i], desktop + i + ".pdf")
    except FileNotFoundError:
        print(i + " Not Downloaded")

files_and_modtimes = []
for dirpath, dirnames, filenames in os.walk(desktop):
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        modtime = os.stat(filepath).st_mtime
        files_and_modtimes.append((filepath, modtime))



# Sort the list of files by modification time
sorted_files = sorted(files_and_modtimes, key=lambda x: x[1])

for filepath, modtime in sorted_files:
    if filepath.endswith(".pdf") or filepath.endswith(".PDF"):
        reader = PdfReader(filepath)
        page = reader.getPage(1)
        extracted_text = str(page.extract_text())
        page_to_extract = 2  # extract table from page 1
        extracted = tabula.read_pdf(filepath, pages=page_to_extract)
        data = extracted[0].values.tolist()
        filtering_data = []
        for i in data:
            cleanedList = [x for x in i if str(x) != 'nan']
            filtering_data.append(cleanedList)


        date_list = ["MMTC Dispensations for " + extracted_text.split("MMTC Dispensations for ")[1].split(":")[0].replace(",","")]
        with open(desktop + 'history.csv', 'a', newline='') as fd:
            writer_object = writer(fd)
            writer_object.writerow(date_list)
            for row in filtering_data:
                writer_object.writerow(row)
            fd.close()






