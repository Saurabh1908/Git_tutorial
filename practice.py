# list1=[1,2,3,4,5,6,7,8]
# list2=[x for x in  list1 if x%2==0]
# print(list2)
#
# x =lambda a,b,c:a*b*c
# print(x(3,4,5))
#
# numbers=[1,2,3,4,5,6]
# even=filter(lambda x: (x% 2 == 0),numbers)
# print(list(even))
#
# list1=[4,5,6]
# list2=[5,6,7]
# result=list(map(lambda x1,x2:x1+x2,list1,list2))
# print(result)

# str=input("Enter the string:")
# i=len(str)-1
# output=''
# while(i>=0):
#     output=output+str[i]
#     i=i-1
# print(output)

# numbers=[2,3,4,5,6,7,8]
# squred_num=map(lambda n:n**2,numbers)
# print(list(squred_num))
#
# list1 = [40,50,60]
# list2 = [2,5,6]
# result = []
# for i in range(0,len(list1)):
#     result.append(list1[i]/list2[i])
# print(result)
#
# numbers=[1, 9, 3, 5, 62, 4, 23]
# numbers.sort()
# print(numbers)

# class Employee():
#     def __init__(self,name):
#         self.name=name
#         print("This is Parametrised constructor")
#     def show(self):
#
#         print("This is",self.name)
#
# emp=Employee("Saurabh")
# emp.show()

# class Employee():
#     def __init__(self):
#         # self.name=name
#         print("This is Non-Parametrised constructor")
#     def show(self,name):
#         self.name=name
#         print("hello!!This is",self.name)
#
# emp=Employee()
# emp.show("Saurabh")

# key=['a',102,'c']
# values=[100,'b',103]
# s=dict(zip(key,values))
# print(s)

# class Car:
#     wheel=4
#     def __init__(self):
#         self.mil=8
#         self.comp='Audi'
#
# c1=Car()
# c2=Car()
# c1.comp='Mercedes'
# print(c1.comp,c1.mil,c1.wheel)

# decimal=int(input("Enter the number:"))
# binary=0
# ctr=0
# temp=decimal
# while(temp>0):
#     binary=(temp%2)*(10**ctr)+binary
#     temp=int(temp/2)
#     ctr+=1
# print(binary)

num=int(input("Enter number:"))
sum=0
temp=num
while(temp>0):
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp=temp//10
if sum==num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
