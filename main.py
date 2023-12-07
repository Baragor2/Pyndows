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
                print("Incorrect input ")


class FileSystem:
    files = []

    def __init__(self):
        print("FileSystem")
        print('Enter "help" for more information')
        if input() == 'help':
            self.help_files()
        else:
            print("Incorrect input ")

    @staticmethod
    def help_files():
        print(
'''1.To create a file, enter "create <filename>"
2.To remove a file, enter "remove <filename>"
3.To rename a file, enter "rename <filename>"
4.To show a list of files, enter "show files"''')

    @classmethod
    def show_files(cls):
        if not self.files:
            print('Directory is empty')
        else:
            print("Your files:", *self.files)

    @classmethod
    def create_file(cls, filename):
        for file in cls.files:
            if file == filename:
                print("The file already exists")
                return
        cls.files.append(filename)

    @classmethod
    def remove_file(cls, filename):
        for file in cls.files:
            if file == filename:
                cls.files.remove(filename)
                return
        print("This file doesn't exist")

    @classmethod
    def rename_file(cls, filename, new_filename):
        for ind, file in enumerate(cls.files):
            if file == filename:
                cls.files[ind] = new_filename
                return
        print("This file doesn't exist")

os = Pyndows()
FileSystem.create_file('file')



