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


# Creates an object
file1 = FileAnalyzer("notepad.txt")
file2 = FileAnalyzer("shadow.txt")

# Shows the filename
file1.show_name()
file2.show_name()