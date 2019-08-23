import xlrd
from utils.pathCreator import path_creator

class excelReader:
    variables = []
    
    def read_excel_file(self, fileNameAndDir):
        path = path_creator(fileNameAndDir) # Create excel file Path
        document = xlrd.open_workbook(path)
        book = document.sheet_by_index(0)   # Extract first book from excel file
        firstEntrance = True
        titles = []
        process = 0
        variablei = []
        dict_var = {}
        for i in range(book.nrows):
            for j in range(book.ncols):
                if firstEntrance:   # Save title value in list and dictionary
                    titles.append(book.cell_value(i, j))
                else:              # Add values from variable to list
                     dict_var[titles[process]] = book.cell_value(i, j)
                process = process+1
            if firstEntrance == False:
                self.variables.append(dict_var)    # Add list to variables list  
                dict_var = {}
            process = 0
            firstEntrance = False

    def getVariablesList(self):
        return self.variables


            
