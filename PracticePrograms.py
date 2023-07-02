s = "one two three four five six"
s = s.upper()
# todo 1stQuestion: WAP Reverse the order of every word in the above string
#! way 1
# ? s = s.split()
# ? s.reverse()
# ? final_string = " ".join(s)
# ? print(final_string)

#! way 2
# ? s = s.split()
# ? s.reverse()
# ? print(s)
# ? final_string = ""
# ? for i in s:
# ?     final_string = final_string + " " + i
# ? print(final_string)

#! way 3
# ? s = s.split()
# ? l = len(s) - 1
# ? final_string = ""
# ? while l >= 0:
# ?     final_string = final_string + " " + s[l]
# ?     l = l - 1
# ? print(final_string.strip())

#! way 4
# ? s = s.split()
# ? s = s[::-1]
# ? final_string = ""
# ? print(s)
# ? for i in s:
# ?     final_string = final_string + " " + i
# ? print(final_string)

##! way 5
# ? s = s.split()
# ? s = s[::-1]
# ? final_string = " ".join(s)
# ? print(final_string)


# todo 2ndQuestion: WAP to reverse internal content of each word
#! way 1
# ? s = s.split()
# ? final_string = ""
# ? for i in s:
# ?     final_string = final_string + " " + i[::-1]
# ? print(final_string)

#! way 2
# ? s = s.split()
# ? l = []
# ? for i in s:
# ?     l.append(i[::-1])
# ? s = " ".join(l)
# ? print(s)

#! way 3
# ? words = s.split()
# ? l = []
# ? for word in words:
# ?     l.append("".join(reversed(word)))
# ? print(" ".join(l))

#! way 4
# ? words = s.split()
# ? finalString = ""
# ? for word in words:
# ?     i = ""
# ?     for j in range(len(word)):
# ?         i = i + word[len(word) - j - 1]
# ?     finalString = finalString + i + " "
# ? print(finalString)

# todo 3rdQuestion: WAP to reverse internal content of every 2nd word of given string

# ? s = s.split()
# ? l = []
# ? final_string = ""
# ? for i in range(len(s)):
# ?     if i % 2 == 0:
# ?         l.append(s[i])
# ?     else:
# ?         l.append(s[i][::-1])
# ? s = " ".join(l)
# ? print(s)

#! way 2
# ? words = s.split()
# ? l = []
# ? for i in range(len(words)):
# ?     if i % 2 == 0:
# ?         l.append(words[i])
# ?     else:
# ?         l.append("".join(reversed(words[i])))
# ? print(l)

#! way3
# ? words = s.split()
# ? l = []
# ? for i in range(len(words)):
# ?     newWord = ""
# ?     if i % 2 == 0:
# ?         l.append(words[i])
# ?     else:
# ?         j = 0
# ?         for k in range(len(words[i])):
# ?             newWord = newWord + words[i][len(words[i]) - k - 1]
# ?         l.append(newWord)
# ? print(" ".join(l))

# todo 4thQuestion: WAP to print characters present at even index and odd index seperately for the given string
s = "sindiri rohith"
s = s.upper()
#! way 1
# ? odds = []
# ? evens = []
# ? for i in range(len(s)):
# ?     if i % 2 == 0:
# ?         evens.append(s[i])
# ?     else:
# ?         odds.append(s[i])
# ? print("Odd position letters :", odds)
# ? print("Even position letters :", evens)


#! way 2
# ? print("Letters present at even position : ")
# ? i = 0
# ? while i < len(s) - 1:
# ?     print(s[i])
# ?     i = i + 2
# ? print("Letters present at odd position : ")
# ? i = 1
# ? while i < len(s):
# ?     print(s[i])
# ?     i = i + 2

#! way 3
# ? print('Characters present at Even Index : ',s[0::2])  #!sindiri rohith
# ? print('Characters present at Odd Index : 's[1::2])  #!sindiri rohith

# todo 5thQuestion: WAP to merge characters of 2 strings into a single string by taking chracters alternatively
# ? s1 = "rohith".upper()
# ? s2 = "preethi".upper()
# ? i, j = 0, 0
# ? output = ""
# ? while i < len(s1) and j < len(s2):
# ?     output = output + s1[i] + s2[j]
# ?     i = i + 1
# ?     j = j + 1
# ? if i < len(s1):
# ?     output = output + s1[i]
# ?     i = i + 1
# ? if j < len(s1):
# ?     output = output + s2[j]
# ?     j = j + 1
# ? print(output)
# todo 6thQuestion: WAP to Sort characters of the string,first alphabets followed by digits
#! input=B4A1D3 output=ABD134
# s = "B4A1D3"
s = "R76o9h6i3t5h8".upper()
#! Way 1
# ? print(s)
# ? alpha = "abcdefghijklmnopqrstuvwxyz".upper()
# ? digits = "1234567890"
# ? letters = []
# ? numbers = []
# ? for i in s:
# ?     if i in alpha:
# ?         letters.append(i)
# ?     if i in digits:
# ?         numbers.append(i)
# ? letters.sort()
# ? numbers.sort()
# ? output = "".join(letters) + "".join(numbers)
# ? print(output)

#! way 2
# ? letters = []
# ? numbers = []
# ? for i in s:
# ?     if i.isalpha():
# ?         letters.append(i)
# ?     if i.isdigit():
# ?         numbers.append(i)
# ? output = "".join(sorted(letters) + sorted(numbers))
# ? print(output)

# todo 7thQuestion WAP for the following requirement
#! input=a4b3c2
#! ouput=aaaabbbcc (a fourtimes,b threetimes,c 2times)
#! input = "a4b3c2"
#! output = ""
#! for i in input:
#!     if i.isalpha():
#!         x = i
#!     if i.isnumeric():
#!         output = output + (x * int(i))
#! print(output)
#! print(i)
#! print(x)

# todo 8thQuestion WAP for the requirement input aaaabbbccz and output 4a3b2c1z
#! way1
# input = "AAABBBBCCZZZ"
# output = "3A4B2C1Z"
# ? l = sorted(set(input))
# ? finalStr = ""
# ? for i in l:
# ?     if i in input:
# ?         finalStr = finalStr + str(input.count(i)) + i
# ? print(finalStr)

#! way2
# ? previous = input[0]
# ? count = 1
# ? finalStr = ""
# ? for i in range(1, len(input)):
# ?     if previous == input[i]:
# ?         count = count + 1
# ?     else:
# ?         finalStr = finalStr + str(count) + previous
# ?         previous = input[i]
# ?         count = 1
# ?     if i == len(input) - 1:
# ?         finalStr = finalStr + str(count) + previous
# ? print(finalStr)

# todo 9thQuestion WAP for the follwoing requirement
input = "a4k3b2"
output = "aeknbd"  #! a+4=e k+3=n b+2=d

#! way 1

# ? finalStr = ""
# ? for ch in input:
# ?     if ch.isalpha():
# ?         x = ch
# ?         finalStr = finalStr + ch
# ?     else:
# ?         finalStr = finalStr + chr(ord(x) + int(ch))
# ? print(finalStr)

# todo 10thQuestion WAP to remove duplicate characters from the given input string
input = "AZZBCDABBCDABBCCCCDDEEEF"
output = "AZBCDEF"
#! Way 1
# ? input = "".join(set(input))
# ? print(input)

#! Way 2
# ? finalStr = ""
# ? for ch in input:
# ?     if ch not in finalStr:
# ?         finalStr = finalStr + ch
# ? print(finalStr)

#! way 3
# ? l = list(set(input))
# ? print("".join(sorted(l)))

# todo 11thQuestion: WAP to find the no.of occurences of each character present in a string
# input = "AZZBCDABBCDABBCCCCDDEEEF"
#! way1
# ?  char_cnt = {}
# ?  for ch in input:
# ?     if ch not in char_cnt:
# ?         char_cnt[ch] = 1
# ?     else:
# ?         char_cnt[ch] = char_cnt.get(ch) + 1
# ? # for key, val in char_cnt.items():
# ? #    print(f"char:{key} count :{val}")
# ?  for key in sorted(char_cnt):
# ?     print(f"char:{key} count :{char_cnt.get(key)}")

#! way2
# ?  l = sorted(set(input))
# ?  for ch in l:
# ?     print(f"char:{ch} count:{input.count(ch)}")

#! way3
# ? l = []
# ? for ch in input:
# ?     if ch not in l:
# ?         l.append(ch)
# ? for ch in sorted(l):
# ?     print(f"char:{ch} count:{input.count(ch)}")

#! way4
# ? char_cnt = {}
# ? for ch in input:
# ?     char_cnt[ch] = char_cnt.get(ch, 0) + 1
# ? for key, val in sorted(char_cnt.items()):
# ?     print(f"char:{key} count :{val}")

# todo 12thQuestion: WAP for the following requirement
# input = "AZZBCDABBCDABBCCCCDDEEEF"
# ? char_cnt = {}
# ? output = ""
# ? for ch in input:
# ?     char_cnt[ch] = char_cnt.get(ch, 0) + 1
# ? for key, val in sorted(char_cnt.items()):
# ?     # print(val, key, sep="", end="")
# ?     output = output + str(val) + key
# ? print(output)

# todo 13thQuestion:WAP to find no.of occurences of each vowel in the given string
#! way 1
# ? input = "Want to be a DataEngineer".lower()
# ? l = ["a", "e", "i", "o", "u"]
# ? for ch in l:
# ?     if ch in input:
# ?         print(f"char :{ch} and count: {input.count(ch)}")
# ?     else:
# ?         print(f"char :{ch} and count: 0")

#! way2
# ? input = "Want to be a DataEngineer".lower()
# ? l = ["a", "e", "i", "o", "u"]
# ? vow_cnt = {}
# ? for ch in input:
# ?     if ch in l:
# ?         vow_cnt[ch] = vow_cnt.get(ch, 0) + 1
# ? for key, val in sorted(vow_cnt.items()):
# ?     print(f"char :{key} count:{val}")

# todo 14thQuestion: WAP to check whether given two strings are anagrams or not
#! heart -- earth
#! knee -- keen
#! triangle -- integral
#! silent -- listen

#! Way1
# s1 = "triangle"
# s2 = "integral"
# ? print(sorted(s1) == sorted(s2))

#! Way2
# ? from collections import Counter as c
# ? print(c(s1) == c(s2))

# todo 15thQuestion: WAP to check whether the given string is Palindrome or not
#! eye eye
#! malayalam malayalam
#! wow wow
#! refer refer
#! radar radar
