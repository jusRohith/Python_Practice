#
# ? Question1 : WAP to dictionary from the keyboard and print sum of the values
#! Way1
# d = eval(input("Enter the dictionary to get the sum : "))
# sum = 0
# for val in d.values():
#    sum = sum + val
# print(sum)
#! Way2
# sum = 0
# for item in d.items():  # here items() method returns tuple thats why we use item[1]
#    sum = sum + item[1]
# print(sum)
#! Way3
# print("The sum of dict values : ", sum(d.values()))


# ? Question2: WAP to find no.of.occurences of each letter present in the given string
# s = "AZZBCDABBCDABBCCCCDDEEEF"
# result = {}
#! Way1
# for ltr in s:
#    if ltr not in result:
#        result[ltr] = 1
#    else:
#        result[ltr] = result.get(ltr) + 1
# print(result)
#! Way2
# for ltr in s:
#    result[ltr] = result.get(ltr, 0) + 1
# print(result)
# ? Question3: WAP find the no.of occurences of each vowel present in the given string
# s = "Learning Python is very easy"
# d = {}
# for ch in s:
#    if ch in ["a", "e", "i", "o", "u"]:
#        d[ch] = d.get(ch, 0) + 1
# print(d)
# ?Question4: Write a program that counts the frequency of each word in a given sentence and stores the results in a dictionary. Ignore case sensitivity and punctuation.
# input = "I love to code, and I love to solve problems"
# output = {}
# for word in input.upper().split():
#    if word.isalpha():
#        output[word] = output.get(word, 0) + 1
# print(output)


# ? Question5:Write a function that takes a list of dictionaries as input, where each dictionary represents a student's information (name, age, and grade). The function should return a dictionary with the average grade of each age group.
# Input:
# students = [
#    {"name": "John", "age": 20, "grade": 80},
#    {"name": "Jane", "age": 20, "grade": 90},
#    {"name": "Mike", "age": 22, "grade": 85},
#    {"name": "Sarah", "age": 22, "grade": 95},
# ]
# Output: {20: 85.0, 22: 90.0}
# def cal_avg_grade(students):
#    age_grades = {}
#    avg_age_grades = {}
#    for student in students:
#        age = student["age"]
#        grade = student["grade"]
#        if age not in age_grades:
#            age_grades[age] = [grade]
#        else:
#            age_grades[age].append(grade)
#    print(age_grades)
#
#    for age, grades in age_grades.items():
#        avg_age_grades[age] = sum(grades) / len(grades)
#    print(avg_age_grades)
#
#
# cal_avg_grade(students)
# ? Question6:Write a function that takes a string as input and returns a dictionary containing the count of each vowel (a, e, i, o, u) in the string. Ignore case sensitivity.
# input = "Want to be a DataEngineer".lower()
#
#
# def vowels_count(input: str) -> dict:
#    vowels = ["a", "e", "i", "o", "u"]
#    output = {}
#    for i in input:
#        if i in vowels:
#            output[i] = output.get(i, 0) + 1
#    return output
#
#
# print(vowels_count(input))

# ?Question7:Write a function that takes a dictionary as input, where the keys are student names and the values are their test scores. The function should return the name of the student with the highest score
# input = {"John": 85, "Jane": 92, "Mike": 78, "Sarah": 95}
# Output= "Sarah"


# def getHighScore(student_details: dict[str, int]) -> int:
#! Way1
#    return (
#        list(student_details.keys())[
#            list(student_details.values()).index(max(student_details.values()))
#        ]
#    )
#! Way2
# return "".join(
#    i
#    for i in student_details
#    if student_details[i] == max(student_details.values())
# )
#! Way3
# for k, v in student_details.items():
#    if v == max(student_details.values()):
#        return k
# print(getHighScore(input))

# ? Question8:Write a program that takes two dictionaries as input and merges them into a single dictionary. If there are any common keys, combine their values as a list.
# Input:
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 3, "d": 4}
# output = {}

# Output: {'a': 1, 'b': [2, 3], 'c': 3, 'd': 4}
#! Way1
# for i in dict1:
#    if i in dict2:
#        output[i] = [dict1.get(i), dict2.get(i)]
#    else:
#        output[i] = dict1.get(i)
# for j in dict2:
#    if j not in output:
#        output[j] = dict2.get(j)
# print(output)

#! Way2
# mergedDict = dict1.copy()
# for k, v in dict2.items():
#    if k in mergedDict:
#        mergedDict[k] = [mergedDict[k], v]
#    else:
#        mergedDict[k] = v
# print(mergedDict)

# ? Question8:
input = "Want to be a DataEngineer".lower()
#! Way1
# output = {i: input.count(i) for i in input if not i.isspace()}
#! Way2
# output = {}
# for i in input:
#    if not i.isspace():
#        output[i] = output.get(i, 0) + 1
# print(output)

# ? Question9:
# Input = ["apple", "banana", "cherry"]
# Output: {'apple': 5, 'banana': 6, 'cherry': 6}
# print({word: len(word) for word in Input})

# ? Question10:Write a function that takes a dictionary as input, where the keys are country names and the values are their populations. The function should return the name of the country with the highest population.
# Input = {"USA": 331002651, "China": 1439323776, "India": 1380004385}

## Output: 'China'
# for k, v in Input.items():
#    if v == max(Input.values()):
#        print(k)
# print(list(Input.keys())[list(Input.values()).index(max(Input.values()))])
# ?Question11:
# input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]
# Output: {'even': 5, 'odd': 5}
#! Way1
# output = {}
# for i in input:
#    if i % 2 == 0:
#        output["Even"] = output.get("Even", 0) + 1
#    else:
#        output["Odd"] = output.get("Odd", 0) + 1
# print(output)
#! Way2 using Dict Comprehension
# output = {
#    "Even": len([i for i in input if i % 2 == 0]),
#    "Odd": len([j for j in input if j % 2 != 0]),
# }
# print(output)

# ? Question12:Write a function that takes a list of dictionaries, where each dictionary represents a student's information (name, age, and subjects), and returns a dictionary where the keys are the unique subjects and the values are lists of students who are enrolled in each subject.
sInfo = [
    {"name": "John", "age": 20, "subjects": ["Math", "Physics"]},
    {"name": "Jane", "age": 21, "subjects": ["Physics", "Chemistry"]},
    {"name": "Mike", "age": 20, "subjects": ["Math", "Chemistry"]},
    {"name": "Sarah", "age": 22, "subjects": ["Physics", "Biology"]},
]
# output={'Math': ['John', 'Mike'],'Physics': ['John', 'Jane', 'Sarah'],'Chemistry': ['Jane', 'Mike'],'Biology': ['Sarah']}
stuName = []
output = {}
for element in sInfo:
    #    subjects=[subject for subject in element["subjects"] if subject not in subjects]
    for subject in element["subjects"]:
        if subject not in output:
            output = {subject: stuName.append(element["name"])}
        # else:
        #    output[subject] = [element["name"]]
print(output)


# output = dict.fromkeys(subjects, None)
