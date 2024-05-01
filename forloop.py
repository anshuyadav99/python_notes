#for loop

'''for x in range(1,21):
	print(x)'''

#print number from 1 to 100 
'''for x in range(1 , 101):
	print(x,end=" ")
#print number from 200 to 250 in horizontally
for x in range (200 , 251):
	print(x,end=" ")
#print all even number between 20 to 50
for x in range (20,51):
	if x%2==0:
		print(x)
		#or 
for x in range (20,51,2):
	print(x)
#print back counting from 50 to 1
#range :- (staringpoint,end point,step size)
for x in range (50,0,-1):
	print(x)'''


#print the nuber wuth the help of user input
'''x=int(input("entre the number:-"))
for x in range (10,x,-1):
	print(x)'''


#print the leap year
'''c=0
for i in range (1947,2025):
	if i%4==0:
		print("leap year",i)
		c=c+1
print(c)'''

#print even number
'''for i in range(20,40):
	if i%2==0:
		print(i,end=" ")'''

#table
'''x=int(in*+ put("entre the number:-"))
for i in range(1,11):
	print(i*x)'''

#write the python program with thr help of user input to show the factorial of any number
'''x=int(input("write the  number:-"))
y=1
for i in range(1,x+1):
	y=y*i
print(y)
'''


#print the reverse counting from 50 to 10
'''for i in range (50,9,-1):
	print(i)'''
#100 to 50 step size 5
'''for i in range(100,49,-5):
	print(i)'''


#x="himachal pardesh"
'''for i in x:
	print(i,end="")'''
'''import time
for i in range(11):
	print(i)
	time.sleep(0.1)'''


'''for i in range (30,0,-1):
	print(i,end="\r")
	time.sleep(1)'''




'''print("hello\tworld") #tab
print("hello\nworld") #new line
print("hello\rworld") #replace'''

#print the each alphabets of "hello world" with the help of the loop
'''x="hello world"
for i in x:
	print(i)

x="hello world"
for i in range(10):
	print(x)'''

#continue and break in for loop


'''for i in range(4,21):
	if i%5==0 or i%10==0:
		continue
	else:
		print(i)'''

'''for i in range(4,51):
	if i%5==0 or i%10==0:
		pass
	else:
		print(i)'''

#count  the even number 1 to 20
'''y=0
for x in range(1,21):
	if x%2==0:
		y=y+1
print(y)
'''
#find the sum of 1 10 number
'''x=0
for i in range(1,11):
	x=x+i
print(x)'''

#sum of 10 even number
'''x=0
for i in range(1,21):
	if x%2==0:
		x=x+i
print(x)'''

#count the total number from 10 to 30 who is divisible of 2 and 3
'''x=0
for i in range(10,31):
	if i%3==0 and i%2==0:
		x=x+1
print(x)'''

'''x="india123@#$"
for i in x:
	if i.isdigit():
		break
	print(i)'''


#string function
'''x="Himachal pardesh"
for i in x:
	if i=="a":
		print(i)'''

#find the index with the text

'''x="anshu"
z=len(x)
for i in range(z):
	print(x[i],i)'''

x="himachal pardesh"
z=len(x)
for i in range(z):
	print(x[i],i,i-z)


'''x="anshu"
z=len(x)
for i in range(z):
	if x[i]=="s":
		print(x[i],i)'''


#count the total number of alphabets

'''x="data123science@#$4"
y=0
for i in x:
	if i.isalpha():
		y = y + 1
print(y)'''


#count total number of digit
'''x="data123science@#$4"
y=0
for i in x:
	if i.isdigit():
		y = y + 1
print(y)'''

#count special character
'''x="data123science@#$4"
y=0
for i in x:
	if i.isalnum():
		continue
	else:
		y = y + 1
print(y)'''


'''x="Anshu966@#$%"
a=0
b=0
c=0
for i in x:
	if i.isalpha():
		a=a+1
	elif i.isdigit():
		b=b+1
	else:
		c=c+1
print("alphabets:-",a)
print("digit:-",b)
print("special character:-",c)'''





'''reverse the string
x="hello"
for i in reversed(x):
	print(i)'''

