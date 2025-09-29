# Rock - Paper - Scissor game (^_^)

import random 

choice = 'y'

while(choice == 'y'):
	print(
	'''
	enter 
	
	r for rock
	p for paper 
	s for scissor 
	''')
	game = {"r": "rock" , "p": "paper" , "s": "scissor"}

	r = "rock"
	p = "paper"
	s = "scissor"

	computer = random.choice(['r' , 'p' , 's'])
	you = input("	enter your choice: ")

	print(f"	you choose {game[you]} \n	computer choose {game[computer]}\n")

	if(computer == you):
		print("	it is a draw")
	else:
		if(computer == "r" and you == "s"):
			print("	you loose")
		elif(computer == "r" and you == "p"):
			print("	you win")
		elif(computer == "p" and you == "s"):
			print("	you win")
		elif(computer == "p" and you == "r"):
			print("	you loose")
		elif(computer == "s" and you == "p"):
			print("	you loose")
		elif(computer == "s" and you == "r"):
			print("	you win")
		else:
			print("	something went wrong")
		
	choice = input("enter y for more chance :  \nenter any other key to end:  ")

