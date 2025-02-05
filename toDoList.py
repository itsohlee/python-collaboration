num = int(input("How many tasks would you like to add: "))
tasks = []
using = True
for i in range (0,num,1):
    task = input("Task " + str(i+1)+ ": ")
    tasks.append(task)
    print(tasks)
def endPro():
    if(using==False):
        return 0
def completeTask():
    user = str(input("Have you completed any tasks?: "))
    if(user=="Y" or user=="y"):
        for i in range(len(tasks)):
            inp = int(input("Which tasks have you completed? Task: "))
            inp2 = str(input("Are you done? Y for Yes, N for no."))
            tasks[inp-1] = tasks[inp-1] + " - DONE!"
            print(tasks) 
            if((inp2=="Y") or (inp2 =="y")):
                endPro()
    elif(user=="N" or user=="N"):
        print("Way to go!")
        print(tasks)
        return 0
    else:
        return 0    
    
def removeTask():
    user = input("Would you like to remove a task? Press Y for Yes, N for no. ")
    if(user=="Y" or user=="y"):
        t = int(input("Which task would you like to remove? Task: "))
        tasks.pop(t-1)
        print(tasks)
        completeTask()
    elif(user=="N" or user=="n"):
        print("Ok, here are your tasks!")
        print(tasks)
        completeTask()
    else:
        print("Wrong input please start over.")

removeTask()

