from utils.pathCreator import path_creator
from utils.excelReader import excelReader

class messageCreator:
    var_dictionary = []
    email_list = []
    key_list = [] # No necesario
    message = ""
    message_list = []

    def readMessage(self, fileName): # Open and save txt file message
        file_path = path_creator(fileName)
        with open(file_path, "r") as txtFile:
            self.message = txtFile.read()

    def excelExtraction(self, fileName): # Open and save excel file values
        variableExtractor = excelReader()
        variableExtractor.read_excel_file(fileName)
        self.var_dictionary = variableExtractor.getVariablesList()

    def keyFinder(self): # No necesario
        listi = self.var_dictionary[0]
        for key in listi:
            if str.find(self.message, key) != -1:
                self.key_list.append(key)

    def saveEmail(self): # Save emails from values
        for variables in self.var_dictionary:
            self.email_list.append(variables["Email"])

    def messageFormat(self): # Create message formated list             MESSAGE FORMAT: {v[VAR_NAME]}
        for variables in self.var_dictionary:
            newMessage = self.message.format(v = variables)
            self.message_list.append(newMessage)
   
    def messagesCreation(self, messageFile, excelFile): # Create complete message with excel and text file
        self.readMessage(messageFile)
        self.excelExtraction(excelFile)
        self.saveEmail()
        self.messageFormat()
    
    def getStandardMessage(self):
        return self.message

    def getFormatedMessages(self):
        return self.message_list

    def getEmails(self):
        return self.email_list

    def getMessageDict(self): # Return message related to his email
        dict = {}
        i = 0
        for email in self.email_list:
            dict[email] = self.message_list[i]
            i = i+1

        return dict
