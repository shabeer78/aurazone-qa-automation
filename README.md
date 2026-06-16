# 🧪 AuraZone QA Automation

Automated test suite for the AuraZone e-commerce website built using Python and Selenium WebDriver.

---

## 📌 About the Project

- **Website Tested:** https://test.aurazone.shop
- **Type:** E-commerce Shoe Store
- **Tester:** Shabeer Ahamed
- **Date:** June 16, 2026
- **Purpose:** QA Intern Assignment — Zansphere

---

## ✅ Test Cases

| Test ID | Test Case | Description |
|---------|-----------|-------------|
| TC-001 | Homepage Loads | Verifies homepage loads with title, logo and content |
| TC-002 | Search Functionality | Searches for 'Nike' and verifies results appear |
| TC-003 | Products Page & Filters | Verifies products load and filter sidebar works |
| TC-004 | Navigation Menu | Verifies hamburger menu opens with correct items |
| TC-005 | Footer Links | Verifies all footer links are visible and clickable |

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| Python 3.x | Programming language |
| Selenium WebDriver | Browser automation |
| WebDriver Manager | Auto installs Chrome driver |
| Google Chrome | Browser used for testing |

---

## ⚙️ Setup Instructions

### Step 1 — Make sure Python is installed
```
python --version
```
If not installed, download from https://python.org

### Step 2 — Install required libraries
```
pip install selenium
pip install webdriver-manager
```

### Step 3 — Download the test file
Save `test_aurazone.py` to your computer

---

## ▶️ How to Run

### Open Command Prompt and run:
```
python test_aurazone.py
```

### Expected Output:
```
✅ PASS | TC-001 Homepage Loads
✅ PASS | TC-002 Search Functionality
✅ PASS | TC-003 Products & Filters
✅ PASS | TC-004 Navigation Menu
✅ PASS | TC-005 Footer Links

All 5 test cases completed!
```

---

## 📁 Project Structure

```
aurazone-qa-automation/
│
├── test_aurazone.py   ← Main automation test file
└── README.md          ← Project documentation
```

---

## 🐛 Bugs Found During Testing

| Bug ID | Description | Severity |
|--------|-------------|----------|
| BUG-001 | Missing product image on Executive Leather Oxford | High |
| BUG-002 | Amazon watermark on Lunar Glide product image | High |
| BUG-003 | Unrealistic prices Rs.95 and Rs.120 for branded shoes | Medium |
| BUG-004 | Size filter not in correct ascending order | Medium |
| BUG-005 | Inconsistent size format — Indian and US sizes mixed | Medium |
| BUG-006 | Page becomes grey when hamburger menu opens | Medium |

---

## 👤 Author

**Shabeer Ahamed**
- GitHub: github.com/shabeer78
- Email: shabeerahamed781@gmail.com
