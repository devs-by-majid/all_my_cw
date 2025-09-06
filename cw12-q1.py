import requests
import csv
import json
import os
from custom_exceptions import FileISEmptyError, FileFormatError
import argparse


def get_post(postid=None, format="json"):
    try:
        url = (
            f"https://jsonplaceholder.typicode.com/posts/{args.user}"
            if postid
            else "https://jsonplaceholder.typicode.com/posts"
        )

        resp = requests.get(url)
        if resp.status_code != 200:
            resp.raise_for_status()

        file_name = f"fetch_post.{format}"
        resp = resp.json()

        data = (
            [
                {
                    "userId": post["userId"],
                    "id": post["id"],
                    "title": post["title"][0:40],
                }
                for post in resp
            ]
            if isinstance(resp, list)
            else {
                "userId": resp["userId"],
                "id": resp["id"],
                "title": resp["title"][0:40],
            }
        )

        if format == "json":

            with open(file_name, "wt") as file:
                json.dump(data, file)

            file_size = os.path.getsize(file_name)
            if file_size == 0:
                raise FileISEmptyError("file is empty")

            else:
                with open(file_name, "r") as file:
                    posts = json.load(file)

                return posts

        if format == "csv":
            # filedsname are column header inside excel
            with open(file_name, "w", newline="", encoding="utf-8") as file:

                writer = csv.DictWriter(file, fieldnames=["userId", "id", "title"])
                writer.writeheader()
                if isinstance(data, list):

                    writer.writerows(data)
                else:
                    writer.writerow(data)

            file_size = os.path.getsize(file_name)
            if file_size == 0:
                raise FileISEmptyError("file is empty")

            return

    except FileFormatError as e:
        print(e)

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


try:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--user", type=int)
    parser.add_argument("-f", "--format", default="json")

    args = parser.parse_args()

    if args.user:
        if args.format and args.format == "json":
            get_post(args.user)

        elif args.format and args.format == "csv":
            get_post(args.user, "csv")

        else:
            raise FileFormatError("file format is not excepted")
    else:
        if args.format and args.format == "json":
            get_post()

        elif args.format and args.format == "csv":
            get_post(None, "csv")

        else:
            raise FileFormatError("file format is not excepted")

except FileFormatError as e:
    print(e)
