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
            case _:
                print("Incorrect input")
                self.choose_func()


class FileSystem:
    files = []

    def __init__(self):
        print("FileSystem")
        print('Enter "help" for more information')
        self.basic_method()

    def basic_method(self):
        choice = input().split()
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
            case _:
                print("Incorrect input ")
                self.basic_method()

    def help_files(self):
        print(
'''1.To create a file, enter "create <filename>"
2.To remove a file, enter "remove <filename>"
3.To rename a file, enter "rename <filename>"
4.To show a list of files, enter "show files"''')
        self.basic_method()

    def show_files(self):
        if not self.files:
            print('Directory is empty')
        else:
            print("Your files:", *self.files)
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

os = Pyndows()




