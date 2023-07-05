# ? lIst comprehension questions practice
# ? Question1.Find all of the numbers from 1–1000 that are divisible by 8
# [print(num) for num in range(1, 1001) if num % 8 == 0]
# ? Question2.Find all of the numbers from 1–1000 that have a 6 in them
# [print(num) for num in range(1, 1001) if "6" in str(num)]
# ? Question3.Count the number of spaces in a string
# sentnce = "Learning Python is very easy"
# print(len([i for i in sentnce if i == " "]))
# ? Question4.Remove all of the vowels in a string
# sentnce = "Learning Python is very easy"
# print("".join([i for i in sentnce if i not in ["a", "e", "i", "o", "u"]]))
# ? Question5.Find all of the words in a string that are less than 5 letters
# sentnce = "Learning Python is very easy"
# print([word for word in sentnce.split() if len(word) < 5])
# ? Question6. Use a dictionary comprehension to count the length of each word in a sentence
# sentnce = "Learning Python is very easy"
# print({word: len(word) for word in sentnce.split()})
# ? Question7.Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1 (2–9)
#! Using normal for loop :
# result = []
# for num in range(1, 101):
#    for i in range(2, 10):
#        if num % i == 0:
#            result.append(num)
#            break
# print(result)

#! Using list comprehension
# print(
#    [
#        num
#        for num in range(1, 101)
#        if True in [True for divisor in range(2, 10) if num % divisor == 0]
#    ]
# )

# ? Question8: Find the common numbers in two lists (without using a tuple or set)
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
#!way1
# print([i for i in list_a for j in list_b if i == j])
#!way2
# print([i for i in list_a if i in list_b])
# ? Question9: Get only the numbers in a sentence below
# sentnce = "In 1984 there were 13 instances of a protest with over 1000 people attending"
# print([word for word in sentnce.split() if not word.isalpha()])
# print([word for word in sentnce.split() if word.isdigit()])
# print([word for word in sentnce.split() if word.isdigit() == True])
# ? Question10: Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
# print(["even" if i % 2 == 0 else "odd" for i in range(20)])
# ? Question11: Produce a list of tuples consisting of only the matching numbers in these lists, Result would look like (4,4), (12,12)
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_b = [2, 7, 1, 12]
#!way1
# print([(i, j) for i in list_a for j in list_b if i == j])
#!way2
# print([(i, i) for i in list_a if i in list_b])
# ? Question12:Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
# fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
# print([fruit.upper() for fruit in fruits])

# ? Question13:create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
# fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
# print([fruit.capitalize() for fruit in fruits])
# ? Question14:Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
# fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
# print(
#    [
#        fruit
#        for fruit in fruits
#        if (
#            fruit.count("a")
#            + fruit.count("e")
#            + fruit.count("i")
#            + fruit.count("o")
#            + fruit.count("u")
#            > 2
#        )
#    ]
# )
# ? Question15:Question Use a list comprehension to remove vowels in each word
# fruits = ["mango", "kiwi", "strawberry", "guava", "pineapple", "mandarin orange"]
# print(
#    [
#        "".join(ch for ch in fruit if ch not in ["a", "e", "i", "o", "u"])
#        for fruit in fruits
#    ]
# )
# ? Question16: Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# print([number for number in numbers if number < 0 and number % 2 != 0])
# ? Question17:use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# print([number for number in numbers if number > 9 or number < -9])
# ? Question18:Given a sentence, return the setence will all it's letter transposed by 1 in the alphabet, but only if the letter is a-y.
# todo>>> encrypt_lol('the quick brown fox jumps over the lazy dog')
# todo>>>'uif rvjdl cspxo gpy kvnqt pwfs uif mbzz eph'
sentnce = "the quick brown fox jumps over the lazy dog"
#! Using Normal for loop : Way1
# for i in sentnce:
#    print(
#        "".join(chr(ord(i) + 1) if ord(i) in range(ord("a"), ord("z")) else i), end=""
#    )
# print()
#! Using Normal for loop : Way2
# l = []
# for word in sentnce.split():
#    newWord = ""
#    for ltr in word:
#        if ord(ltr) in range(ord("a"), ord("z")):
#            newWord = newWord + chr(ord(ltr) + 1)
#        else:
#            newWord = newWord + ltr
#    l.append(newWord)
# print(" ".join(l))
#! Using List Comprehension
# print(
#    "".join(
#        chr(ord(i) + 1) if ord(i) in range(ord("a"), ord("z")) else i for i in sentnce
#    )
# )
# ? Question19:Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
#
#
# def isPrime(num: int) -> bool:
#    primeCheck = False
#    if num > 1:
#        for i in range(2, num):
#            if num % i == 0:
#                primeCheck = False
#                break
#            else:
#                primeCheck = True
#    return primeCheck
#
#
# primenumbers = [number for number in numbers if isPrime(number)]
# print(primenumbers)
# ?Question20: You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.
# if __name__ == "__main__":
#    x = int(input("Enter the value of x: "))
#    y = int(input("Enter the value of y: "))
#    z = int(input("Enter the value of z: "))
#    n = int(input("Enter the value of n: "))
#
#    print(
#        list(
#            [i, j, k]
#            for i in range(x + 1)
#            for j in range(y + 1)
#            for k in range(z + 1)
#            if i + j + k != n
#        )
#    )
# ? Question21 :
# ? Input:
# ? >>>matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
# ? Desired output:
# ? >>> [[1, 3, 5, 7], [2, 4, 6, 8]]
# output = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
