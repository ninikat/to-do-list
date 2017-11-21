class ToDo():
    def __init__(self, title):
        self.title = title
        self.tasks = []
        self.remove = 0
        
    def addTask(self,task):
        self.tasks.append(task)
    
    def viewTasks(self):
        print self.tasks
    
    def removeTask(self,item):
        for index in range(0,len(self.tasks)):
            if self.tasks[index]==item:
                self.remove = index
        del self.tasks[self.remove]
            
#i create this just so there is one. i can put it in the function? 
list=ToDo('Monday')

            
def toDoTasks():
    while True:
        userInput = raw_input("Enter 'add' to add a task, 'view' to view all tasks or 'delete' to remove task or 'q' to exit:  ")

        if userInput.lower() == 'add':
            userTask = raw_input("Enter your task: ")
            list.addTask(userTask)
            #print(userTitle)

        elif userInput.lower() == 'view':
            list.viewTasks()

        elif userInput.lower() == 'delete':
            userToDelete = raw_input("Enter the task you want to delete: ")
            list.removeTask(userToDelete)

        elif userInput.lower() == "q":
            break
            
toDoTasks()



#need to give options, like 1 to add, 2 to remove(it will ask you which to remove), 3 to view