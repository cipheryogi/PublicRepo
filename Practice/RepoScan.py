import os

def search_for_passwords(file_path):
    passwords = []
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line_num, line in enumerate(file, start=1):
            # Search for lines containing various keywords or patterns
            keywords = ["password","passwords","Password","Passwords","passwd", "secret", "key", "token", "credentials", "auth", "access", 
                        "apikey", "api_key", "apiSecret", "api_secret", "clientSecret", "client_secret", 
                        "privateKey", "private_key", "oauth", "bearer"]
            if any(keyword in line.lower() for keyword in keywords):
                passwords.append((file_path, line_num, line.strip()))
    return passwords

# Function to traverse files in a directory
def traverse_files(directory):
    passwords_found = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not file_path.endswith('.git'):  # Skip Git-related files
                passwords_found.extend(search_for_passwords(file_path))
    return passwords_found

# Function to write findings to a text file
def write_findings_to_file(passwords_found, output_file):
    with open(output_file, 'w') as f:
        if passwords_found:
            f.write("Passwords found:\n")
            for file_path, line_num, password in passwords_found:
                f.write(f"File: {file_path}, Line: {line_num}, Password: {password}\n")
        else:
            f.write("No passwords found.")

# Main function to scan the local directory
def scan_local_directory(directory_path, output_file):
    passwords_found = traverse_files(directory_path)
    write_findings_to_file(passwords_found, output_file)

# Replace 'path_to_your_local_directory' with the path to your local directory
local_directory_path = '/Users/yogesh.shinde/Library/CloudStorage/OneDrive-ServiceNow/Learning & Development/PublicRepo'
output_file = 'password_findings.txt'
scan_local_directory(local_directory_path, output_file)