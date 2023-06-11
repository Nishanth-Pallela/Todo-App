from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print(now)
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos_arg=todos)
    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            index = index + 1
            print(f"{index}. {item}")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos_arg=todos)
        except ValueError:
            print('Your command is invalid.')
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"{todo_to_remove} has been completed.")
        except ValueError:
            print('Your command is invalid.')
            continue
    elif user_action.startswith('exit'):
        break


print('Goodbye')
