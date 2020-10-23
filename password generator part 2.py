import random
import string
'''
print all chars
test_list = string.printable
print upper & lowercase char
test1 = string.ascii_letters
print nums
test2 = string.digits
print special chars
test3 = string.punctuation
print(test3)
'''
password = []
list_fix =[]

def random_pass(choice):
	global password
	password_char = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
	password = list(''.join(random.choice(password_char) for i in range(choice)))
	return list(password)

def fixed_char():
	global list_fix
	list_fix = list(random.choice(string.ascii_lowercase))
	list_fix += "".join(random.choice(string.ascii_uppercase))
	list_fix += "".join(random.choice(string.digits))
	list_fix += "".join(random.choice(string.punctuation))
	return list(list_fix)
	
choice = input("How many character length password, you need: ")
random_pass((int(choice) - 4))
fixed_char()
pre_final = password + list_fix
random.shuffle(pre_final) 
final = ''
for i in pre_final:
	final += str(i)

print("Your desired", choice, "length password is :", final)