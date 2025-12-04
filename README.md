
🚀 Internship Project: Backend Development using FastAPI

📌 Overview

This project was developed during a 1-month internship focused on Backend Development using FastAPI.
It demonstrates how to build RESTful APIs, perform CRUD operations, and use a mock JSON database powered by JSON-Server.


---

🛠 Technologies & Tools

Python – Backend programming

FastAPI – API framework

JSON-Server – Mock database

Swagger-UI – Interactive API docs

Postman / REST Client – API testing

Git & GitHub – Version control



---

📁 Project Structure

Internship/
├── database/
│   └── db.json          # Mock database
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
└── README.md


---

⚙ Setup & Installation

⿡ Clone the Repository

git clone https://github.com/sreejarachakonda/Internship.git
cd Internship

⿢ Create and Activate a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

Linux / Mac

python -m venv venv
source venv/bin/activate

⿣ Install Dependencies

pip install -r requirements.txt

⿤ Run the FastAPI Server

uvicorn main:app --reload

⿥ Run JSON-Server (Mock Database)

json-server --watch database/db.json --port 3000


---

📄 API Documentation

Swagger-UI is available at:
👉 http://127.0.0.1:8000/docs
