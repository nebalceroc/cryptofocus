class CypherIO:    
        def __init__(self):
            self.working_file=""
    
        def openFile(self, filename):
            f = open(filename, 'r+')
            self.working_file=f
            return f
    
        def createFile(self, filename):
            f = open(filename, 'w+')
            return f
    
        def getFileText(self):
            text = self.working_file.read()
            return text 