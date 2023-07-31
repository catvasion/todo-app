todos = []

while True : 
    user_action = input("Type add, show, edit, remove or exit:")
    user_action = user_action.strip() # remove white space
    
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo) # method
            
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case "show":
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index + 1}.{item}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit:"))
            number = number -1 
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case "remove":
            number = int(input("Number of the todo to remove:"))
            todos.pop(number - 1)
            
            
        case "exit":
            break 
        
         
print("Bye!")



    


    
    
    
