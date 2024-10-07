# Task Manager

Task Manager is a simple and effective task management tool designed to help you organize your daily tasks. With this tool, you can easily add, remove, and display your tasks in a Markdown file.

## Features
- **Add Tasks**: Easily add tasks to your list. 
- **Remove Tasks**: Remove one or more tasks by specifying their numbers. 
- **Display Tasks**: Display your numbered task list for a quick overview. 
- **Markdown Format**: Tasks are stored in a Markdown file, making them easy to read and manage. 

## Prerequisites 
- Python 3.x 
- No external libraries required 

## Installation 

1. Clone the repository: 

    ```bash
    git clone https://github.com/benoitxyz/TodoManager.git
    cd TodoManager 

2. Create an alias to the main script in your favorite .bashrc and .zshrc
    ```bash
    alias tdm = python /path/to/the/repository/

3. Init the todo list in your folder
    ```bash
    tdm init

4. Run the main script: tdm <commande>

## Usage
- **Add a Task** : To add a task, use the following function: tdm add "task to add"
- **Remove a Task** : To remove one or more tasks, use the following function:  
  - tdm delete 1,2,3 # Removes tasks 1, 2, and 3
  - tdm delete 2-4 # Removes tasks from 2 to 4
- **Display Tasks** : To display the list of tasks: tdm list

## Help and Support
For any questions or issues, please open an issue on the GitHub repository or contact the author.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for using Task Manager to manage your tasks!

*Edit: this is my first contribution, please be kind ;-).*
