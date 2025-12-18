import psycopg2
from psycopg2 import Error

class User:
    def RegisterUser(self, username, password, email):
        try:
            # Replace with your actual database connection string
            con = psycopg2.connect(database="your_actual_db", user="your_actual_user", password="your_actual_password", host="localhost", port="5432")
            cursor = con.cursor()
            sql = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, email))
            con.commit()
            print(f"User registered successfully with username {username} and password {password}.")
        except Error as e:
            print(f"Database error: {e}")
        finally:
            if 'con' in locals() and con:
                cursor.close()
                con.close()

import logging
class Logger:
    def LogMessage(self, message):
        logging.basicConfig(level=logging.ERROR, filename="app.log", filemode="a",
                            format="%(asctime)s - %(levelname)s - %(message)s")
        logging.error(message)
        print(f"Logged message: {message}")

import smtplib
import ssl
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email:
    def SendEmail(self, to_email, message_content, subject="User Registered"):
        try:
            with open('credentials.json') as f:
                data = json.load(f)

            smtp_server = "smtp.gmail.com"
            port = 465
            sender_email = data["fromuser"]
            password = data["password"]

            context = ssl.create_default_context()
            message = MIMEMultipart("alternative")

            message["From"] = sender_email
            message["To"] = to_email
            message["Subject"] = subject
            message_content = f"Hello,<br><b>Message from Laasya:</b><br>{message_content}<br>Regards,<br>Team Laasya"
            part = MIMEText(message_content, "html")
            message.attach(part)

            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, to_email, message.as_string())
            print(f"Email sent to {to_email} successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

class Registration:
    def RegisterUser(self, username, password, email):
        try:
            User().RegisterUser(username, password, email)
            Email().SendEmail(email, f"Welcome {username}, you have been registered successfully.")
        except Exception as e:
            Logger().LogMessage(str(e))
            print("An error occurred during registration.")

r = Registration()
r.RegisterUser("laasya", "laasya123", "bijjalalaasyasri17@gmail.com")