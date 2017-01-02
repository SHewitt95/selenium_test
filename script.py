from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

if __name__ == "__main__":

    # Initiate driver.
    driver = webdriver.Chrome()
    driver.get("http://p2c.coralgables.com/Summary.aspx")
    
    # Get XPath's of elements
    agreeButtonXPath = '//*[@id="mainContent_CenterColumnContent_btnContinue"]'
    dateDropDownXPath = '//*[@id="mainContent_ddlDates2"]'
    areaDropDownXPath = '//*[@id="mainContent_ddlNeighbor2"]'
    searchButtonXPath = '//*[@id="mainContent_cmdSubmit2"]'

    # Get "Agree" button on redirect page.
    agreeButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(agreeButtonXPath))

    # Click "Agree" button on redirect page.
    agreeButtonElement.click()

    # Get dropdown elements for selecting date range and Police Reporting Area.
    dateDropDownElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(dateDropDownXPath))
    areaDropDownElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(areaDropDownXPath))

    # Make selection in dropdown menus.
    # CAREFUL: Selecting the date reloads the page, this it must be done last.
    Select(areaDropDownElement).select_by_visible_text("POLICE ZONE 07 (UM)")
    Select(dateDropDownElement).select_by_visible_text("Last Month")

    # Due to page reload, the Search button must be found AFTER the page relaods.
    searchButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(searchButtonXPath))
    searchButtonElement.click()

    # Get and parse given page's html.
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Find the table with the police records.
    myTable = soup.findAll('table', {"class":"DataGridText"})

    for td in myTable:
        print(td.text.encode('utf-8'))

    driver.quit()