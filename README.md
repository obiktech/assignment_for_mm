# assignment_for_mm


How to set up 
1. pip install requirements.txt 
2. open and python shell and run these command

    from app import app
    from app.models import User
    from app import db 
    with app.app_context():
        db.create_all()

then finally run using python run.py



debug mode can switch using .env file modification , not the code 


employee can register using  site-address/employee/register
by sending data in format like  {"email": email, "password": password} 


and employee can login using  site-address/employee/login
by sending data in format like  {"email": email, "password": password} and get a web token 