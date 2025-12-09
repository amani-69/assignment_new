from html import parser
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="enter a valid github username")

#collecting the args where theyre going to be passed
args = parser.parse_args()

username = args.username


# 1. ask user for input
#username = input("Enter GitHub username: ")

# 2. format the URL using the username
url = f"https://api.github.com/users/{username}/events"

# 3. make request to the formatted URL
response = requests.get(url)

# Check if the request worked
if response.status_code != 200:
    print("Error retrieving data. Status code:", response.status_code)
    exit()

# 4. get JSON response
events = response.json()

# 5. loop through events and look for CreateEvent
for event in events:
    if event["type"] == "CreateEvent":
        repo_name = event["repo"]["name"]
        repo_url = f"https://github.com/{repo_name}"

        print(f"{username} created a GitHub repo '{repo_name}' found at {repo_url}")
        break
else:
    print("No CreateEvent found for this user.")

