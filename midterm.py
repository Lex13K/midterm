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

with open('text.txt') as file:
    book = file.read()     # just an old text tile because i was interested if there was a word like that in there
file.close()




def unanCkecker(text):
    c = 0
    punct = ",.-'!?\"()*+/:;"  # defining punctuations for later

    lines = text.splitlines()  # i assumed the text given could have several lines
    i = 0
    for line in lines:
        words = lines[i].split(' ') # spliting word by word
        i += 1
        for word in words:
            for p in punct:
                text = text.replace(p, "")  # replacing them with nothing so they dont block me from counting the words properly
            word = word.lower() # doing lowercases
            if word.startswith('un') and word.endswith('an'): # the actual checking happens here
                c += 1
    return c


print(unanCkecker("the umbrella was very unananan by alexander unan")) # just random text

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
