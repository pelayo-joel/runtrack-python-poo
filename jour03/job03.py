class Tache:
    def __init__(self, title:str, desc:str, status:bool=False):
        self.__title = title
        self.__description = desc
        self.__status = "Done"

        if status:
            self.__status = "To do"



    '''Public methods'''
    def PrintTask(self):
        print(f"    - Task: {self.__title}")
        print(f"    - Desc: {self.__description}")
        print(f"    - Status: {self.__status}\n")


    def GetTitle(self):
        return self.__title
    

    def GetStatus(self):
        return self.__status


    def ChangeStatus(self):
        self.__status = "Done"


class ListeDeTache:
    def __init__(self):
        self.__taskList = []

    

    '''Public methods'''
    def AddTask(self, newTask:Tache):
        self.__taskList.append(newTask)


    def DelTask(self, taskToDel:str):
        for task in self.__taskList:

            if task.GetTitle() == taskToDel:
                self.__taskList.remove(task)
                break

        else:
            print(f"Task '{taskToDel}' not present in the list")


    def TaskDone(self, taskDone:str):
        for task in self.__taskList:

            if task.GetTitle() == taskDone:
                task.ChangeStatus()
                break

        else:
            print(f"Task '{taskDone}' not present in the list")


    def TaskList(self):
        print(f"To-Do list (all):")
        for i in range(len(self.__taskList)):
            print(f"- task {i+1}")
            self.__taskList[i].PrintTask()


    def FilterList(self):
        print(f"To-Do list (to-do only):")
        i = 1
        for task in self.__taskList:
            if task.GetStatus() != "Done":
                print(f"- task {i}")
                task.PrintTask()

            i += 1
            

#Demonstrates both 'Tache' and 'ListeDeTache' class
task1 = Tache("Nettoyer", "Nettoyer mon ...", True)
task2 = Tache("Travailler", "Travailler sur ...", True)
task3 = Tache("Manger", "Manger ...", True)

taskList = ListeDeTache()
taskList.AddTask(task1)
taskList.AddTask(task2)
taskList.AddTask(task3)


taskList.TaskList()
taskList.FilterList()
print('\n')

taskList.DelTask("Nettoyer")
taskList.TaskList()
print('\n')

taskList.TaskDone("Travailler")
taskList.FilterList()