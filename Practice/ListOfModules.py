import pkgutil

# Get a list of all modules in Python
all_modules = list(pkgutil.iter_modules())

# Define the file path and name
file_path = "/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/Caltech AI ML/Python Refresher/python3_module_list.txt"

# Open the specified text file to write module names
with open(file_path, 'w') as file:
    # Write the names of all modules to the file
    counter = 0
    for module in all_modules:
        counter += 1
        file.write(str(counter) + ' ' + module.name + '\n')
        
# Read and display the contents of the file
with open(file_path, 'r') as file:
    file_contents = file.read()
    print(file_contents)

