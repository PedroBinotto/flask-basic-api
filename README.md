# FlaskBasicAPI

[![Build status](https://github.com/PedroBinotto/flaskbasicapi/actions/workflows/tests.yml/badge.svg)](https://github.com/PedroBinotto/flaskbasicapi/actions/)

Bootstrapping tool (hack) for simple Flask backend API development

### Configuration

Copy the contents of `.env.example` to `{YOUR_PROJECT_ROOT}/.env` and set the values for the configuration variables

### Usage

Managing database migrations:

```bash
flask db downgrade
# or
flask db upgrade
```

Run the application with the Flask development web server:

```bash
flask run
```

The application runs on `localhost:5000`. You can access the API documentation
at `http://localhost:5000/docs`.

- Move FlaskBasicAPI to another port:
    - Start the server with the command `flask run --port=4000`.

