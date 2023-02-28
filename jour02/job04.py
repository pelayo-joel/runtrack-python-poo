class Student:
    def __init__(self, firstName:str, name:str, id:int):
        self.__firstName, self.__name = firstName, name
        self.__studentId, self.__studentPoint = id, 0
        self.__level = self.__StudentEval()

    '''Public methods'''
    def AddCredits(self, points:int):
        self.__studentPoint += points

    def StudentInfo(self):
        return self.__level
    
    def GetPoints(self):
        return self.__studentPoint
    
    def StudentInfo(self):
        print(f"ID: {self.__studentId}")
        print(f"First Name: {self.__firstName}")
        print(f"Name: {self.__name}")
        print(f"Level: {self.__level}\n")



    '''Private methods'''
    def __StudentEval(self):
        if self.__studentPoint >= 90:
            return "Excellent"
        
        elif self.__studentPoint >= 80:
            return "Tres bien"
        
        elif self.__studentPoint >= 70:
            return "Bien"
        
        elif self.__studentPoint >= 60:
            return "Passable"
        
        elif self.__studentPoint < 60:
            return "Insuffisant"
        

#Demonstrates the 'Student' class
JohnDoe = Student("Doe", "John", 145)

JohnDoe.AddCredits(30)

print(f"Le nombre de credits de John Doe est de {JohnDoe.GetPoints()} points\n")
JohnDoe.StudentInfo()