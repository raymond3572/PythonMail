import smtplib
import ssl
from email.message import EmailMessage

subject = "Social Media Latest Post Notification"
body = "Hi <br><br>Check out our social media pages to see our latest posts.<br><br>Please like, share, or copy and paste our content to your LinkedIn profile status update.<br>Click on the links below to visit our social media pages: <br><br>https://www.facebook.com/RahnConsolidated <br> https://www.linkedin.com/company/rahn-consolidated-itconsulting-businessanalytics-bireporting-itrecruitment-financialcrimeproducts <br>https://www.instagram.com/rahnconsolidated/ <br><br> Kind regards"
sender_email = "rahnconsolidated@gmail.com"
receiver_email = "raymondvdb@rahn.co.za"
password = "Sabba2020"

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Mail!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")