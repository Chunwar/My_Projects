my_dict = {"a":"1", "b":"2", "c":"3"}
global flag
flag = 0
global name 
name = ""
def name():
	global flag
	print("enter your name")
	global name
	name = str(input())
	for i in my_dict:
		if name == i:
			print("yes")
			flag = 1
			return



			
def password():
	global name
	print("enter password")
	password = str(input())
	for i in my_dict:
		if password == my_dict[name]:
			print("correct password")
			break
		else:
			
			for i in my_dict:
				if password != my_dict[name]:
					print("you have three chances of write correct password")
					
					print("enter password")
					password = str(input())
					if password == my_dict[name]:
						print("right password")
					else:
						print("wrong password")
						print("you have two more chances write the correct password")
						password = str(input())
						if password == my_dict[name]:
							print("right password")
						else:
							print("wrong password")
							password = str(input())
							if password == my_dict[name]:
								print("right password")
							else:
								print("come again later")
								return
def new_name():
	
	print("do you want to create a new user yes or no")
	decision = input().upper()
	if decision == "YES":
		print("ok tell me a user name for the new user")
		new_user = str(input())
		print("tell me a password for the new user")
		new_password = str(input())
		my_dict[new_user] = new_password
		print("your new user has been created \n now you can test your new user name and password")
		global flag
		print("enter your name")
		global name
		name = str(input())
		for i in my_dict:
			if name == i:
				print("yes")
				flag = 1
				password()
				return
	else:
		print("come any other time when you have got your username and password")
		return
name()
if flag == 1:
	password()
else:
	new_name()
