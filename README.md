# DjBahamut

DjBahamut is a Django project that integrates Discord OAuth2 for user authentication. This is meant as a base for development of a website that can admin a discord bot using those credentials and using discord oath as your authentication platform.

## Features

- User authentication via Discord OAuth2
- MySQL database integration
- Environment variable management with `.env` file

## Requirements

- Python 3.8+
- Django
- MySQL
- `pipenv` for managing dependencies

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/djbahamut.git
cd djbahamut
```

### 6. Run Migrations

Apply the migrations to set up your database schema.

### 7. Run the Development Server

Start the Django development server.

```sh
python3 manage.py runserver
```

### 8. Access the Application

Open your web browser and navigate to http://127.0.0.1:8000.

### Usage
Navigate to /login/ to authenticate via Discord.
After successful authentication, you will be redirected to the home page.
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

### License
This project is licensed under the MIT License.