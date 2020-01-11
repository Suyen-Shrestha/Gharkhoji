# Gharkhoji
This is a kind of a property searching website developed in django as back-end and PostgreSQL as a database, where you can view property on sales and search using certain criterias and make inquries to the realtors of website.

## Project Setup

1. First of all create a virtual environment inside your project's directory and make sure that its activated(*refer to: **virtual environment in python** for details*).
2. Then install the required packages mentioned in the **"requirements.txt"** file(*included in the project's directory*) using command: `pip install -r requirements.txt`.
3. Then setup the database as mentioned below in **Database Configuration** step.
4. Then migrate to update your database using command: `python manage.py migrate`.
5. Finally, you can run the project using command: `python manage.py runserver`.



## virtual environment in python
*(Note: Strictly for Windows users, for others commands may vary slightly.)*

Browse to the directory where you want to setup your virtual environment then enter the command below:

`virtualenv <virtualenvironment_name>`

To activate the virtual environment:

`<virtualenvironment_name>\Scripts\activate`



## Database Configuration

Browse to the **"settings.py"** file in the directory: **_GharKhoji>GharKhoji>settings.py_** where you will find the following lines of code which is a setup for database.

Then enter your *'database name'*, *'password'* that you must have created in your PostgreSQL.

You can use the default *'USER': 'postgres'* and *'HOST': 'localhost'* for the PostgreSQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db_name>',
        'USER': 'postgres',
        'PASSWORD': '<db_password>',
        'HOST': 'localhost'
    }
}
```

