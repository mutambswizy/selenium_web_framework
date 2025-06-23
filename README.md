# 🧪 Selenium Python Web Automation Framework

This project is a modular, maintainable Selenium test automation framework built using Python and PyTest with a Page Object Model (POM) architecture. It is designed to test the User List Table on [Way2Automation](http://www.way2automation.com/angularjs-protractor/webtables/) with CI/CD integration via GitHub Actions.

## 📁 Project Structure Overview

```
Selenium_web_framework/
├── tests/
├── pages/
├── utils/
├── reports/
│   ├── report.html
│   └── screenshots/
├── .github/workflows/
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Selenium_web_framework.git
   cd Selenium_web_framework
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   Create a `.env` file with:
   ```env
   BASE_URL=http://www.way2automation.com/angularjs-protractor/webtables/
   ```

## ▶️ How to Run the Tests

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```



## 📌 Assumptions & Design Decisions

- Page Object Model for maintainability
- PyTest + pytest-html for structured reporting
- GitHub Actions for CI/CD with artifact uploads

## 🛠️ Tools & Resources

| Tool               | Purpose                        |
|--------------------|--------------------------------|
| Selenium WebDriver | Browser automation             |
| PyTest             | Test runner                    |
| pytest-html        | HTML report generation         |
| GitHub Actions     | CI/CD pipeline                 |

## ✅ Sample Report & Screenshots

### 📄 HTML Report
See: `reports/report.html`

## Video Recording
https://github.com/user-attachments/assets/b318806b-4488-4308-a02b-1e678e18b3d7


### 📸 Screenshot
![image](https://github.com/user-attachments/assets/9f03ed62-bbbd-4d17-bba0-d9f62304fdf0)


## 🚀 CI/CD Pipeline

`.github/workflows/ci.yml` runs tests on push/PR and uploads `report.html` as artifact.

## 💬 Git Best Practices

- Feature branches (`feature/add-login-tests`)
- Descriptive commits (`feat: add screenshot support`)

## 👨‍💻 Author

**Wisdom Mutambirwa**
