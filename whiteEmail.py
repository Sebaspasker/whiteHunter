import getpass
import os
import sys
import time
from utils.userSender import userSender

Exit = False
os.system('cls||clear')
print("Welcome to whiteEmail, ")

formatMessage = """
User: {User}
Password: {codPassword}
Port:  {Port}
Host: {Host}
To: {To}

Choose an option:
    1. User and Password introduction
    2. Port and host introduction
    3. Standard port and host (587, "smtp.gmail.com")
    4. To introduction
    5. All introduction (First select option 6)
    6. Txt message and excel information extraction (Excel file have to be closed in window to acceed)
    7. Send Message
    E. Exit"""

USER = userSender()

def addUserAndPassword():
    USER.addEmail(input("Introduce you're email: \n"))
    USER.addPassword(getpass.getpass(prompt="Introduce you're password: \n"))

def addPortAndHost():
    USER.addPort(input("Introduce port:\n"))
    USER.addHost(input("Introduce host:\n"))

def addUserList():
    Exit = False
    to = []
    while Exit == False:
        YorN = ""
        t = ""
        t = input("Introduce a email you want to send a message:")
        while YorN != 'Y' and YorN != 'y' and YorN != 'n' and YorN != 'N': 
            YorN = input("Sure you want to add {email} to to_list? Y/N".format(email = t))
        if YorN == 'Y' or YorN == 'y':
            to.append(t)
        YorN = ''
        while YorN != 'Y' and YorN != 'y' and YorN != 'n' and YorN != 'N': 
            YorN = input("Want to introduce another email?Y/N")
        if YorN == 'N' or YorN == 'n':
            Exit = True

    USER.addEmailList(to)

def addAllIntroduction():
    if USER.getDictionary() != {}:
        USER.addEmailList(USER.getDataEmails())
    else:
        print("ERROR:NO DICTIONARY, SELECT FIRST OPTION 6")
        time.sleep(1)

def excelAndTextSave(txtFile = None, exclFile = None):
    if txtFile == None:
        txtFile = input("Introduce txt file where message is:")
    if exclFile == None:
        exclFile = input("Introduce excel file:")
    USER.createMessages(txtFile, exclFile)
firstEntrance = True
Entrance = False
firstValue = False
Help_entrance = False
User_entrance = False
saveValueUser = False
Std_entrance = False
Password_entrance = False
saveValuePassword = False
if len(sys.argv) >= 2:
    Entrance == True

for arg in sys.argv:
    if firstEntrance:
        firstEntrance = False
    elif saveValueUser:
        saveValueUser = False
        User_first = arg
    elif saveValuePassword:
        saveValuePassword = False
        Password_first = arg
    elif arg == '--help' or arg == '-h':
        Help_entrance = True
    elif arg == '--user' or arg == '-u':
        User_entrance = True
        saveValueUser = True
    elif arg == '--standard' or arg == '-std':
        Std_entrance = True
    elif arg == '--password' or arg == '-p':
        Password_entrance = True
        saveValuePassword = True
    else:
        Entrance = False
        raise Exception("ERROR:INCORRECT ENTRANCE PARAMETER %s"%(arg))

if saveValueUser == True or saveValueMFK == True:
    raise Exception("ERROR:NOT ENOUGH VALUE INTRODUCTION")


if Help_entrance == False:
    while Exit == False:

        if User_entrance:
            USER.addEmail(User_first)
            User_entrance = False

        if Password_entrance:
            USER.addPassword(Password_first)
            Password_entrance = False

        print(formatMessage.format(User=USER.getEmail(), codPassword=USER.getCodifiedPassword(), Port=USER.getPort(), Host=USER.getHost(), To = USER.getToList()))
        
        if Std_entrance:
            option = '3'
            Std_entrance = False
        else:
            option = input()

        if option == '1':
            addUserAndPassword()
        elif option == '2':
            addPortAndHost()
        elif option == '3':
            USER.addPort(587)
            USER.addHost("smtp.gmail.com")
        elif option == '4':
            addUserList()
        elif option == '5':
            addAllIntroduction()
        elif option == '6':
            excelAndTextSave()
        elif option == '7':
            USER.sendMessages()
        elif option == 'E' or option == 'e':
            Exit = True

    
        os.system('cls||clear')
else:
    help = """
With this program you can create messages and send it by email with excel data values.
"-h" or "--help" --> Help command
"-u" or "--user" --> User introduction, need one value after introduction
"-p" or "--password" --> User introduction, need one value after introduction
"-std" or "--standard" --> Standard host and port introduction ("smtp.gmail.com", 587)
"""
    print(help)

print("Thanks for use our services")
