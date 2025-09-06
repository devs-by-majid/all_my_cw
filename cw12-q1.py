import requests
import csv
import json
import os
from custom_exceptions import FileISEmptyError
import argparse

try:
    

    file_path = "user_posts.json"
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(resp.status_code)

    if resp.status_code == 200:
        resp = resp.json()

        posts = [
            {"userId": post["userId"], "id": post["id"], "title": post["title"][0:40]}
            for post in resp
        ]

        # with open(file_path, "wt") as file:
        #         json.dump(resp, file)

        with open("output.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file, fieldnames=["userId", "id", "title"]
            )  # filedsname are column header inside excel
            writer.writeheader()
            writer.writerows(post for post in posts)

        file_size = os.path.getsize("output.csv")
        if file_size == 0:
            raise FileISEmptyError("file is empty")

        print("file is contain data")
        with open(file_path, "r") as file:
            posts = json.load(file)

    else:
        raise resp.raise_for_status()

except FileISEmptyError as e:
    print(e)

except FileNotFoundError as e:
    print(e)

except requests.exceptions.HTTPError as httpErr:
    print(httpErr.args[0])
except requests.ConnectionError as e:
    print(e)
except requests.ConnectTimeout as e:
    print(e)
except requests.exceptions.InvalidJSONError as e:
    print(e)





# two way of validating file empty or not
# 2-  file_size=os.stat(file_path).st_size
# file is empty  if file_size ==0 else file is not empty


# file_path = "input1.txt"
# 3
# open the file in read mode
# with open(file_path, 'r') as file_obj:
# move the file pointer from 0th position to end position
# file_obj.seek(0, os.SEEK_END)

# return the current position of file pointer
# file_size = file_obj.tell()

# if file size is 0, it is empty
# if file_size == 0:
# print("File is empty")
# else:
# print("File is NOT empty")
