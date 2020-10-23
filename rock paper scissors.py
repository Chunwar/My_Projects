import random
global x
global y
global com_score
global player_score
x = ""
y = ""
com_score = 0
player_score = 0

def results():
	print("Computer picked ", x,"and You picked",  y)
	print()

def play ():
	global x
	global y
	global com_score
	global player_score
	for i in range(5):
		player = input("enter your choice: \n 1 for rock \n 2 for paper \n 3 for scissors\n")
	
		if player == "1":
			y = ("rock")
			# print("you pick :", y)
		elif player == "2":
			y = ("paper")
			# print("you pick :", y)
		elif player == "3":
			y = ("scissors")
			# print("you pick :", y)
		else:
			print("Pagle, Enter a valid choice i.e. a number from 1 to 3. \n You LOST one point. ready for next......")
			y = ""
			com_score += 1	

		computer = random.randrange(1, 4)
		if computer == 1:
			x = ("rock")
		elif computer == 2:
			x = ("paper")
		elif computer == 3:
			x = ("scissors")

		if x  == y:
			results()
			print("Draw, both You and Computer are winners")
			com_score += 1
			player_score += 1
		elif x == "rock" and y == "paper":
			results()
			print("You are the winner")
			player_score +=1
			print()
		elif x == "rock" and y == "scissors":
			results()
			print("Computer is winner")
			com_score +=1
			print()
		elif x == "paper" and y == "rock":
			results()
			print("Computer is winner")
			com_score += 1
			print()
		elif x == "paper" and y == "scissors":
			results()
			print("You are the winner")
			player_score +=1
			print()
		elif x == "scissors" and y == "rock":
			results()
			print("You are the winner")
			player_score += 1
			print()
		elif x == "scissors" and y == "paper":
			results()
			print("Computer is the winner")
			com_score +=1
			print()
	print("Final Score: ", "Computer's Score: ",  com_score, "and Your's Score: ", player_score)






print("Enter your name: ")
name = input().title()
print("hello,", name,"welcome to the 'Rock-Paper-Scissors' Game")
print("------------------------------------------------------")
print("Do you want to play yes or no")
start = input().upper()

if start == "YES":
	print("You have total five chances")
	print()
	
	play()
else:
	print("OK, come some other time to play this game, You COWARD!")



