from email.message import EmailMessage
import ssl
import smtplib


def send_message(name, issue, email):
    if issue == "" or name == "":
        return False
    else:
        # account and entry are both important data, so please use your own
        account = ""
        entry = ""
        message = f"From: {name}\n" \
                  f"Error: {issue}\n" \
                  f"gmail: {email}"

        mail = EmailMessage()
        mail['From'] = account
        mail['To'] = account
        mail['Subject'] = "Autoclicker"

        mail.set_content(message)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as gmail:
            gmail.login(account, entry)
            gmail.sendmail(account, account, mail.as_string())
        return True