import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from python"
body = "This is a test email from python"
sender = "prasaddharmadhikari265@gmail.com"
receiver = "prasad.dharmadhikari4669@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender
message["Subject"] = subject
message["To"] = sender
#message.set_content(body)

html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p> 
        </body>
    </html>
"""

message.add_alternative(html, subtype="html")
context  = ssl.create_default_context()
print("Sending email..............")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password) 
    server.sendmail(sender,receiver,message.as_string())
    
print("Successfully sent...............")