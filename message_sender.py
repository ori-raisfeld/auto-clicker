from email.message import EmailMessage
import ssl
import smtplib


def send_message(name, issue, email):
    if issue == "" or name == "":
        return "ERROR: name or issue are empty"
    else:
        message = f"From: {name}\n" \
                  f"Error: {issue}\n" \
                  f"gmail: {email}"

        mail = EmailMessage()
        mail['From'] = "whitepantherwebsite@gmail.com"
        mail['To'] = "whitepantherwebsite@gmail.com"
        mail['Subject'] = "Autoclicker"

        mail.set_content(message)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as gmail:
            gmail.login("whitepantherwebsite@gmail.com", "abcvqfpbzzjlbbsv")
            gmail.sendmail("whitepantherwebsite@gmail.com", "whitepantherwebsite@gmail.com", mail.as_string())
