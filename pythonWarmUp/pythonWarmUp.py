"""
	Ken Amamori
	CS4375 - OS
	Python Warm UP
"""

def response(cur, inp):
	print("System:\t", end="")
	if cur == 0:
		if inp == "female":
			print("How excellent! Are you a CS major?")
		elif inp == "male":
			print("Me too. Are you CS major?")
		else:
			print("Great! Anyways, are you CS major?")
	elif cur == 1:
		if inp == "no":
			print("Too bad. Anyway, what's an animal you like, and two you don't?")
		elif inp == "yes":
			print("Excellent, I am too. What's an animal you don't like, and two you don't?")
		else:
			print("Cool! By the way, what's an animal you like, and two you don't?")
	else:
		print(inp[0].strip(), "awesome, but i hate", inp[-1].strip(), "too. Bye for now.")
	return cur+1

def importFromFile():
	print("System:\tHello, are you male or female?")
	f = open('testFile3.txt', 'r')
	lines = f.readlines()
	c = 0
	for line in lines:
		print("User:\t", end="")
		if c == 2:
			print(line)
			response(c, line.split(','))
		else:
			print(line, end="")
			response(c, line)
		c+=1

def userEntering():
	cur = 0
	print("System:\tHello, are you male or female?")
	while cur<3:
		print("User:\t", end="")
		inp = input()
		if "," in inp:
			inp = inp.split(',')
		cur = response(cur, inp)

def main():
	print("Hello, welcome to chatbot program.")
	checker = True
	while(checker):
		print("Are you importing messages from file?")
		print("Enter only either \"yes\" or \"no\".")
		message = input()
		if message == "yes":
			importFromFile()
			checker = False
		elif message == "no":
			userEntering()
			checker = False
		else:
			print("Please enter in the correct format...\n")


if __name__ == '__main__':
	main()

