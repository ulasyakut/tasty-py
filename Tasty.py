#!/usr/bin/env  python3

import sys
import json
import os

class Tasty:
    """
    Tasty class.
    :param tasks: the user tasks
    :param important_tasks: the important user tasks
    :param complete: the completed tasks
    :param unfinished: the unfinished tasks
    :param trash: the user trash
    :param version: the Tasty version
    :param save_file: the Tasty save file
    """
   
    # make sure to do an __init__ method

    def __init__(self):
        self.tasks={}
        self.trashs={}

    def display_tasks(self):
        for task_name, status in self.tasks.items():
            print("- ",task_name,status)

    def help(self):
        """
        Display a help message.
        """
        print("Tasty Help ")
        print("============================================================================")
        print("help                     ->        display this message")
        print("tasks                    ->        display all your tasks")
        print("trash                    ->        display the content of the trash")
        print("new <task>               ->        add a new task")
        print("remove <task>            ->        add a task to the trash")
        print("complete <task>          ->        complete a task")
        print("unfinish <task>          ->        unfinish a task")
        print("recover <task>           ->        recover a removed task")
        print("destroy <task>           ->        remove a task from the trash")
        print("advancement              ->        see the tasks advancement")
        print("exit                     ->        exit Tasty")
        print("save                     ->        save your current tasks")
        print("load                     ->        load a save file")
        print("clear                    ->        clear the screen")
        
    def license(self):

        """
        Display the MIT License terms for Tasty.
        """
        print("""
Copyright (c) 2024 Tasty

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        """)

    def prompt_user(self,prompt):
        line =input(prompt)
        while not line:
            line =input(prompt)
        words = line.split()
        command = words[0]
        rest = words[1:]
        rest = " ".join(rest)
        return command,rest
        
    def add_task(self,task_name):
        if task_name not in self.tasks:
            self.tasks[task_name] = 'not yet'
        else:
            print('its already in list')

    def complete_task(self,task_name):
        if self.tasks[task_name] == 'not yet':
            self.tasks[task_name] = 'completed'
        else:
            print('task is already done')

    def unfinish_tasks(self,task_name):
        if self.tasks[task_name] == 'completed':
            self.tasks[task_name] = 'not yet'
        else:
            print('task is alread unfinished')

    def save(self):
        with open("saved_data.json", "w") as fp:
            json.dump(self.tasks,fp)

    def load(self):
        with open('saved_data.json', 'r') as fp:
            self.tasks = json.load(fp)
        
    def exit(self):
        print("Bye bye")
        exit()

    def clear(self):
        os.system('cls' if os.name == "nt" else "clear")

    def remove(self,task_name):
        self.trashs[task_name] = self.tasks[task_name]
        del self.tasks[task_name]

    def recover(self,task_name):
        
        self.tasks[task_name] = self.trashs[task_name]
        del self.trashs[task_name]
    
    def trash(self):
         for task_name, status in self.trashs.items():
            print("- ",task_name,status)

if __name__ == "__main__":
    tasty = Tasty()
    tasty.help()
    #tasty.tasks["fooo"] = "incomplete"
    while True:
        command,rest = tasty.prompt_user("Type someting: ")
        if command == "exit":
            pass # exit the program, how would you do this?
        elif command == "help":
            tasty.help()
        elif command == "license":
            tasty.license()
        elif command == "tasks":
            tasty.display_tasks()
        elif command == "new":
            tasty.add_task(rest)
        elif command == "complete":
            tasty.complete_task(rest)
        elif command == "unfinished":
            tasty.unfinish_tasks(rest)    
        elif command == "save":
            tasty.save()
        elif command == "load":
            tasty.load()
        elif command == "exit":
            tasty.exit()
        elif command == "clear":
            tasty.clear()
        elif command == "remove":
            tasty.remove(rest)
        elif command == "trash":
            tasty.trash()
        elif command == "recover":
            tasty.recover(rest)
        else:
            print("Unknown command")