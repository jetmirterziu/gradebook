# GRADEBOOK APP

A command line Gradebook system built in Python.
<br>It allows you to manage **Students**, **Courses**, **Enrollments**, and **Grades** — with persistent JSON storage, logging, and data validation.


## Project Structure
gradebook/
<br>├── gradebook/
<br>│ ├── init.py
<br>│ ├── models.py # -- Core data models
<br>│ ├── storage.py # -- Data loading/saving with logging
<br>│ ├── service.py # -- Business logic (add, list, GPA, etc.)
<br>│
<br>├── scripts/
<br>│ └── seed.py #  -- Script to populate demo data
<br>│
<br>├── tests/
<br>│ └── test_service.py # -- Unit tests using pytest
<br>│
<br>├── data/
<br>│ └── gradebook.json # -- Stored data file (auto-created)
<br>│
<br>├── main.py # -- Command-line interface (CLI)
<br>├── requirements.txt # -- Dependencies
<br>└── README.md # -- Project documentation




## Features
1. Add and list **students** and **courses**  
2. **Enroll** students in courses  
3. Add and validate **grades** (0–100)  
4. Compute **average** per course and **GPA** per student  
5. Data persistence in JSON  
6. Logging of all operations  
7. Fully **PEP 8** compliant  
8. **Unit tested** with `pytest`  
9. **Seed script** to populate demo data  


## Installation

```bash
# 1. Clone the repository
git clone https://github.com/jetmirterziu/gradebook.git
cd gradebook

# 2. Create and activate a virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```
## Usage
Run the CLI:
```python main.py add-student --name "Alice"
python main.py add-course --code CS101 --title "Intro to CS"
python main.py enroll --student-id 1 --course-code CS101
python main.py add-grade --student-id 1 --course-code CS101 --grade 95
python main.py list students
python main.py avg --student-id 1 --course-code CS101
python main.py gpa --student-id 1
```

Run the Seed Script:
```bash
python -m scripts.seed
```

Run tests:
```bash
pytest -v
```
Logging:
<br>Logs are automatically written to:
```bash
logs/app.log
```
Each operation (add, enroll, save, etc.) is timestamped for traceability.


***Author***

Jetmir Terziu
<br>Project for Python & Data Management Assessment
(2025)