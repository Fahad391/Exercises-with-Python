class Directory:

    def __init__(self, name: str, path:str):
        self.name = name
        self.path = path
        self.files = [] # Holds File objects

    # Created a Nested class
    class File:

        def __init__(self, name: str, extension: str, size_kb: float):
            self.name = name
            self.extension = extension
            self.size_kb = size_kb

        def get_filename(self) -> str:
            return f"{self.name}.{self.extension}"


    # Outer class method
    def add_file(self, name: str, extension: str, size_kb: float):

        new_file = self.File(name, extension, size_kb)
        self.files.append(new_file)
        print(f"Added '{new_file.get_filename()}' to {self.path}/{self.name}")

    def get_total_size(self) -> float:
        return sum(f.size_kb for f in self.files)

    def list_contents(self):
        print(f"\n📁 contents of {self.path}/{self.name}:")
        for file in self.files:
            print(f" - {file.get_filename()} ({file.size_kb} KB)")


# 1. Create the outer directory
documents_dir = Directory(name="Documents", path="/home/user")

# 2. Add files 
documents_dir.add_file("resume", "pdf", 250.5)
documents_dir.add_file("budget", "xlsx", 1020.0)
documents_dir.add_file("notes", "txt", 15.2)

# 3. View contents and total storage used
documents_dir.list_contents()
print(f"\nTotal Directory Size: {documents_dir.get_total_size()} KB")