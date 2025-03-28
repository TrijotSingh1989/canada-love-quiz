import os

def print_tree(startpath, indent=""):
    for item in os.listdir(startpath):
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(indent + "├── " + item)
            print_tree(path, indent + "│   ")
        else:
            print(indent + "├── " + item)

if __name__ == "__main__":
    print("📁 Project Structure:\n")
    print_tree(".")
