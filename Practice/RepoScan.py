import os

# Function to search for passwords in a file
# def search_for_passwords(file_path):
#     passwords = []
#     with open(file_path, 'r') as file:
#         for line_num, line in enumerate(file, start=1):
#             # Example: Search for lines containing the word "password"
#             if 'password' in line.lower():
#                 passwords.append((file_path, line_num, line.strip()))
#             # You can add more conditions to check for different patterns or formats
#     return passwords

def search_for_passwords(file_path):
    passwords = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            # Search for lines containing various keywords or patterns
            keywords = ["password", "passwd", "secret", "key", "token", "credentials", "auth", "access", 
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

# Main function to scan the Git repository
def scan_git_repo(repo_path):
    passwords_found = traverse_files(repo_path)
    if passwords_found:
        print("Passwords found:")
        for file_path, line_num, password in passwords_found:
            print(f"File: {file_path}, Line: {line_num}, Password: {password}")
    else:
        print("No passwords found.")

# Replace 'path_to_your_git_repo' with the path to your Git repository
git_repo_path = 'https://github.com/cipheryogi/PublicRepo/tree/main/Practice'
scan_git_repo(git_repo_path)
