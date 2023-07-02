
import math
''' This module provides demo data'''

supermarket={
    'store1':{
        'name':'Durga general store',
        'items':[
                {'name':'soap','quantity':20},
                {'name':'brush','quantity':30},
                {'name':'pen','quantity':40}
        ]
    },
    'store2':{
        'name':'Rohith Book store',
        'items':[
                {'name':'python','quantity':100},
                {'name':'django','quantity':200},
                {'name':'java','quantity':300}
        ]
    }
}





from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
numbers='0123456789'
cities=['Hyderabad','Chennai','Banglore','Pune','Delhi','Mumbai']
designations=['Software Engineer','Senior Software Engineer','Team Lead','Project Lead','Project Manager']


def get_fake_name():
    name=choice(alphabets).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(alphabets)
    return name

def get_fake_empid():
    empid='E-'
    for i in range(4):
        empid=empid+choice(numbers)
    return empid

def get_fake_salary():
    esal=uniform(10000,50000)
    return esal

def get_fake_city():
    city=choice(cities)
    return city

def get_fake_mobilenumber():
    mobileno=choice('6789')
    for i in range(9):
        mobileno=mobileno+choice(numbers)
    return mobileno

def get_fake_designation():
    designation=choice(designations)
    return designation

#for i in range(11):
#    print('Employee Details ')
#    print(f'Employee Name : {get_fake_name()}')
#    print(f'Employee Id : {get_fake_empid()}')
#    print(f'Employee Salary : {get_fake_salary()}')
#    print(f'Employee City : {get_fake_city()}')
#    print(f'Employee mobilenumber :{get_fake_mobilenumber()}')
#    print(f'Desgination : {get_fake_designation()}')
#    print()
    

class Movie:
    '''This class is developed by me for demo purpose'''
    def __init__(self,title,hero,heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine
    
    def movieInfo(self):
        print('Movie Name :', self.title)
        print('Hero Name :', self.hero)
        print('Heroine Name :', self.heroine)

moviesList=[]
while True:
    title=input('Enter Movie name :')
    hero=input('Enter movie Hero name : ')
    heroine=input('Enter movie Heroine name :')
    m=Movie(title,hero,heroine)
    moviesList.append(m)
    print('Movie details inserted successfully')
    flag=input('Do you want to store more movies details [Yes/No]')
    if flag.lower()=='no':
        break

print()
print()
print(':'*10+'All movie details'+':'*10)
for movie in moviesList:
    movie.movieInfo()
    print()
