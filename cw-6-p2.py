import string


class Book:
    def __init__(self, name, title, author):
        self.name = name
        self.title = title
        self.id = self.gen_id()
        self.authors = author

    def gen_id(self):
        return f"{string.punctuation[:4]}{self.name}-{string.digits[:4]}-{self.title}"

    def __str__(self):
        return f"book_name:{self.name}-title:{self.title}-authors:{[auth.name for auth in self.authors]} "


class PrintedBook(Book):
    def __init__(self, name, title, count, author):
        super().__init__(name, title, author)
        if isinstance(count, int):
            self.page_count = count
        else:
            print('book page count must be integer')


class Ebook(Book):
    def __init__(self, name, title, file_size, author):
        super().__init__(name, title, author)
        if isinstance(file_size, str):
            self.fsize = file_size
        else:
            print("filesize must be string")


class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email


author1 = Author("majid", "majid75@gmail.com")
author2 = Author("saeed", "big_saeed@gmail.com")
author3 = Author("eli", "eli_official@gmail.com")
author4 = Author("ramin", "ramin_geek@gmail.com")

book1 = PrintedBook("poor and rich dad", 'self_growth', 320, [author2])
ebook1 = Ebook("ebook1", 'Inforamtion_tech', "32.mb", [author3, author4])

print(book1)
print(ebook1)
