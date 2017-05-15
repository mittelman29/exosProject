# exosProject

Installation instructions

1. Create a directory called exos for the project

2. cd to directory and run:

    virtualenv -p /usr/bin/python2.7 exos
    
3. Source the virtualenv

    source exos/bin/activate

4. Install django

    pip install Django==1.9.13
    
5. Clone exosProj directory from this repository into the exos directory

6. Edit the exos/lib/python2.7/site-packages/django/contrib/auth/models.py file

    A. Add the following import at line 15
    
            import random
    
    B. Add the following at line 373:
    
            birthday = models.DateField(blank=True, null=True)
            random_num = models.PositiveIntegerField(default=random.randint(1,101), validators=[validators.MinValueValidator(1),         validators.MaxValueValidator(100)])
        
    The entire User class should appear as follows:
    
        class User(AbstractUser):
        """
        Users within the Django authentication system are represented by this
        model.

        Username, password and email are required. Other fields are optional.
        """
        birthday = models.DateField(blank=True, null=True)
        random_num = models.PositiveIntegerField(default=random.randint(1,101), validators=[validators.MinValueValidator(1),     validators.MaxValueValidator(100)])

        class Meta(AbstractUser.Meta):
            swappable = 'AUTH_USER_MODEL'
            
7. The migration has already been run so the fields are in the database.

8. Start the django development server
    
        python manage.py runserver
    
9. Navigate to http://127.0.0.1/users/list to start! Good luck!
