FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads a text file and return the list of
    to-do items.
    """
    with open(f"{filepath}", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items lst in the text file."""
    with open(f"{filepath}", "w") as file:
        file.writelines(todos_arg)


def create_student(name, info):
    with open(f"{name}.txt", "w") as file:
        file.writelines(info)


def open_file(filepath):
    """Returns a list of the lines in a file."""
    with open(filepath) as file:
        alist = file.readlines()
    return alist


if __name__ == "__main__":
    print("Hello")
