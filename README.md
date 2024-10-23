# Flask Starter

## Project Structure

```
flask-starter/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── config.py
│   └── extensions.py
├── instance/
│   └── config.py
├── tests/
│   └── test_basic.py
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

- **Project Structure**: Organizes the project into directories for the application, instance configuration, and tests.
- **Flask Application**: Sets up the Flask application with configuration management, extensions, and blueprints.
- **Configuration**: Uses environment variables and instance-specific configuration for flexibility.
- **Extensions**: Initializes common Flask extensions like SQLAlchemy and Flask-Migrate.
- **Routes**: Defines a simple route that returns a JSON response.
- **Tests**: Includes a basic test case to verify the index route.
- **Environment Variables**: Uses a .env file to manage secret keys and database URLs.
- **Requirements**: Lists the required Python packages.
- **Run Script**: Provides a script to run the Flask application.

## Running the Application

### venv

Create a virtual environment and activate it:

```sh
cd flask-starter
python3 -m venv venv
```

activation:

**Mac & Linux**

```sh
source venv/bin/activate
```

**Windows**

To activate your venv on Windows, you need to run a script that gets installed by venv.

Command Prompt:

```sh
venv\Scripts\activate
```

PowerShell:

```sh
venv\Scripts\Activate.ps1
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run the Application

```
python run.py
```

### Access the Application

Open your web browser and navigate to http://localhost:5000.
