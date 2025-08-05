import uuid
from collections import Counter


class OnlineShop:
    def __init__(self):
        self.users = []
        self.sellers = []
        self.products = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            return "user is already exist"

    def fav_list_by_username(self, name):

        for usr in self.users:
            if name == usr.username:
                return usr.favorites

        return "username is invalid"

    def most_interset_item_for_all(self):

        data = [fav for user in self.users for fav in user.favorites]
        data = Counter(data)
        data = {value for value, count in data.items() if count > 1}
        return data

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
        return "already exist"

    def add_seller(self, seller):
        self.sellers.append(seller)

    def remove_favorite(self, name=None, item=None):
        if name and item:
            for user in self.users:
                if name == user.username:
                    user.remove_from_list(item)

        return "this username is not exist"

    def add_favorites(self, name=None, item=None):
        if name and item:
            for user in self.users:
                if name == user.username:
                    user.add_to_fav(item)


class Seller:
    def __init__(self, name):
        self.name = name


class User:
    def __init__(self, username):
        self.username = username
        self.favorites = []

    def add_to_fav(self, items):
        if isinstance(items, list):

            for item in items:
                if item not in self.favorites:
                    self.favorites.append(item)

        else:
            if items not in self.favorites:
                self.favorites.append(items)

    def remove_from_list(self, item):
        for fav in self.favorites:
            if item == fav.name:
                self.favorites.remove(fav)

    def show_favorite(self):
        return [str(item) for item in self.favorites]


class Product:
    def __init__(self, name):
        self.name = name
        self.id = self.gen_id()

    @staticmethod
    def gen_id():

        return uuid.uuid4()  # random id

    def __str__(self):
        return f"{self.name}"


try:

    product1 = Product("iphone17")
    product2 = Product("iwatch 9")
    product3 = Product("airpod3")
    product4 = Product("macbookairm4")
    prodcut5 = Product("hp-laptop")
    prodcut6 = Product("nothing-phone3")
    prodcut7 = Product("ausu-laptop")
    # print(item1.name)
    # print(item1.id)

    user1 = User("majid12")
    user2 = User("mehdi_m")
    user3 = User("romi")
    user4 = User("ramin")

    shop1 = OnlineShop()
    shop1.add_user(user1)
    shop1.add_user(user2)
    shop1.add_user(user3)
    shop1.add_user(user4)

    shop1.add_product(product1)
    shop1.add_product(product2)
    shop1.add_product(product3)
    shop1.add_product(product4)
    shop1.add_product(prodcut5)
    shop1.add_product(prodcut6)
    shop1.add_product(prodcut7)

    shop1.add_favorites("ramin", [product1, product2, product3])
    shop1.add_favorites("romi", [product1, product4, prodcut5])
    shop1.add_favorites("majid12", [product3, prodcut7, prodcut6])
    shop1.add_favorites("mehdi_m", [product3, prodcut7, prodcut6, product1])

# print(shop1.users)
# print(shop1.products)

    # print(shop1.fav_list_by_username("ramin"))
    # print(shop1.fav_list_by_username("romi"))
    # print(shop1.fav_list_by_username("majid12"))
    # print(shop1.fav_list_by_username("mehdi_m"))
    print(shop1.most_interset_item_for_all())

except ValueError as e:
    print(e)
except TypeError as e:
    print(e)
except Exception as e:
    print(e)
