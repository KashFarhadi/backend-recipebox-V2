[This Project is on the V2-assessment branch here](https://github.com/KashFarhadi/backend-recipebox-V2/tree/V2-assessment)


# backend-recipebox-V2
Here we add editing and favorites recipes to our previous recipebox assessment. For this project we used an external codebase to implement these new features to replicate the experience of working on code you didn't build. Consulting the creator, fundamentally changing the code and refactoring were not allowed.


[Original Codebase by Chris Joy](https://github.com/cmjoy136/recipebox)

[Original Codebase at start of project](https://github.com/KashFarhadi/recipebox)


### Completed by
Kash Farhadi

## Running the Application

Fork, Clone, Navigate to directory
Create and start a a virtual environment

for pipenv:
`pipenv -install`
`pipenv shell`

`python manage.py makemigrations {foldername}` 
(where foldername is the top level folder for this project)

`python manage.py migrate`

Create an admin account (superuser) if you would like to test admin features and access the admin page. Easily create users and objects from the built in django visual interface

`python manage.py createsuperuser`

Finally start the django server using: 
`python manage.py runserver`

Access the homepage at 
`http://127.0.0.1:8000/` 
`http://localhost:8000/`

Admin page
`http://127.0.0.1:8000/admin` 
`http://localhost:8000/admin`


##### Built using Python 3.8 and the latest version of Django (2.1.2 as of this writing)
