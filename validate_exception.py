


class InvalidUsername(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidPassword(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidEmail(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidTelNumber(Exception):
    def __init__(self, msg):
        super().__init__(msg)