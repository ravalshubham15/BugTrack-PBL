# 🐞 BugTrack — Software Bug Reporting & Tracking System

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Django-5.2+-092E20?style=for-the-badge&logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white">

</p>

<p align="center">
<strong>🚀 Report • Track • Manage • Resolve</strong>
</p>

---

## 📌 About The Project

**BugTrack** is a modern, simple and user-friendly web-based **Software Bug Reporting & Tracking System** developed using **Python and Django**.

The purpose of this project is to provide a centralized platform where users can report software bugs and developers can manage, assign, track and resolve those bugs efficiently.

### 🔄 Bug Lifecycle

**🐞 Report → 🏷️ Categorize → 🚨 Prioritize → 👨‍💻 Assign → 🛠️ Work → ✅ Resolve**

---

## 🎯 Project Objectives

- 🐞 Provide an organized platform for reporting software bugs
- 📋 Maintain bug records in a centralized database
- 👨‍💻 Assign bugs to developers
- 🚦 Track bug status throughout development
- 🚨 Manage bug priority
- 🏷️ Categorize bugs
- 🔎 Search and filter bug records
- 📊 Display useful bug statistics
- 🔐 Provide secure user authentication
- 🛠️ Provide administrative management through Django Admin

---

## ✨ Key Features

### 🔐 User Authentication

- 📝 User Registration
- 🔑 User Login
- 🚪 User Logout
- 🔒 Authentication-protected pages

### 📊 Dashboard

- 📌 Total Bugs
- 🟢 Open Bugs
- 🟡 In Progress Bugs
- 🔵 Resolved Bugs

### 🐞 Bug Management

- ➕ Report a new bug
- 👁️ View bug details
- ✏️ Edit bug information
- 🗑️ Delete bugs
- 👨‍💻 Assign bugs to developers
- 🔄 Change bug status

### 🏷️ Bug Categories

- 🎨 UI/UX
- ⚙️ Functional
- 🗄️ Database
- 🔐 Security
- ⚡ Performance

### 🚨 Bug Priority

- 🟢 Low
- 🟡 Medium
- 🟠 High
- 🔴 Critical

### 🚦 Bug Status

- 🟢 Open
- 🟡 In Progress
- 🔵 Resolved

### 🔎 Search & Filtering

Users can search bugs by title or description and filter them by:

- 🚦 Status
- 🚨 Priority
- 🏷️ Category

### 👨‍💻 Developer Assignment

A reported bug can be assigned to a registered developer/user for development and resolution.

### 🛠️ Admin Panel

Django's built-in Admin Panel allows authorized administrators to manage users and bug records.

---

## 🏗️ Project Architecture

                         👤 User
                           │
                           ▼
                    🌐 Web Interface
                           │
                           ▼
                    🐍 Django Backend
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Views.py     Forms.py     URLs.py
              │
              ▼
           🗄️ Models
              │
              ▼
          💾 SQLite DB

---

## 🔄 System Workflow

👤 User Registration
        │
        ▼
🔑 Login
        │
        ▼
📊 Dashboard
        │
        ▼
🐞 Report Bug
        │
        ▼
🏷️ Select Category
        │
        ▼
🚨 Set Priority
        │
        ▼
👨‍💻 Assign Developer
        │
        ▼
🟢 Open
        │
        ▼
🟡 In Progress
        │
        ▼
🔵 Resolved

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🌐 Django | Backend Web Framework |
| 🧱 HTML5 | Web Structure |
| 🎨 CSS3 | Styling |
| 🅱️ Bootstrap | Responsive User Interface |
| ⚡ JavaScript | Client-side Functionality |
| 🗄️ SQLite | Database |
| 🔧 Git | Version Control |
| 🐙 GitHub | Code Hosting |
| 💻 VS Code | Development Environment |

---

## 📂 Project Structure

BugTrack_PBL/
│
├── 📁 BugTrack/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── 📁 bugapp/
│   ├── 📁 migrations/
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── 0002_bug_category.py
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
│
├── 📁 templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── bug_list.html
│   ├── bug_form.html
│   ├── bug_detail.html
│   └── bug_confirm_delete.html
│
├── 📁 static/
│   └── 📁 css/
│       └── style.css
│
├── 📄 manage.py
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md

---

## 🗄️ Database Design

BugTrack uses **SQLite** as its database.

### 🐞 Bug Model

| Field | Description |
|---|---|
| 🆔 `id` | Unique Bug ID |
| 📝 `title` | Bug title |
| 📄 `description` | Detailed bug description |
| 🏷️ `category` | Bug category |
| 🚨 `priority` | Bug priority |
| 🚦 `status` | Current bug status |
| 👤 `reported_by` | User who reported the bug |
| 👨‍💻 `assigned_to` | Developer assigned to the bug |
| 📅 `created_at` | Bug creation date and time |
| 🔄 `updated_at` | Last updated date and time |

The project also uses Django's built-in **User model** for authentication.

### 🏷️ Bug Categories

- UI/UX
- Functional
- Database
- Security
- Performance

### 🚨 Priority Types

- Low
- Medium
- High
- Critical

### 🚦 Status Types

- Open
- In Progress
- Resolved

---

## 🖥️ Application Pages

### 🔐 Authentication

- 📝 Register
- 🔑 Login
- 🚪 Logout

### 📊 Main Application

- 🏠 Dashboard
- ➕ Report Bug
- 📋 All Bugs
- 👁️ Bug Details
- ✏️ Edit Bug
- 🗑️ Delete Bug

### ⚙️ Administration

- 🛠️ Django Admin Panel

---

## 🔍 Search & Filtering

### 🔎 Search

- 🐞 Bug Title
- 📄 Bug Description

### 🎯 Filters

- 🚦 Status
- 🚨 Priority
- 🏷️ Category

### Example

Search   : Login button
Status   : Open
Priority : High
Category : Functional

---

## 🔐 Security

- 🔒 Django Authentication
- 🔐 Secure Password Handling
- 🛡️ CSRF Protection
- 🔑 Admin Authentication
- 🚫 Database exclusion from Git
- 🚫 Environment file exclusion from Git
- 👤 Login-protected application pages

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/ravalshubham15/BugTrack-PBL.git

### 2️⃣ Open the Project Folder

cd BugTrack-PBL

### 3️⃣ Install Dependencies

py -m pip install -r requirements.txt

### 4️⃣ Create Migrations

py manage.py makemigrations

### 5️⃣ Apply Migrations

py manage.py migrate

### 6️⃣ Create Superuser

py manage.py createsuperuser

### 7️⃣ Start the Development Server

py manage.py runserver

### 8️⃣ Open the Application

http://127.0.0.1:8000/

### 🛠️ Admin Panel

http://127.0.0.1:8000/admin/

---

## 🧪 Example Bug Workflow

### 1️⃣ Report Bug

Title       : Login button not working

Description : Login button does not respond after entering valid credentials.

Category    : Functional

Priority    : High

Status      : Open

### 2️⃣ Assign Developer

The reported bug is assigned to a developer.

### 3️⃣ Development

🟢 Open
   ↓
🟡 In Progress

### 4️⃣ Resolution

🔵 Resolved

---

## 🎓 Project Based Learning

This project was developed as a **Project Based Learning (PBL)** web application.

The project demonstrates practical implementation of:

- 🐍 Python Programming
- 🌐 Django Web Development
- 🗄️ Database Management
- 🔐 Authentication
- 📝 Django Forms
- 🔄 CRUD Operations
- 🔎 Search & Filtering
- 👨‍💻 Developer Assignment
- 📊 Dashboard Development
- 🛠️ Django Admin
- 🔧 Git & GitHub

---

## 🎯 Learning Outcomes

Through this project, we learned:

- 🐍 Python programming
- 🌐 Django web development
- 🧩 Django MVT architecture
- 🗄️ Database design
- 🔐 Authentication implementation
- 📝 Django forms
- 🔄 CRUD operations
- 🔎 Search and filtering
- 📊 Dashboard development
- 🛠️ Django Admin
- 🔧 Git version control
- 🐙 GitHub repository management
- 🤝 Team-based project development

---

## 🚀 Future Improvements

Possible future enhancements include:

- 📎 Bug screenshot/file attachments
- 💬 Bug comments
- 🔔 Email notifications
- 🔔 In-app notifications
- 📅 Bug due dates
- 📈 Advanced analytics
- 🌙 Dark mode
- ☁️ Cloud deployment
- 🐘 PostgreSQL database
- 📱 Improved mobile interface

---

## 📸 Screenshots

Recommended screenshots:

1. 🔐 Login Page
2. 📝 Registration Page
3. 📊 Dashboard
4. ➕ Report Bug Page
5. 📋 All Bugs Page
6. 👁️ Bug Details Page
7. ✏️ Edit Bug Page
8. 🛠️ Django Admin Panel

---

## 📋 Project Information

| Information | Details |
|---|---|
| 🐞 Project Name | BugTrack |
| 📚 Project Type | Project Based Learning |
| 🌐 Application Type | Web Application |
| 🐍 Backend | Python + Django |
| 🎨 Frontend | HTML + CSS + Bootstrap |
| 🗄️ Database | SQLite |
| 🔧 Version Control | Git |
| 🐙 Repository | GitHub |
| 💻 IDE | Visual Studio Code |

### 🔗 GitHub Repository

https://github.com/ravalshubham15/BugTrack-PBL

---

## 📜 License

This project was developed for **educational and academic purposes** as part of a Project Based Learning (PBL) activity.

---

## 🙏 Acknowledgement

We would like to sincerely thank our faculty members and institute for providing us with the opportunity to develop this project as part of our **Project Based Learning** activity.

This project helped us gain practical experience in web development, database management, authentication, version control and team collaboration.

---

## 💡 Conclusion

**BugTrack** provides a simple and organized platform for reporting, managing, assigning and tracking software bugs.

The project demonstrates how **Python, Django, HTML, CSS, Bootstrap and SQLite** can be combined to develop a practical software bug management system.

Through this project, we gained valuable practical knowledge of **web application development, database management, authentication, CRUD operations, Git/GitHub and teamwork**.

---

## 👨‍💻 Developer

### **Raval Shubham**

💻 Computer Engineering Student

🌐 GitHub: [@ravalshubham15](https://github.com/ravalshubham15)

---

<p align="center">

<strong>🐞 BUGTRACK</strong>

<br>

<strong>🚀 Report • Track • Manage • Resolve</strong>

<br><br>

<strong>Built with ❤️ using Python & Django</strong>

</p>

<p align="center">

⭐ <strong>If you find this project useful, consider giving it a star!</strong> ⭐

</p>