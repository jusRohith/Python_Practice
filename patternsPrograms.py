n = int(input("Enter a number : "))
# todo 1stQuestion:WAP given no.of *'s in a row
#! way1
# ? print("* " * n)
#! way2
# ? for i in range(n):
# ?     print("*", end=" ")
# ? print()

# todo 2ndQuestion: WAP to print square pattern with '*' symbols
# * * *
# * * *
# * * *
#! way1
# ? for i in range(n):
# ?     print("* " * n)
#! way2
# ? pattern = "*" * n
# ? for i in range(n):
# ?     print(" ".join(pattern))

# todo 3rdQuestion: WAP square pattern with provided fixed digit every row
# n= 3   n=4
# 1 1 1  1 1 1 1
# 2 2 2  2 2 2 2
# 3 3 3  3 3 3 3
#        4 4 4 4
#! way 1
# ?for i in range(n):
# ?    print((str(i + 1) + " ") * n)

# todo 4thQuestion: WAP to print square pattern with alphabet symbols
# n=5
# A A A A A
# B B B B B
# C C C C C
#! way1
# ? alphbet = ord("A")
# ? for i in range(n):
# ?     print((chr(65 + i) + " ") * n)

# todo 5thQuestion: WAP right angle triangle pattern with * symbols
# ?for i in range(n):
# ?    print("* " * (i + 1))
