# MarketIO

## Description
MarketIO is an e-commerce product comparison platform that scrapes products in real-time across 5 different platforms - AliExpress, Amazon, EzBuy, Lazada and Qoo10.

## Features
1. User authentication via the convential username and password, or via social platforms like Google
2. Real-time product comparison across 5 different e-commerce platforms
3. Watchlist for users to track specific products

## Installation
1. Clone this project using git clone: ````git clone https://github.com/marvine9830/MarketIO````
2. Add a .env file in the root folder of this project with the following variables:
````
DJANGO_SECRET_KEY = "<any randomly generated string with 64 alphanumeric characters>"
DJANGO_JWT_SIGNING_KEY = "<any randomly generated string with 64 alphanumeric characters>"
DJANGO_JWT_ALGORITHM = HS512
DJANGO_JWT_LIFETIME = 14
DJANGO_BACKEND_URL = http://127.0.0.1:8000    ## change this to your backend production url upon deployment
DJANGO_DEBUG = True
GOOGLE_CLIENT_ID = "<your google project's client id>"
GOOGLE_CLIENT_SECRET = "<your google project's client secret>"
NEXTAUTH_URL = http://127.0.0.1:3000  ## change this to your frontend production url upon deployment
NEXTAUTH_SECRET = "<any randomly generated string with 64 alphanumeric characters>"
NEXTAUTH_BACKEND_URL = http://127.0.0.1:8000    ## should be same as DJANGO_BACKEND_URL
NEXTAUTH_PUBLIC_BACKEND_URL = http://127.0.0.1:8000    ## should be same as DJANGO_BACKEND_URL
````
3. Install dependencies for both frontend and backend
    - Front-end
        - Navigate to the frontend directory: ````cd frontend````
        - Install all frontend dependencies: ````npm install````
    - Back-end
        - Navigate to the backend directory: ````cd backend````
        - Generate a python virtual environment: ````python -m venv venv````
        - Activate the python virtual environment: ````venv/Scripts/activate````
        - Install all backend dependencies: ````pip install -r packages.txt````
        - Navigate to the project directory: ````cd project````
        - Generate project migration files: ````python manage.py makemigrations analytics products profiles scrapers search watchlists````
        - Migrate the project: ````python manage.py migrate````
        - Create a new super user: ````python manage.py createsuperuser````, follow the prompts provided

## Running the Project
1. Build the static files for the Next.js frontend
    - Navigate to the frontend directory: ````cd frontend````
    - Generate an optimised production build: ````npm run build````
2. Run the Next.js frontend: ````npm run start````
3. Run the Django backend
    - Navigate to the Django project directory: ````cd backend/project````
    - Run the Django server: ````python manage.py runserver````
4. Open the project in your browser (if you did not change the urls in the environment variables)
    - Frontend: ````127.0.0.1:3000````
    - Backend: ````127.0.0.1:8000````
