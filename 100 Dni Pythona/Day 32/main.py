import smtplib

my_email = 'mlukasik277@gmail.com'
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()