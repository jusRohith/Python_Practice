#There are 6 types of Inheritance are there
# 1.Single Inheritance      2.Multi level Inheritance
# 3.Hierarchical            4.Multiple   
# 5.Hybrid                  6.Cyclic

# 2.Mutilevel Example
class P:
    def m1(self):
        print('Parent Method')
class C(P):
    def m2(self):
        print('Child Method')
class CC(C):
    def m3(self):
        print('Subchild Method')
obj=CC()
obj.m1()
obj.m2()
obj.m3()
print('*'*15+'Mutilevel Example Ends Here'+'*'*15)
print()

# 3.Hierarchical Inheritance example:

class Parent:
    def m1(self):
        print('Parent method')
class child1(Parent):
    def child1_m2(self):
        print('Child 1 method')
class child2(Parent):
    def child1_m2(self):
        print('Child 2 method')
c1=child1()
c1.m1()
c1.child1_m2()
print()
c2=child2()
c2.m1()
c2.child1_m2()
print('*'*15+'Hierarchical Inheritance example Ends Here'+'*'*15)
print()

# 4.Multiple Inheritance Example

class Parent1():
    def parent1Method(self):
        print('P1 Method')
    def commonMethod(self):
        print('Common Method in parent 1')
class Parent2():
    def parent2Method(self):
        print('P2 Method')
    def commonMethod(self):
        print('Common Method in parent 2')
class Child(Parent1,Parent2):
    def childMethod(self):
        print('Child Method')
c =Child()
c.parent1Method()
c.parent2Method()
c.childMethod()
c.commonMethod()
#if we have methods with same name in the multiple parent methods based on the 
#Arguments of the child class declaration it will be invoked
#kindly check the above example
print('*'*15+'Multiple Inheritance example Ends Here'+'*'*15)
print()