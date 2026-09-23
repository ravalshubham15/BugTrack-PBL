# 🐞 BugTrack – Software Bug Reporting & Tracking System

A simple web-based Software Bug Reporting and Tracking System developed as a Project Based Learning (PBL) project.

## 📌 About The Project

BugTrack is a web-based Software Bug Reporting and Tracking System developed using Python and Django.

It helps users report, manage, assign, and track software bugs from a centralized platform.

The system allows users to:

- Register and Login
- Report new bugs
- View bug details
- Edit bugs
- Delete bugs
- Set bug priority
- Assign bugs to developers
- Track bug status
- Search bugs
- Filter bugs
- View bug statistics on the dashboard

## 🎯 Objectives

- Provide a simple platform for reporting software bugs.
- Maintain all bug information in one place.
- Make bug management easier for developers.
- Assign bugs to responsible developers.
- Track the progress of reported bugs.
- Provide search and filtering functionality.
- Display bug statistics through a dashboard.
- Reduce manual bug tracking work.

## ✨ Features

### 👤 User Authentication

- User Registration
- User Login
- User Logout
- Django-based authentication

### 🐞 Bug Management

- Report a new bug
- View all bugs
- View complete bug details
- Edit existing bugs
- Delete bugs

### 🎯 Priority Management

Each bug can have one of the following priorities:

- Low
- Medium
- High
- Critical

### 🔄 Status Tracking

Each bug can have one of the following statuses:

- Open
- In Progress
- Resolved

Bug workflow:

Open → In Progress → Resolved

### 👨‍💻 Developer Assignment

Bugs can be assigned to developers for further work and tracking.

### 🔎 Search & Filter

Users can:

- Search bugs
- Filter bugs by status
- Filter bugs by priority

### 📊 Dashboard

The dashboard displays:

- Total Bugs
- Open Bugs
- In Progress Bugs
- Resolved Bugs

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Django | Backend Web Framework |
| SQLite | Database |
| HTML5 | Web Page Structure |
| CSS3 | Styling |
| Bootstrap | User Interface |
| JavaScript | Client-side Functionality |
| VS Code | Development Environment |
| Git | Version Control |
| GitHub | Source Code Management |

## 🏗️ System Architecture

```text
User
  ↓
Web Interface
  ↓
Django Application
  ↓
Views / Forms
  ↓
Models
  ↓
SQLite Database

## 🔄 System Workflow

The working process of BugTrack is as follows:

1. User opens the BugTrack website.
2. User registers a new account or logs in.
3. After login, the user is redirected to the dashboard.
4. User reports a new bug by entering:
   - Bug title
   - Bug description
   - Priority
   - Assigned developer
5. The bug is saved in the SQLite database.
6. The reported bug appears in the All Bugs page.
7. Users can search and filter bugs based on:
   - Bug title
   - Status
   - Priority
8. The developer updates the bug status:
   - Open
   - In Progress
   - Resolved
9. Users can view, edit, or delete bug details.
10. The dashboard displays the total number of bugs according to their status.

### Bug Status Flow

Open → In Progress → Resolved

---

## 🗄️ Database

BugTrack uses **SQLite** as its database.

The main database table is:

### Bug Table

| Field Name | Description |
|---|---|
| id | Unique ID of the bug |
| title | Title of the bug |
| description | Detailed explanation of the bug |
| priority | Bug priority such as Low, Medium, High, or Critical |
| status | Current status of the bug |
| reported_by | User who reported the bug |
| assigned_to | Developer assigned to fix the bug |
| created_at | Date and time when the bug was created |
| updated_at | Date and time when the bug was last updated |

### Priority Types

- Low
- Medium
- High
- Critical

### Status Types

- Open
- In Progress
- Resolved

The database stores all bug information and helps the application manage bug records efficiently.

---

## 📁 Project Structure

```text
BugTrack_PBL/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
│
├── BugTrack/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── bugapp/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── bug_list.html
│   ├── bug_form.html
│   ├── bug_detail.html
│   └── bug_confirm_delete.html
│
└── static/
    └── css/
        └── style.css