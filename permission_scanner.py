import os 

class FileAnalyzer:
    """
    To represent a file meant to be analyzed.
    """
    def __init__(self, filename: str):
        """
        Saves the filename
        """
        self.filename = filename

    def show_name(self) -> None:
        """
        Prints out the file name
        """
        print(self.filename)

    def file_exists(self):
        """
        Function here sees if the file exists at all.
        """
        if os.path.exists(self.filename):
            return True
        else:
            return False


# Creates an object
file1 = FileAnalyzer("notepad.txt")
file2 = FileAnalyzer("find_me.html")

# Shows the filename
file1.show_name()
print(file1.file_exists())

file2.show_name()
print(file2.file_exists())