from flask import render_template
from flask_mail import Message
from app import app

def send_email(mail, email):
    recipients = [email]  # Replace with the recipient's email address

    subject = 'Test Email'
    html_body = render_template('email_template.html', name='John Doe')  # Replace with your HTML email template

    msg = Message(subject=subject, recipients=recipients, html=html_body)
    mail.send(msg)

    return 'Email sent successfully!'




import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to):
    instance = MIMEMultipart()
    instance["FROM"]=app.config["MAIL_DEFAULT_SENDER"]
    instance["TO"] = to 
    instance.attach(MIMEText(render_template("email_template.html"),"html"))
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(app.config["MAIL_DEFAULT_SENDER", app.config["MAIL_PASSWORD"]], )
            server.sendmail(app.config["MAIL_DEFAULT_SENDER"], to, instance.as_string())
