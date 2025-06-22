# even or odd counter

# even=0
# odd=0
# number=[1,2,3,4,5]
# for i in number:
#     if(i%2==0):
#         even+=1
#     else:
#         odd+=1
# for i in number:
#     print(i)
# print("odd numebers are ",odd,"\n" ,"even numbers are ",even)





# FizzBuzz

# for i in range(1,101):
#     if(i%3==0 & i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")



#factorial

# n=5
# result=1
# for i in range(1,n+1):
#     result*=i
# print(result)



# Plaindrome

# string="ayuya"
# if string==string[::-1]:
#     print("Palindrome")
# else:
#     print("Not A Plaindrome")




# Greatest of Three

# def greatest(a,b,c):
#     return max(a,b,c)
# print(greatest(5,6,7))


# count occurance

# n=[1,2,3,4,3,2,1,1,2,3,4,3,2,1]
# x=3n
# count=0
# for i in n:
#     if i==x:
#         count+=1
# print(count)


#lowest value in the array

# arr=[1,2,3,4,5,6,7,8,9,0]
# min_val=arr[0]
# for i in arr:
#     if i < min_val:
#         min_val=i
        
# print("smallest value is",min_val)      


# class student:
#     def __init__(self, name, rollno):
#         self.name= name
#         self.rollno= rollno
#     def show(self):
#         print(f"Student name is {self.name} and its rollno is {self.rollno}")

# start= student("ayush" , 22)
# start.show()


# x=open("new.txt")
# print(x.read(3))
# x.close

# import os
# if os.path.exists("new.txt"):
#      print("file exists")
# else:
#     print("File doesn't exist")

import os
with open("new.txt","w+") as f:
    f.write("hi there my name is ayush thakur")
    f.seek(0)
    content=f.read()
    print(content)