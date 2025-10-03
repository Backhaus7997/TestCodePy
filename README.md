
# Demoblaze E2E Automation (Pytest + Selenium)

Automatización de flujos core en [demoblaze.com](https://www.demoblaze.com/): Login, navegación, agregado al carrito, verificación de totales y checkout (Place Order).  
Diseño con **Page Object Model**, ejecución en **Chrome** y **Firefox**, reporte **pytest-html**, y **GitHub Actions** con matriz de navegadores.

> Este repo adapta los requerimientos típicos del code challenge (POM, Selenium, PyTest, reporte y CI/CD). fileciteturn0file0

## Requisitos
- Python 3.10+
- Navegadores: Chrome y/o Firefox
- (Opcional) Headless por default

## Instalación
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecutar pruebas
```bash
# Chrome headless (default)
pytest -v --html=report.html --self-contained-html

# Firefox
pytest -v --browser firefox --html=report.html --self-contained-html

# UI visible
pytest -v --headed
```

Puedes combinar flags, por ejemplo:
```bash
pytest -v --browser firefox --headed --html=report.html --self-contained-html
```

## Variables útiles
- `--base-url` para apuntar a otro entorno (default: https://www.demoblaze.com/)
- `--wait` segundos de espera explícita (default: 10)

## Estructura
```
demoblaze-automation/
├─ pages/
│  ├─ base_page.py
│  ├─ home_page.py
│  ├─ auth_modals.py
│  ├─ product_page.py
│  └─ cart_page.py
├─ tests/
│  ├─ test_01_login.py
│  ├─ test_02_add_to_cart.py
│  ├─ test_03_cart_totals.py
│  └─ test_04_checkout.py
├─ utils/
│  └─ data.py
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
└─ .github/workflows/ci.yml
```

## CI en GitHub Actions
- Matriz de **chrome** y **firefox**
- Genera `report.html` como artefacto

## Nota sobre credenciales
Demoblaze permite **Signup** y **Login** por modales. En las pruebas se genera un usuario único con timestamp para asegurar independencia entre corridas.

---

## AI usage (breve)
- Generación inicial del boilerplate y estructura POM
- Búsqueda de selectores basada en conocimiento del sitio (sin navegación asistida en este entorno)
- Decisiones manuales en esperas y desacople de fixtures

