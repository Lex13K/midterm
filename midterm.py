print("Welcome to the MIDTERM")

# 1

# a = 10
#
# a = a + 2
#
# print(a*2)
#
# a = 19
#
# print(a+3)
#
# a = a // 2
#
# print(a)
#

# 2
# print(2+3*6/2)

# 3

# import datetime
#
# a = 7
# b = 2
# today = datetime.datetime.today()
# day_of_week = today.weekday()
# month_of_year = today.month
# a = a + day_of_week
# b += month_of_year
#
# print(a)
# print(b)
# c = a + b
# print(c)
# d = "xyz" * (c // 3)
# print(d)

# 4

#
# def palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
# print(palindrome("7798338247658278460338648728567428338977"))
# print(palindrome("2704702208931031198668911301398022074072"))
# print(palindrome("4257304920394478392772938744930294037524"))
# print(palindrome("0974101607733149676776769413377061014790"))
#

# 5
#
# with open('text.txt') as file:
#     book = file.read()     # just an old text tile because i was interested if there was a word like that in there
# file.close()
#
#
#
#
# def unanCkecker(text):
#     c = 0
#     punct = ",.-'!?\"()*+/:;"  # defining punctuations for later
#
#     lines = text.splitlines()  # i assumed the text given could have several lines
#     i = 0
#     for line in lines:
#         words = lines[i].split(' ') # spliting word by word
#         i += 1
#         for word in words:
#             for p in punct:
#                 text = text.replace(p, "")  # replacing them with nothing so they dont block me from counting the words properly
#             word = word.lower() # doing lowercases
#             if word.startswith('un') and word.endswith('an'): # the actual checking happens here
#                 c += 1
#     return c
#
#
# print(unanCkecker("the umbrella was very unananan by alexander unan")) # just random text

# def secondUnanCkecker(text):
#     for p in len(text):
#         if

# 6
#
# ostring = "Hello, World!"
# # ostring[0] = "J"
# new = "HHH" + ostring[1:]
#
# print(new)
# 7
# import random
# random_numbers = []
# for i in range(10):
#     random_numbers.append(random.randint(1, 100))
#
# for i in range(10):
#     if random_numbers[i] > 80:
#         random_numbers[i] = -random_numbers[i]
#     print(random_numbers[i])

# 8

# def linkValidity(text):
#     if text.startswith("http://") or text.startswith("https://") or text.startswith("ftp://"):
#         return True  # there are many things that define a valid link but given the current class knowledge
#     else:            # i very simply checked if it starts with one of these but still there are a lot of links
#         return False # this function does not account for
#
#
# text = "https://github.com/Lex13K/midterm"
#
# print(linkValidity(text))

# 9
# def daysOld(date):
#     dateNow = "01-03-2024"
#     parts = date.split('-')
#     day = int(parts[0])
#     month = int(parts[1])
#     year = int(parts[2])        # getting just what we need plus other info for later development of function
#     parts = dateNow.split('-')
#     dayNow = int(parts[0])
#     monthNow = int(parts[1])
#     yearNow = int(parts[2])    # getting what we need
#
#     total_days = 0
#     for year in range(year + 1, yearNow):  # exclude birth year and current year
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # factoring in for leap years
#             total_days += 366
#         else:
#             total_days += 365
#
#     return total_days
#
# birthDate = "13-11-2004"
# print(daysOld(birthDate))

# 10

# https://github.com/Lex13K/midterm author alex