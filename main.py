import time
import pickle
from rich.console import Console
console = Console()

class Pyndows:
    def __init__(self):
        print(
'''Hello, Pyndows user!
What do you want to do?
1. File system
2. CLock
3. Calculator
4. Memory''')
        self.choose_func()

    def choose_func(self):
        num = input()

        match (num):
            case '1':
                MyFiles = FileSystem()
            case '2':
                Time = Clock()
            case '4':
                Mem = Memory()
            case _:
                console.print("[italic red]Incorrect input[/italic red]")
                self.choose_func()


class FileSystem:
    files = []
    try:
        with open("files.bin", "rb") as file:
            files = pickle.load(file)
    except:
        print("File error")

    def __init__(self):
        print("FileSystem")
        print('Enter "help" for more information')
        self.basic_method()

    def basic_method(self):
        choice = input().strip()
        if not choice:
            console.print("[italic red]Incorrect input[/italic red]")
            self.basic_method()
        choice = choice.split()
        if len(choice) < 2 and choice[0] in ['create', 'remove', 'rename']:
            console.print("[italic red]Incorrect input[/italic red]")
            self.basic_method()

        match(choice[0]):
            case 'help':
                self.help_files()
            case 'create':
                self.create_file(choice[1])
            case 'remove':
                self.remove_file(choice[1])
            case 'rename':
                self.rename_file(choice[1])
            case 'show':
                self.show_files()
            case 'clear':
                print("Are you sure? - Yes/No")
                answer = input()
                if answer == 'Yes':
                    self.clear_files()
                elif answer == 'No':
                    self.basic_method()
                else:
                    console.print("[italic red]Incorrect input[/italic red]")
                    self.basic_method()
            case 'exit':
                self.exit()
            case _:
                console.print("[italic red]Incorrect input[/italic red]")
                self.basic_method()

    def help_files(self):
        print(
'''1.To create a file, enter "create <filename>"
2.To remove a file, enter "remove <filename>"
3.To rename a file, enter "rename <filename>"
4.To show a list of files, enter "show"
5.To clear all files, enter "clear"
6.To exit from File Sistem, enter "exit"''')
        self.basic_method()

    def show_files(self):
        if not self.files:
            print('Directory is empty')
        else:
            print("Your files:", end=' ')
            print('; '.join(self.files))
        self.basic_method()

    def create_file(self, filename):
        for file in self.files:
            if file == filename:
                print("The file already exists")
                self.basic_method()
        self.files.append(filename)
        self.basic_method()

    def remove_file(self, filename):
        for file in self.files:
            if file == filename:
                self.files.remove(filename)
                self.basic_method()
        print("This file doesn't exist")
        self.basic_method()

    def rename_file(self, filename, new_filename):
        for ind, file in enumerate(self.files):
            if file == filename:
                self.files[ind] = new_filename
                self.basic_method()
        print("This file doesn't exist")
        self.basic_method()

    def clear_files(self):
        self.files = []
        self.basic_method()

    def exit(self):
        try:
            with open("files.bin", "wb") as file:
                pickle.dump(self.files, file)
        except:
            print("[italic red]File error[/italic red]")
        os = Pyndows()
        os.choose_func(self)

class Clock:
    def __init__(self):
        print("Clock interface")
        print('Enter "help" for more information')
        self.basic_method()

    def basic_method(self):
        choice = input()
        if not choice:
            console.print("[italic red]Incorrect input[/italic red]")
            self.basic_method()
        match (choice):
            case 'help':
                self.help_clock()
            case 'time':
                self.show_time()
            case 'date':
                self.show_date()
            case 'exit':
                self.exit()
            case _:
                console.print("[italic red]Incorrect input[/italic red]")
                self.basic_method()

    def help_clock(self):
        print(
'''1.To see the time, enter "time"
2.To see the date, enter "date"
3.To exit from Clock interface, enter "exit"''')
        self.basic_method()

    def show_time(self):
        your_time = time.localtime()
        print(f'{your_time.tm_hour}:{your_time.tm_min}:{your_time.tm_sec}')
        self.basic_method()

    def show_date(self):
        your_date = time.localtime()
        print(f'{your_date.tm_mday}/{your_date.tm_mon}/{your_date.tm_year}')
        self.basic_method()

    def exit(self):
        os = Pyndows()
        os.choose_func(self)

class Memory:
    def __init__(self):
        print("Memory interface")
        print('Enter "help" for more information')
        self.basic_method()

    def basic_method(self):
        choice = input()
        if not choice:
            console.print("[italic red]Incorrect input[/italic red]")
            self.basic_method()
        match (choice):
            case 'help':
                self.help_memory()
            case 'total':
                self.show_total()
            case 'remaining':
                self.show_remaining()
            case 'exit':
                self.exit()
            case _:
                console.print("[italic red]Incorrect input[/italic red]")
                self.basic_method()

    def help_memory(self):
        print(
'''1.To see total memory, enter "total"
2.To see remaining memory, enter "remaining"
3.To exit from Memory interface, enter "exit"''')
        self.basic_method()

    def show_total(self):
        print('Total memory: 500mb')
        self.basic_method()

    def show_remaining(self):
        try:
            with open("files.bin", "rb") as file:
                files = pickle.load(file)
        except:
            print("[italic red]File error[/italic red]")
        print(f"Remaining memory: {500 - len(files)}mb")
        self.basic_method()

    def exit(self):
        os = Pyndows()
        os.choose_func(self)


os = Pyndows()




