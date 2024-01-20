
# Django Celery Project
## Introduction: This repository contains the source code for Celery Project, a Django project utilizing Celery for asynchronous tasks. This README provides instructions for setting up and running the project locally.

### Prerequisites:
  - Python 3.x
  - pippython-dotenv
  - SQLite3SQL (or other supported database
  - Redis (optional, for Celery result backend)
  - 
### Installation:
  - Clone the repository
  - Create and activate a virtual environment
  - Install dependencies
  - Configure Database
     - Update settings.py with your database credentials.
     - Run database migrations:
  - Configure Celery
      - Update celery.py with your broker and backend settings.
      - Start the Celery workers:
        ```diff
          - celery -A celery_project worker -l info
  - Run the Django server
    
### Additional Resources:

Django: https://docs.djangoproject.com/en/5.0/
Celery: https://docs.celeryq.dev/
