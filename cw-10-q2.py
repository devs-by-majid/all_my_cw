import re


my_string='1404-13-05'
regex_pat=r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

# data=re.split(r'-',my_string)

check=re.match(regex_pat,my_string)


check="valid date"if check else "invalid-date"
print(check)
