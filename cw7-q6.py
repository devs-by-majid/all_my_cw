
class Logger:
    def __init__(self,name):
        self.file_name=open(name,"w")
    
    def write(self):
       self.file_name.write("hello World")
       
    def __del__(self):
        self.file_name.close()
        print("log file closed")
        

logger=Logger("file.txt")               