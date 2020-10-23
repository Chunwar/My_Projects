'''rules 
1. must be 8 character's 
2. at least 1 upper case 
3. at least 1 lower case
4. at least 1 number
5. at least one special charcter
example = Ab1@5678
'''
import random
#creating lists 
number = [0,1,2,3,4,5,6,7,8,9,]
letter  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special = ["[","!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+","<",">","?","/","|","{","}","~",":","]"]
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#generaing random number lower and upper case letter and special character
#generating passworrd containg four random numbers
number2 = random.choice(number)

letter2 = random.choice(letter)

special2 = random.choice(special)

upper2 = random.choice(upper)

password = [number2, letter2, special2, upper2]




#generating another four numbers for the password and creating a list
pwd = []
for i in range(4):
	number3 = random.choice(number)

	letter3 = random.choice(letter)

	special3 = random.choice(special)

	upper3 = random.choice(upper)

	password3 = [number3, letter3, special3, upper3]
	password4 = random.choice(password3)
	pwd.append(password4)


#combining them and shuffling them to create a eight number password
password5 = pwd + password

final = ""
random.shuffle(password5)

for i in password5:
	final += str(i)
print("your password is ", str(final))

