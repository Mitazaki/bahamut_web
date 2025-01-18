![DjBahamut](https://www.numbtongue.cc/images/bahamut_logo_splash1.png)

# DjBahamut

<p style="color: red;">⚠️ This project is still under development and not yet complete. Use at your own risk. ⚠️</p>

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

## Skills Demonstrated

- **Web Development**: Building a full-stack web application using Django.
- **Authentication**: Implementing OAuth2 authentication with Discord.
- **Database Management**: Integrating and managing a MySQL database.
- **Environment Management**: Using `.env` files for environment variable management.
- **Version Control**: Using Git for version control and collaboration.
- **Dependency Management**: Managing project dependencies with `pipenv`.
- **API Integration**: Working with external APIs (Discord API).
- **Problem Solving**: Debugging and solving issues that arise during development.
- **Team Collaboration**: Contributing to a project in a collaborative environment.
- **Linux Proficiency**: Navigating and managing a Linux-based server environment.
- **Django Framework**: Utilizing Django's features for rapid development and clean design.

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