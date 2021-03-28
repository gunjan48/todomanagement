def todolist():

    print("hello, here is your to-do list menu!")
    print("press 1: to create a task")
    print("press 2: to delete a task")
    print("press 3: to view todo list")
    print("press 4: to exit")
    press=input("enter your choice: ")

    if press=="1": 
        f = open("to-do.txt", "a")
        task=input("enter a task to do: ")
        f.write(task +"\n")
        f.close()
    elif press=="2":
        f=open("to-do.txt",'r+')
        todos=f.read().split('\n')
        for line in todos:
            print(line)
        f.close()
        f=open('to-do.txt','w')
        deltask=int(input("enter the line number of task in list: "))
        todos.pop(deltask-1)  
        for i in range(0,len(todos)):
            f.write(todos[i]+"\n")
        f.close()  
    elif press=="3":
        print("hello, here is your to-do list!")
        f=open('to-do.txt','r')
        todos2=f.read().split('\n')
        for line in todos2:
            print(line)
        f.close()
    else:
        exit ()    
ch=input('start? (Yes/No)')
while ch=="Yes":
    todolist()
else:
    print('Thank you!')