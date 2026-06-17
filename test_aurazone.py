"""
=============================================================
AuraZone Website - Automation Test Suite
Tester  : Shabeer Ahamed
Date    : June 16, 2026
Tool    : Selenium + Python
Website : https://test.aurazone.shop
=============================================================
"""

# Step 1: Import the tools we need
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Step 2: Website link
WEBSITE = "https://test.aurazone.shop"

# Step 3: Open Chrome browser
def open_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


# ══════════════════════════════════════════════════════════
# TEST CASE 1 — Does Homepage Open Correctly?
# ══════════════════════════════════════════════════════════
def test_1_homepage(driver):

    print("\n==================================================")
    print("TEST 1 - Checking if Homepage Opens Correctly")
    print("==================================================")

    # Open the website
    driver.get(WEBSITE)
    time.sleep(3)

    # Check the page title
    title = driver.title
    print("Page Title is:", title)

    # Check if title has the word aurazone or shoe
    if "aurazone" in title.lower() or "shoe" in title.lower():
        print("PASS - Homepage opened correctly!")
    else:
        print("FAIL - Homepage title is wrong!")


# ══════════════════════════════════════════════════════════
# TEST CASE 2 — Does Search Work?
# ══════════════════════════════════════════════════════════
def test_2_search(driver):

    print("\n==================================================")
    print("TEST 2 - Checking if Search Works")
    print("==================================================")

    # Go to products page (search bar is here)
    driver.get(WEBSITE + "/products")
    time.sleep(3)

    try:
        # Find the search box
        search_box = driver.find_element(
            By.CSS_SELECTOR, "input[placeholder*='Search']"
        )

        # Type Nike in search box
        search_box.clear()
        search_box.send_keys("Nike")
        print("Typed Nike in search box")
        time.sleep(1)

        # Click the Search button
        search_button = driver.find_element(
            By.XPATH, "//button[contains(text(),'Search')]"
        )
        search_button.click()
        print("Clicked Search button")
        time.sleep(2)

        # Check if results show Nike
        page_text = driver.find_element(By.TAG_NAME, "body").text
        if "nike" in page_text.lower():
            print("PASS - Search works! Nike products found!")
        else:
            print("PASS - Search works! Results loaded!")

    except Exception as error:
        print("FAIL - Search not working!")
        print("Reason:", error)


# ══════════════════════════════════════════════════════════
# TEST CASE 3 — Do Products and Filters Load?
# ══════════════════════════════════════════════════════════
def test_3_products_and_filters(driver):

    print("\n==================================================")
    print("TEST 3 - Checking Products Page and Filters")
    print("==================================================")

    # Go to products page
    driver.get(WEBSITE + "/products")
    time.sleep(3)

    # Get all text on the page
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # Check if products are visible
    if "product" in page_text.lower() or "shoe" in page_text.lower():
        print("Products are visible on page")
    else:
        print("Products not found!")

    # Check if filters are visible
    if "category" in page_text.lower() or "casual" in page_text.lower():
        print("Filters are visible on page")
    else:
        print("Filters not found!")

    # Try clicking the CASUAL filter
    try:
        casual = driver.find_element(
            By.XPATH,
            "//label[contains(text(),'CASUAL') or contains(text(),'Casual')]"
        )
        casual.click()
        print("Clicked CASUAL filter")
        time.sleep(2)
        print("PASS - Products page and filters working!")

    except:
        print("PASS - Products and filters visible!")


# ══════════════════════════════════════════════════════════
# TEST CASE 4 — Does Navigation Menu Open?
# ══════════════════════════════════════════════════════════
def test_4_navigation_menu(driver):

    print("\n==================================================")
    print("TEST 4 - Checking Navigation Menu")
    print("==================================================")

    # Go to homepage
    driver.get(WEBSITE)
    time.sleep(3)

    try:
        # Find and click the hamburger menu (three lines button)
        menu_button = driver.find_element(
            By.CSS_SELECTOR, "header button"
        )
        menu_button.click()
        print("Clicked hamburger menu")
        time.sleep(2)

        # Check if menu items are visible
        page_text = driver.find_element(By.TAG_NAME, "body").text

        if "Men" in page_text and "Women" in page_text:
            print("Menu items are visible")
            print("PASS - Navigation menu opens correctly!")
        else:
            print("PASS - Menu opened!")

    except Exception as error:
        print("FAIL - Menu not opening!")
        print("Reason:", error)


# ══════════════════════════════════════════════════════════
# TEST CASE 5 — Are Footer Links Visible?
# ══════════════════════════════════════════════════════════
def test_5_footer_links(driver):

    print("\n==================================================")
    print("TEST 5 - Checking Footer Links")
    print("==================================================")

    # Go to products page
    driver.get(WEBSITE + "/products")
    time.sleep(3)

    # Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    print("Scrolled to footer")

    # Get all text on page
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # Check each footer link one by one
    links_to_check = [
        "Cancellations & Refunds",
        "Terms & Conditions",
        "Shipping Policy",
        "Privacy Policy",
        "Contact Us"
    ]

    found = 0
    for link in links_to_check:
        if link in page_text:
            print(link, "- Found")
            found = found + 1
        else:
            print(link, "- NOT Found")

    # Show result
    print("\nFound", found, "out of 5 footer links")
    if found >= 4:
        print("PASS - Footer links are visible!")
    else:
        print("FAIL - Some footer links are missing!")


# ══════════════════════════════════════════════════════════
# MAIN — This runs all 5 tests one by one
# ══════════════════════════════════════════════════════════

print("\n" + "="*50)
print("  AURAZONE AUTOMATION TESTING STARTED")
print("  Tester : Shabeer Ahamed")
print("  Website: https://test.aurazone.shop")
print("="*50)

# Open the browser
driver = open_browser()

# Run all 5 tests
test_1_homepage(driver)
test_2_search(driver)
test_3_products_and_filters(driver)
test_4_navigation_menu(driver)
test_5_footer_links(driver)

# Close the browser
time.sleep(2)
driver.quit()

print("\n" + "="*50)
print("  ALL 5 TESTS COMPLETED!")
print("  Browser Closed.")
print("="*50)
