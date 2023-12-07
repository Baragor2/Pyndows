class FileSystem:
    files = []

    def __init__(self):
        print("FileSystem")
        if not self.files:
            print('Directory is empty')
        else:
            print("Your files", *self.files)
        print('Enter "help" for more information')

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
FileSystem.create_file('file')

print(
'''
Hello, Pyndows user!
What do you want to do?
1. File system
2. CLock
3. Calculator
4. Memory
'''
)
num = input()

match(num):
    case '1':
        MyFiles = FileSystem()



