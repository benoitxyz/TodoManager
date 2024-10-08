import os
from config import Config

def init(titre):
    test_result = test_todo_file()
    if test_result == "OK" :
        print('Todo list already initialized')
    elif test_result == "WRONG" :
        print(f'A file with target name {Config.TODO_FILE} already exist in the directory')
    else:
        # If the file don not exist, create one with title and end file comment.
        with open(Config.TODO_FILE, 'w') as f:
            f.write(f"# {titre}\n")
            f.write("\n")  # Empty line to separate comment from tasks
            f.write(Config.END_FILE_COMMENT + "\n")
        print(f"Todo file '{Config.TODO_FILE}' had been initialized")
    
def test_todo_file():
    if os.path.isfile(Config.TODO_FILE):
        # Check if comment is present in the file
        with open(Config.TODO_FILE, 'r') as f:
            contenu = f.read()
            if Config.END_FILE_COMMENT in contenu:
                return "OK"
            else:
                return "WRONG"
    else:
        return "MISSING"