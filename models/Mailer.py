import settings
class Mailer:
    def __init__(self,subject:str,body:str):   
        self.__mail=settings.EMAIL
        self.__subject=subject
        self.__body=body
        self.__receptor=None

    @property
    def subject(self):
        return self.__subject
    
    
    @property
    def body(self):
        return self.__body
    
    @subject.setter
    def subject(self,s):
        if not s: raise Exception('Subject cannot be empty.')
        self.__subject = s

    @body.setter
    def body(self,b):
        if not b: raise Exception('Body cannot be empty.')
        self.__body = b

    def __setup(self) -> dict:
        from email.message import EmailMessage
        import ssl
        email_message=EmailMessage()
        email_message['From']=self.__mail
        email_message['To']=self.__receptor
        email_message['Subject']=self.__subject
        email_message.set_content(self.__body)
        return {
            'EMAIL_MESSAGE' : email_message,    
            'CONTEXT' : ssl.create_default_context(),
            'HOST' : settings.HOST,
            'PORT' : settings.PORT,
            'EMAIL' : self.__mail,
            'PASSWORD' : settings.PASSWORD
        }

    def __connection(self):
        ## Establishes the connection to the mail server.
        import smtplib
        settings = self.__setup()
        with smtplib.SMTP_SSL(settings['HOST'],settings['PORT'],context=settings['CONTEXT']) as smtp:
            smtp.login(settings['EMAIL'],settings['PASSWORD'])
            smtp.sendmail(settings['EMAIL'],self.__receptor,settings['EMAIL_MESSAGE'].as_string())

    def send_email(self,email_receptor:str) -> bool:
        """Send an email to a user.
        Args:
            email_receptor (str): Recipient user email. 
        """
        self.__receptor=email_receptor
        self.__connection()

