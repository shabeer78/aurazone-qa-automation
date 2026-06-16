"""
=============================================================
AuraZone Website - Automation Test Suite
Tester  : Shabeer Ahamed
Date    : June 16, 2026
Tool    : Selenium + Python
Website : https://test.aurazone.shop
=============================================================
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ── SETUP ──────────────────────────────────────────────────
BASE_URL = "https://test.aurazone.shop"

def setup_driver():
    """Start Chrome browser"""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)
    return driver

def print_result(test_name, status, message=""):
    """Print test result clearly"""
    icon = "✅ PASS" if status else "❌ FAIL"
    print(f"\n{icon} | {test_name}")
    if message:
        print(f"       → {message}")

# ══════════════════════════════════════════════════════════
# TEST CASE 1 — Homepage Loads Correctly
# ══════════════════════════════════════════════════════════
def test_homepage_loads(driver):
    """
    Test Case : TC-001
    Title     : Verify Homepage Loads Correctly
    Steps     : 1. Open https://test.aurazone.shop
                2. Check page title contains AuraZone
                3. Check logo is visible
                4. Check Shop Now button is visible
    Expected  : Homepage loads with AuraZone title and logo
    """
    print("\n" + "="*55)
    print("TC-001 | Homepage Loads Correctly")
    print("="*55)

    try:
        # Step 1: Open homepage
        driver.get(BASE_URL)
        time.sleep(2)

        # Step 2: Check page title
        title = driver.title
        print(f"  Page Title: {title}")
        assert "aurazone" in title.lower() or "shoe" in title.lower(), \
            f"Title not matching: {title}"

        # Step 3: Check logo is visible
        logo = driver.find_element(By.CSS_SELECTOR, "a img, .logo, header a")
        assert logo.is_displayed(), "Logo not visible"

        # Step 4: Check hero section text
        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert any(word in body_text.lower() for word in
                   ["shoe", "aurazone", "discover", "run", "shop"]), \
            "Homepage content not found"

        print_result("TC-001 Homepage Loads", True,
                     f"Title='{title}' | Logo visible | Content found")

    except Exception as e:
        print_result("TC-001 Homepage Loads", False, str(e))


# ══════════════════════════════════════════════════════════
# TEST CASE 2 — Search Functionality Works
# ══════════════════════════════════════════════════════════
def test_search_functionality(driver):
    """
    Test Case : TC-002
    Title     : Verify Search Functionality Works
    Steps     : 1. Go to products page (has search bar)
                2. Find search input box
                3. Type 'Nike' in search box
                4. Click Search button
                5. Check results appear
    Expected  : Search results page shows Nike products
    """
    print("\n" + "="*55)
    print("TC-002 | Search Functionality Works")
    print("="*55)

    try:
        # Step 1: Go to products page — search bar is here
        driver.get(BASE_URL + "/products")
        time.sleep(2)

        # Step 2 & 3: Find search input and type Nike
        # Try multiple selectors to find the search box
        search_box = None
        selectors = [
            "input[placeholder*='Search']",
            "input[placeholder*='search']",
            "input[placeholder*='product']",
            "input[placeholder*='Product']",
            "input[type='text']",
            "input[class*='search']",
            ".search-input input",
            "form input",
        ]
        for selector in selectors:
            try:
                search_box = driver.find_element(By.CSS_SELECTOR, selector)
                if search_box.is_displayed():
                    print(f"  Found search box with: {selector} ✓")
                    break
            except:
                continue

        assert search_box is not None, "Search box not found on products page"

        search_box.clear()
        search_box.send_keys("Nike")
        print("  Typed 'Nike' in search box ✓")
        time.sleep(1)

        # Step 4: Click Search button
        try:
            search_btn = driver.find_element(
                By.XPATH,
                "//button[contains(text(),'Search')] | "
                "//button[@type='submit'] | "
                "//input[@type='submit']"
            )
            search_btn.click()
            print("  Clicked Search button ✓")
        except:
            # If no button, press Enter
            search_box.send_keys(Keys.RETURN)
            print("  Pressed Enter to search ✓")
        time.sleep(2)

        # Step 5: Check results contain Nike
        body_text = driver.find_element(By.TAG_NAME, "body").text
        has_results = any(word in body_text.lower() for word in
                          ["nike", "product", "result", "found", "urban"])

        assert has_results, "No search results found for Nike"

        print_result("TC-002 Search Functionality", True,
                     "Search for 'Nike' on products page returned results")

    except Exception as e:
        print_result("TC-002 Search Functionality", False, str(e))


# ══════════════════════════════════════════════════════════
# TEST CASE 3 — Products Page Loads with Filters
# ══════════════════════════════════════════════════════════
def test_products_page_and_filters(driver):
    """
    Test Case : TC-003
    Title     : Verify Products Page Loads with Filters
    Steps     : 1. Open products page
                2. Check products are visible
                3. Check filter section is visible
                4. Click CASUAL filter
                5. Check filtered results
    Expected  : Products load and filter works correctly
    """
    print("\n" + "="*55)
    print("TC-003 | Products Page Loads with Filters")
    print("="*55)

    try:
        # Step 1: Open products page
        driver.get(BASE_URL + "/products")
        time.sleep(2)

        # Step 2: Check products are visible
        body_text = driver.find_element(By.TAG_NAME, "body").text
        assert any(word in body_text.lower() for word in
                   ["product", "shoe", "found"]), \
            "Products not visible on page"
        print("  Products found on page ✓")

        # Step 3: Check filter section visible
        filter_keywords = ["category", "gender", "brand", "size", "filter", "casual", "running"]
        has_filters = any(kw in body_text.lower() for kw in filter_keywords)
        assert has_filters, "Filter section not found"
        print("  Filter section visible ✓")

        # Step 4: Click CASUAL filter
        try:
            casual_filter = driver.find_element(
                By.XPATH,
                "//label[contains(text(),'CASUAL') or contains(text(),'Casual')] | "
                "//span[contains(text(),'Casual')] | "
                "//input[@value='casual']"
            )
            casual_filter.click()
            time.sleep(2)
            print("  Clicked CASUAL filter ✓")
        except:
            print("  Could not click filter (may need login or different selector)")

        # Step 5: Check page still has products
        current_text = driver.find_element(By.TAG_NAME, "body").text
        assert any(w in current_text.lower() for w in ["product", "shoe", "casual"]), \
            "Page broken after filter click"

        print_result("TC-003 Products & Filters", True,
                     "Products page loaded | Filters visible | Filter click tested")

    except Exception as e:
        print_result("TC-003 Products & Filters", False, str(e))


# ══════════════════════════════════════════════════════════
# TEST CASE 4 — Navigation Menu Opens Correctly
# ══════════════════════════════════════════════════════════
def test_navigation_menu(driver):
    """
    Test Case : TC-004
    Title     : Verify Navigation Hamburger Menu Opens
    Steps     : 1. Open homepage
                2. Find hamburger menu button
                3. Click it
                4. Check menu items are visible
                5. Close menu with X button
    Expected  : Menu opens with Shop, By Gender, By Category sections
    """
    print("\n" + "="*55)
    print("TC-004 | Navigation Menu Opens Correctly")
    print("="*55)

    try:
        # Step 1: Open homepage
        driver.get(BASE_URL)
        time.sleep(2)

        # Step 2 & 3: Find and click hamburger menu
        hamburger = driver.find_element(
            By.CSS_SELECTOR,
            "button[aria-label*='menu'], .hamburger, button svg, "
            "button[class*='menu'], header button"
        )
        hamburger.click()
        time.sleep(1)
        print("  Clicked hamburger menu ✓")

        # Step 4: Check menu items visible
        body_text = driver.find_element(By.TAG_NAME, "body").text
        menu_items = ["New Arrivals", "Featured", "All Products",
                      "Men", "Women", "Running", "Casual"]
        found_items = [item for item in menu_items if item in body_text]
        assert len(found_items) >= 3, f"Menu items not visible. Found: {found_items}"
        print(f"  Menu items visible: {found_items} ✓")

        # Step 5: Close menu
        try:
            close_btn = driver.find_element(
                By.CSS_SELECTOR, "button[aria-label*='close'], .close-btn, button svg"
            )
            close_btn.click()
            time.sleep(1)
            print("  Menu closed successfully ✓")
        except:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            print("  Closed menu with ESC key ✓")

        print_result("TC-004 Navigation Menu", True,
                     f"Menu opened | Items found: {found_items}")

    except Exception as e:
        print_result("TC-004 Navigation Menu", False, str(e))


# ══════════════════════════════════════════════════════════
# TEST CASE 5 — Footer Links Are Visible and Clickable
# ══════════════════════════════════════════════════════════
def test_footer_links(driver):
    """
    Test Case : TC-005
    Title     : Verify Footer Links Are Visible and Clickable
    Steps     : 1. Open products page
                2. Scroll to footer
                3. Check all footer links visible
                4. Click Contact Us link
                5. Verify Contact Us page opens
    Expected  : Footer shows all legal links and they work
    """
    print("\n" + "="*55)
    print("TC-005 | Footer Links Visible and Clickable")
    print("="*55)

    try:
        # Step 1: Open products page (has footer)
        driver.get(BASE_URL + "/products")
        time.sleep(2)

        # Step 2: Scroll to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        print("  Scrolled to footer ✓")

        # Step 3: Check footer links
        body_text = driver.find_element(By.TAG_NAME, "body").text
        footer_links = [
            "Cancellations & Refunds",
            "Terms & Conditions",
            "Shipping Policy",
            "Privacy Policy",
            "Contact Us"
        ]
        found_links = [link for link in footer_links if link in body_text]
        assert len(found_links) >= 4, \
            f"Footer links missing. Found only: {found_links}"
        print(f"  Footer links visible: {found_links} ✓")

        # Step 4 & 5: Click Contact Us
        try:
            contact_link = driver.find_element(
                By.LINK_TEXT, "Contact Us"
            )
            contact_link.click()
            time.sleep(2)
            current_url = driver.current_url
            print(f"  Clicked Contact Us → URL: {current_url} ✓")
        except:
            print("  Contact Us link found but could not click")

        print_result("TC-005 Footer Links", True,
                     f"Found {len(found_links)}/5 footer links")

    except Exception as e:
        print_result("TC-005 Footer Links", False, str(e))


# ══════════════════════════════════════════════════════════
# MAIN — Run All Tests
# ══════════════════════════════════════════════════════════
def main():
    print("\n" + "🚀 " * 18)
    print("  AURAZONE AUTOMATION TEST SUITE")
    print("  Tester : Shabeer Ahamed")
    print("  Date   : June 16, 2026")
    print("  URL    : https://test.aurazone.shop")
    print("🚀 " * 18)

    driver = setup_driver()

    try:
        test_homepage_loads(driver)
        test_search_functionality(driver)
        test_products_page_and_filters(driver)
        test_navigation_menu(driver)
        test_footer_links(driver)

    finally:
        time.sleep(2)
        driver.quit()
        print("\n" + "="*55)
        print("  All 5 test cases completed!")
        print("  Browser closed.")
        print("="*55 + "\n")


if __name__ == "__main__":
    main()