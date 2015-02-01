response = None
answer = 3
while response != ' correct ':
	guess = int(raw_input("guess a number (1-10) "))
	if guess > answer:
		response = ' too high '	
	elif guess < answer:
		response = ' too low '
	else:
		response = ' correct '
	print response