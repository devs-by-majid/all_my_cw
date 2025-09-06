import requests
import json
import csv
import argparse


class PostFetcher:

    api_url = "https://jsonplaceholder.typicode.com/posts"

    def __init__(self):
        self.data = []

    def fetch_posts(self):
        resp = requests.get(PostFetcher.api_url)
        self.data = resp.json()
        return self.data

    def filter_posts(self, postid):
        self.api_url += f"/{postid}"
        resp = requests.get(self.api_url)
        self.data.append(resp.json())
        return self.data

    def save_to_file(self, filename, format="json"):

        new_data = [
            {"userId": post["userId"], "id": post["id"], "title": post["title"][:40]}
            for post in self.data
        ]

        if format == "json":
            with open(f"{filename}.{format}", "w") as file:
                json.dump(self.data, file)

        elif format == "csv":
            with open(f"{filename}.{format}", "w") as file:
                writer = csv.DictWriter(file, fieldnames=["userId", "id", "title"])
                writer.writeheader()
                writer.writerows(new_data)
        else:
            print("unsupported file format")


def main():
    fetcher = PostFetcher()

    parser = argparse.ArgumentParser(description="request to url based on user asks")
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["json", "csv"],
        default="json",
        help="chooce file format",
    )
    parser.add_argument(
        "--search", "-p", type=int, help="type a nubmber of post to get from url"
    )

    args = parser.parse_args()

    if args.search:
        print(fetcher.filter_posts(args.search))

        if args.format == "json":

            fetcher.save_to_file("post")
            return

        fetcher.save_to_file("post", "csv")

    elif args.search is None:
        print(fetcher.fetch_posts())
        if args.format == "json":

            fetcher.save_to_file("posts")
            return
        fetcher.save_to_file("posts", "csv")


if __name__ == "__main__":
    main()
