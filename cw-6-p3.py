# class Score:
#     def __init__(self, score):
#         if isinstance(score, int):
#             self.value = score
#         else:
#             raise TypeError('instance type must be integer')

#     def __lt__(self, second):

#         if self.value < second.value:
#             return True
#         else:
#             return False

#     def __gt__(self, second):
#         if self.value > second.value:
#             return True
#         else:
#             return False

#     def __eq__(self, second):
#         if self.value == second.value:
#             return True
#         else:
#             return False

#     def __add__(self, second):
#         if isinstance(second,Score):
#             new_value = self.value + second.value
#             return Score(new_value)

#     def __sub__(self, second):
#         if isinstance(second,Score):
#           new_value = self.value - second.value
#           return Score(new_value)

#     def __repr__(self):
#         return f"score:{self.value} point"


class Score(int):
    
    def __lt__(self, second):
        return super().__lt__(second)

    def __gt__(self, second):
        return super().__gt__(second)

    def __eq__(self, second):
        return super().__eq__(second)

    def __add__(self, second):
        return super().__add__(second)

    def __sub__(self, second):
        return super().__sub__(second)

    def __repr__(self):
        return f"score:{super().__repr__()} point"


try:
    score1 = Score(10)
    score2 = Score(20)
    print(score1 > score2)
    print(score1 < score2)
    print(score1 == score2)
    score3 = score1+score2
    score4 = score1-score2
    print(score1+score2)
    print(score1-score2)
    print(score1)
    print(score2)
except TypeError as e:
    print(e)
