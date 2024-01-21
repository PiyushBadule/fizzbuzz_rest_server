<div align="center">
    <h1>🚀 FizzBuzz REST Server 🚀</h1>
</div>

<p align="center">
    <i>A robust, production-ready server implementing the classic Fizz-Buzz logic with REST API support.</i>
</p>

<div align="center">


</div>

---

## 📖 Table of Contents
- 🔍 [Overview](#-overview)
- 🧩 [Features](#-features)
- 🔧 [Installation](#-installation)
- 🌐 [Access the Application](#-access-the-application)
- 📁 [Project Structure](#-project-structure)
- 📚 [Third-Party Libraries](#-third-party-libraries)
- 📜 [API Documentation](#-api-documentation)
- 🎮 [Usage](#-usage)
- ⚖️ [License](#-license)
- ✉️ [Contact](#-contact)
- 📝 [Instructions](#-instructions)

---

## 🔍 Overview
FizzBuzz REST Server is a robust, production-ready server that implements the classic Fizz-Buzz logic. It exposes a REST API endpoint to process Fizz-Buzz requests, along with a statistical endpoint to track and report the most frequently used requests.

## 🧩 Features 
### 1. REST API Endpoint
   - Accepts five parameters: three integers (`first_int`, `second_int`, `limit`) and two strings (`first_str`, `second_str`).
   - Data validation is managed using Pydantic models.
   - Returns a list of strings from 1 to `limit` with FizzBuzz logic applied.
   
### 2. Statistics Endpoint
   - No-parameter endpoint returning the most used request's parameters and their count.
   - Statistics are tracked and managed using SQLAlchemy for database interactions.

## 🔧 Installation

**Python Version >= 3.9**

To set up the FizzBuzz REST Server:
1. **Clone the Repository**
   ```bash
   git clone https://github.com/PiyushBadule/fizzbuzz_restapi.git
   cd fizzbuzz-flask
   ```
2. **Set up a Virtual Environment** 

   - **WINDOWS**
   ```bash
   python -m venv venv
   venv\Scripts\activate.ps1
   ```
   - **LINUX or Mac**
   ```bash
   python -m venv venv
   source venv\Scripts\activate
   ``` 

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Running the Application**
   ```bash
   # Start the Flask Server
   python main.py
   ```

## 🌐 Access the Application
Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## 📁 Project Structure
```plaintext
fizzbuzz_app/
├── app/
│ ├── __init__.py
│ ├── api_routes.py
│ ├── constants.py
│ ├── frontend_routes.py
│ ├── models_pydantic.py
│ ├── urls.py
│ └── utils.py
│
├── database_handler/
│ ├── __init__.py
│ ├── fizzbuzz.db
│ └── models.py
│
├── logs/
│ ├── __init__.py
│ ├── app.log
│ └── logger.py
│
├── static/
│ ├── css/
│ │   ├── 404_style.css
│ │   ├── error_style.css
│ │   ├── home_style.css
│ │   ├── result_style.css
│ │   └── statistics_style.css
│ └── openapi.yaml
│
├── templates/
│ ├── 404.html
│ ├── error.html
│ ├── home.html
│ ├── result.html
│ └── statistics.html
│
├── tests/
│ ├── __init__.py
│ ├── test_database_handler.py
│ ├── test_fizzbuzz_service.py
│ └── test_flask_routes.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 📚 Third-Party Libraries
- **Flask**: A web application framework for creating API endpoints.
- **SQLite**: A lightweight database for tracking request statistics.
- **SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, a powerful ORM and database toolkit for Python.
- **Pydantic**: For data validation and settings management using Python type annotations.
- **Requests**: A simple, yet elegant HTTP library for making requests and handling responses in Python.


## 📜 API Documentation
Detailed API documentation is available to describe all the endpoints, parameters, and expected responses.

- **Interactive API Docs (Swagger UI)**: If you've integrated Swagger UI, you can access the interactive documentation by navigating to `/api/docs` on your running server. Example: [http://127.0.0.1:5000/api/docs](http://127.0.0.1:5000/api/docs)
- **OpenAPI Specification**: You can view the OpenAPI specification in YAML format [here](/static/openapi.yaml).

## 🎮 Usage
- **FizzBuzz Game**: Enter parameters on the homepage and submit to see the result.
- **Statistics**: View the most used FizzBuzz parameters by clicking the 'View Statistics' link.
- **Contributing**: Contributions are welcome. Please fork the repository and submit a pull request with your proposed changes.

## ⚖️ License
This project is open source.

## ✉️ Contact
For questions or feedback, please contact me at [piyush.badule30@gmail.com](mailto:piyush.badule30@gmail.com).

Project maintained by Piyush Badule.

### 📝 Instructions:
1. **Folder Structure:** The folder structure is detailed to give a clear view of the project layout.
2. **Further Customization:** Feel free to add or modify sections to suit your project's specifics or personal preferences.
