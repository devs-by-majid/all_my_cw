from datetime import datetime


class Profile:
    def __init__(self, name, email, sign_up_date, role):
        self.name = name
        self.email = email
        self.date = sign_up_date
        self.role = role
        self.user = self.get_role()

    def get_role(self):
        if self.role == "premium":
            return PremiumUser()

        if self.role == "standard":
            return StandardUser()

    def create_post(self, content):
        post = Post(content)
        self.user.posts.append(post)

    def edit_post(self, index, new_content):
        if isinstance(self.user, PremiumUser):
            self.user.edit_posts(index, new_content)
        else:
            raise TypeError

    def delete_post(self, index):
        if isinstance(self.user, PremiumUser):
            self.user.delete_posts(index)
        else:
            raise TypeError

    def post_data(self):
        if isinstance(self.user, PremiumUser):
            self.user.access_post_index()
        else:
            raise TypeError

    def view_posts(self):
        self.user.seen_post()


class PremiumUser:

    def __init__(self):
        self.posts = []

    def access_post_index(self):
        likes = sum(post.likes for post in self.posts)
        shares = sum(post.shares for post in self.posts)
        print(f"Total likes: {likes}, Total shares: {shares}")

    def delete_posts(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]

    def edit_posts(self, index, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].content = new_content

    def seen_post(self):
        for post in self.posts:
            return post


class StandardUser:

    def __init__(self):
        self.posts = []

    def create_post(self, content):
        post = Post(content)
        self.posts.append(post)

    def seen_post(self):
        for post in self.posts:
            return post


class Post:
    def __init__(self, content, like_count=0, shares_count=0):
        self.content = content
        self.like_count = like_count
        self.shares_count = shares_count

    def __repr__(self):
        return f"{self.content} has {self.like_count} and {self.shares_count}"


try:
   
    prof1 = Profile("majid", "majid-official@gmail.com", datetime.now(), "premium")
    print(prof1.user.name)








except TypeError as e:
    print(e)
except AttributeError as e:
    print(e)    
