# Jaza Savings App

## Overview

Jaza Savings App is a Django-based application designed to help users manage their savings. This README provides instructions for setting up the project for local development and deploying it to Heroku using JawsDB as the MySQL database.

## Local Development Setup

### Prerequisites

- Python 3.9 or later
- MySQL (or a compatible MySQL database)

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/micro_savings_app.git
    cd micro_savings_app
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a Local `.env` File:**

    Create a file named `.env` in the project root directory with the following content:

    ```env
    DEBUG=True
    DATABASE_URL=mysql://username:password@localhost:3306/dbname
    ```

    Replace `username`, `password`, `localhost`, and `dbname` with your local MySQL database credentials.

5. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

    Access the app at `http://127.0.0.1:8000/`.

## Deployment to Heroku

### Prerequisites

- Heroku CLI installed
- A Heroku account

### Setup Instructions

1. **Login to Heroku:**

    ```bash
    heroku login
    ```

2. **Create a New Heroku App:**

    ```bash
    heroku create your-heroku-app-name
    ```

    Replace `your-heroku-app-name` with your desired Heroku app name.

3. **Add JawsDB MySQL Add-on:**

    ```bash
    heroku addons:create jawsdb:kitefin
    ```

4. **Set Environment Variables:**

    ```bash
    heroku config:set DJANGO_SETTINGS_MODULE=config.settings.heroku
    ```

5. **Add Heroku Remote (if not already added):**

    ```bash
    git remote add heroku https://git.heroku.com/your-heroku-app-name.git
    ```

6. **Deploy Code to Heroku:**

    ```bash
    git add .
    git commit -m "Prepare for deployment"
    git push heroku main
    ```

7. **Run Migrations on Heroku:**

    ```bash
    heroku run python manage.py migrate
    ```

8. **Create a Superuser on Heroku (optional):**

    ```bash
    heroku run python manage.py createsuperuser
    ```

9. **Open the App in the Browser:**

    ```bash
    heroku open
    ```

## Additional Notes

- **Database Configuration:**
  - Ensure that the `DATABASE_URL` in your `.env` file and Heroku settings are properly configured.

- **Environment Variables:**
  - You may need to set additional environment variables depending on your project's requirements.

- **Debugging:**
  - Use Heroku logs to debug any issues:
    ```bash
    heroku logs --tail
    ```

Feel free to adjust the instructions as needed for your specific setup and environment.
