def geet():
    print('hello')
    print('good morning')
#when we run the code we havant got output because of w need to calling function


#calling the geet function
geet()    

geet()

geet()

# function return the multipal argument

def add(a,b,c):
    d=a+b+c
    return d

result=add(12,23,3)
print(result)

# get multipal parameter from function

def mul_agr_return(w,e,r,t):
    f=20+w
    g=30-e
    h=34*r
    d=23/t
    return f,g,h,d

r1,r2,r3,r4=mul_agr_return(23,43,56,34)
print(r1,r2,r3,r4)

print(f"{type(r1)} and   {id(r2)} and {id(r1)}")
   
#function Argument 

def add_sub():
    f=3+2 # get the value from user
    g=3-4
    return f,g
f,d=add_sub()
print(f,d)

#update the function take the value from user

def cal_sub(w,q): # get the value from user
    f=w-q
    return f
g=cal_sub(12,34)
print(g)

#By default in pythin no pass by value and pass by reference 
#--------------------------------------------------------
def update(x):   
    x = 8
    print('x : ', x)    

a = 10
update(a)
print('a : ',a)


# type 2

def update1(a1):
    print(id(a1))
    a1=2
    print(id(a1))
    print('a1',a1)

a1=10
print(id(a1))
update1(a1)
print('a1',a1)

# type 3 using list 

def update2(list):
    print(list)
    list[0]=12
    print(id(list))

list=[1,2,3]
print(id(list))
update2(list)
print('list',list)


def update4(lst):   
    print(id(lst))
    
    lst[1] = 25
    print(id(lst))
    print('x', lst)    

lst = [10,20,30] #lets pass list hear
print(id(lst))
update4(lst)
print('lst',lst)

print('\n')


def modify_integer(x):
    x = 10
    print("Inside function:", x)    
    
my_integer = 5
modify_integer(my_integer)
print("Outside function:", my_integer)

def modify_integer1(x):
    x = 10
    print("Inside function:", x)  
    print('Inside function:',id(x))
    
my_integer = 5
modify_integer1(my_integer)
print("Outside function:", my_integer)
print('Outside function:',id(my_integer))


print('\n')

def modify_list(my_list):
    my_list.append(4)
    print("Inside function:", my_list)

my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

print('\n')

def modify_list1(my_list):
    print("original Inside function:", id(my_list))
    my_list.append(4)
    print("Inside function:", my_list)
    print("Inside function:", id(my_list))

my_list = [1, 2, 3]
modify_list1(my_list)
print("Outside function:", my_list)
print("Outside function:", id(my_list))

#Argument Actual and formal

def add1(a,b,d,e): # a & b called formal argument
    c = a+b+d+e
    print(c)
    
add1(5,6,7,8) #5 and 6 we called as actual argument  

#actual keyword possition 
def person(name,age):
    print(name)
    print(age)
    
person(22,'nit')

print('\n')


#keyword Argument
def person(name,age):
    print(name)
    print(age-5)
    
person(age = 20, name = 'nit') 

def person1(name,age=20): #in this code we expected to print 2 but we got bydefault 
    print(name)
    print(age)
    
person1('nit') 


#variable length
print('\n')

def sum(a, *b): # 1st argument is fixed & we fetch each value from the tuple & we can add them. 
    c = a   
    for i in b:
     c = c + i 
     print(c)       
result=sum(5,6,7,8) 
print(result)

print('\n')

def sum1(a, *b): # 1st argument is fixed but for 2nd argument
   # c = a+sum(b)
    print(f'a is {a} and b is {b}')
    print(type(a))
    print(type(b))

sum1(5,6,7,8) 

#-------------------------------
print('\n')
def mul_para(a,*b):
    c=a
    for s in b:
        c=c+s
        print(f'c is {c}')

mul_para(2,3,4,5,6)


print('\n')

def sum(a, *b): 
    print(a)
    c = 0
    
    for s in b:
           c=c+s
           print(f'c is {c}')
    
sum(5,6,7,8)

#----Keyword variable---------------------------
print('\n')
def person(name,*data):
    print(name)
    print(data)

person('ALEX', 36, 'JOHN', 987767)


print('\n')

#type 2

def person2(name,**data):
    print(name)
    print(data)

person2('ALEX', age = 36, home_place ='southcity', mob =987767)
# we got error as keyword argument thats why we add another *


def person3(name, **data):
    print(name)
    
    for i, j in data.items():
        print(i, j)
        
person3('john', age = 36, home_place ='southcity', mob =987767, place = 'USA')


#anonymous function 
#-------------------


def squre(a):
    return a*a
result=squre(2)

print(result)

#using lambda function

f=lambda a:a*a
result=f(2)
print(result)

#type 2

a1=lambda a,b:a+b
b2=lambda s,d:s+d
r1=a1(2,2)
r2=b2(3,4)
print(r1)
print(r2) 

#type 3
import keyword 
keyword.kwlist

#------------------
def is_even(f):
    return f*f

ff=lambda g:is_even(g)
r3=ff(5)
print(r3)


# type 4



#modules - devide the code in diffrent block


def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

import mymodule

aa=5
bb=22

print(mymodule.sum(aa,bb))
print(mymodule.sub(aa,bb))


