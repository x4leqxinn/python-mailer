from models.Mailer import Mailer

subject=input('Enter a subject: ')
body=input('Enter a body: ')
receptor=input('Enter a destination email: ')

## Send email
mailer = Mailer(subject=subject,body=body)
mailer.send_email(email_receptor=receptor)

