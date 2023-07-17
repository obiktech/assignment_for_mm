import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'jwt_secret_key')
    MAIL_SERVER = 'your_mail_server'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_mail_username'
    MAIL_PASSWORD = 'your_mail_password'
    MAIL_DEFAULT_SENDER = 'your_default_sender_email'
