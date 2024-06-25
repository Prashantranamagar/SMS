# School Management System

## Overview

Web Application for managing student.

## Features



## Prerequisites

- Python 
- Django

## Installation with virtualenv

1. Clone the repository:
  
    ```
    git clone https://github.com/Prashantranamagar/SMS.git
    ```

2. Checkout to the project directory:

    ```  
    cd SMS
    ```


3. Create a virtual environment:

    ```  
    python -m venv venv
    ```

4. Activate the virtual environment:

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

- On Windows:

    ```
    venv\Scripts\activate
    ```

5. Install the app's dependencies:

    ```
    pip install -r requirements.txt 
    ```  

6. Apply database migrations:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Start the development server:

    ```
    python manage.py runserver
    ```



## Installation with Docker Compose

### Prerequisites

- Docker
- Docker Compose

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Prashantranamagar/SMS.git
    cd SMS
    ```

2. **Build and run the Docker containers:**

    ```bash
    docker compose up --build
    ```

   The application will be accessible at `http://localhost:8000`.