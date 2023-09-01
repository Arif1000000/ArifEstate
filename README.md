# ArifEstate

ArifEstate is a real estate web application built using Django and Bootstrap for the frontend.

## Features

- List and display properties for sale
- Admin interface for managing properties
- Responsive design using Bootstrap
- ...

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/ArifEstate.git
Navigate to the project directory:

bash
Copy code
cd ArifEstate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database settings in settings.py:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Run migrations:

bash
Copy code
python manage.py migrate
Create a superuser account:

bash
Copy code
python manage.py createsuperuser
Start the development server:

bash
Copy code
python manage.py runserver
Access the admin interface at http://127.0.0.1:8000/admin/ and log in with the superuser account.

Usage
Access the property listing page at http://127.0.0.1:8000/
Use the admin interface to manage properties and add new entries.
Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
This project was created as part of ALX portfolio project.

Contact
For any questions or inquiries, please contact Me @ muhammed.arif11@gmail.com
