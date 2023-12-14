import smtplib

def send_email(subject, body, to_email):
    # Email configuration
    sender_email = 'contact.od.terminal@gmail.com'
    sender_password = 'iwbl hrck qnad thmo'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create email headers
    headers = f"Subject: {subject}\nFrom: {sender_email}\nTo: {to_email}\n"

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login to the email account
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, to_email, headers + '\n' + body)

    # Quit the server
    server.quit()

# Example usage
'''subject = 'Test Email'
body = 'This is a test email sent from Python.'
to_email = 'sakshamraghav57@gmail.com'

send_email(subject, body, to_email)
'''