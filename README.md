
# Demoblaze E2E Automation (Pytest + Selenium)

Automated end-to-end tests for [**demoblaze.com**](https://www.demoblaze.com/) covering:  
- Signup & Login  
- Product navigation  
- Add to Cart  
- Cart totals validation  
- Checkout (*Place Order*)  

Built with the **Page Object Model (POM)** pattern, runs on **Chrome** and **Firefox**, generates **pytest-html** reports, and integrates with **GitHub Actions** using a browser matrix.

---

## Requirements
- Python **3.10+**
- Browsers: **Chrome** and/or **Firefox**
- Headless mode supported (default)

---

## Installation

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate      # On Linux / Mac
.venv\Scripts\Activate.ps1     # On Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

---

## Running Tests

```bash
# Chrome (headless by default)
pytest -v --html=report.html --self-contained-html

# Firefox
pytest -v --browser firefox --html=report.html --self-contained-html

# Run with browser UI (headed)
pytest -v --headed
```

Flags can be combined, for example:

```bash
pytest -v --browser firefox --headed --html=report.html --self-contained-html
```

---

## Useful CLI Options

| Option        | Default | Description                                |
|---------------|---------|--------------------------------------------|
| `--base-url`  | https://www.demoblaze.com/ | Target environment base URL |
| `--wait`      | 10      | Explicit wait timeout (in seconds)         |
| `--browser`   | chrome  | Browser: `chrome` or `firefox`             |
| `--headed`    | *off*   | Show browser UI instead of headless mode   |

---

## Project Structure

```
demoblaze-automation/
├─ pages/              # Page Object Model classes
│  ├─ base_page.py
│  ├─ home_page.py
│  ├─ auth_modals.py
│  ├─ product_page.py
│  └─ cart_page.py
├─ tests/              # Test cases
│  ├─ test_01_login.py
│  ├─ test_02_add_to_cart.py
│  ├─ test_03_cart_totals.py
│  └─ test_04_checkout.py
├─ utils/              # Helpers
│  └─ data.py
├─ conftest.py         # Pytest fixtures & setup
├─ pytest.ini
├─ requirements.txt
└─ .github/workflows/ci.yml
```

---

## CI/CD with GitHub Actions
- Runs in a **matrix** of `chrome` and `firefox`
- Generates `report.html` and uploads it as an artifact

---

## Credentials Note
- Demoblaze provides **Signup** and **Login** via modals.  
- Tests generate **unique users** (with timestamps) to avoid conflicts across runs.

---

## AI Usage (disclosure)
- Generated boilerplate and Page Object Model structure  
- Selectors chosen based on site knowledge  
- Waits and fixtures tuned manually  
