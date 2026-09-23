# BugTrack – GTU PBL

Simple Django web application for reporting and tracking software bugs.

## Technology
- Python
- Django
- SQLite
- HTML/CSS/Bootstrap

## Features
- User registration and login
- Dashboard
- Create, view, edit and delete bugs
- Priority: Low, Medium, High, Critical
- Status: Open, In Progress, Resolved
- Assign bug to a developer/user
- Search and filter
- Django admin

## Setup on Windows

Open PowerShell in this folder:

```powershell
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Open:
http://127.0.0.1:8000/

Admin:
http://127.0.0.1:8000/admin/

## Suggested PBL team split
1. Frontend/UI
2. Django backend
3. Database & authentication
4. Bug management
5. Dashboard/testing/integration
