import smtplib
import time
from utils.messageCreator import messageCreator
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class userSender:
    user_email = ""
    user_password = ""
    host = ""
    port = 0
    to_list = []
    messDictionary = {}
    SubjectFromMessage = ""
    mc = messageCreator()

    def defineUser(self, email, password, host, port, email_list = None, Subject = None):
        self.user_email = email
        self.user_password = password
        self.host = host
        self.port = port
        if email_list != None:
            self.to_list = email_list
        if Subject != None:
            self.SubjectFromMessage = Subject
        
    def sendMessages(self):        
        if self.user_email != "" and self.user_password != "" and self.host != "": # Filter:Empty str necessary values
            if len(self.messDictionary) != 0:   # Filter:Case no message to send
                if len(self.to_list) == 0: # Filter:Case no emails to send
                    YorN = ''
                    while YorN != 'y' and YorN != 'n' and YorN != 'Y' and YorN != 'N':
                        YorN = input("Send message to all emails? Y/N \n")

                    if YorN == 'y' or YorN == 'Y':
                        self.to_list = self.mc.getEmails() # Save all emails in to send list
                    else:
                        raise Exception("Can't send message with no emails")
            
                for sendUser in self.to_list:
                    email = sendUser
                    msg = self.messDictionary[sendUser]
                    try:
                        email_conn = smtplib.SMTP(self.host, self.port)
                        email_conn.ehlo()
                        email_conn.starttls()
                        email_conn.login(self.user_email, self.user_password)
                        YorN = ''
                        EorR = ''
                        Exit = False
                        if self.SubjectFromMessage == "": # Subject introduction, exit option
                            while YorN != 'y' and YorN != 'Y' and EorR != 'E' and EorR != 'e':
                                self.SubjectFromMessage = input("Write a subject for the message \n")
                                YorN = input("Sure you want to send this subject? Y/N")
                                if YorN == 'N' or YorN == 'n':
                                    EorR = input("Want rewrite subject or exit? R/E")
                            if EorR == 'E':
                                Exit = True
                                email_conn.quit()
                                break

                        if Exit == False: # Send email
                            the_msg = MIMEMultipart("alternative")
                            the_msg["Subject"] = self.SubjectFromMessage
                            the_msg["From"] = self.user_email
                            the_msg["To"] = email
                            part_1 = MIMEText(msg, 'plain')
                            the_msg.attach(part_1)
                            email_conn.sendmail(self.user_email, [email], the_msg.as_string())
                            email_conn.quit()

                    except smtplib.SMTPException:
                        print("Error sending message")
                    if Exit:
                        print("Exit operation realized with success \n")
                        break

            else:
                print("Can't send email with no message data")
                time.sleep(1)
        else:
            if self.user_email == "":
                print("ERROR:NO USER INTRODUCTION")
            if self.user_password == "":
                print("ERROR:NO PASSWORD INTRODUCTION")
            if self.host == "":
                print("ERROR:NO HOST INTRODUCTION")
            time.sleep(1)

    def addEmail(self, email):
        self.user_email = email

    def addPassword(self, password):
        self.user_password = password

    def addHost(self, host):
        self.host = host
      
    def addPort(self, port):
        self.port = port

    def addEmailList(self, to_list):
        self.to_list = to_list

    def getEmail(self):
        return self.user_email

    def getPassword(self):
        return self.user_password

    def getCodifiedPassword(self):
        i = 0
        codpas = ""
        while i < len(self.user_password):
            codpas = codpas + '*'
            i = i + 1

        return codpas

    def getHost(self):
        return self.host

    def getPort(self):
        return self.port

    def getToList(self):
        return self.to_list

    def getDictionary(self):
        return self.messDictionary

    def getDataEmails(self):
        return self.mc.getEmails() # Save all emails in to send list

    def createMessages(self, txtFile, excFile):
        self.mc.messagesCreation(txtFile, excFile)
        self.messDictionary  = self.mc.getMessageDict()

