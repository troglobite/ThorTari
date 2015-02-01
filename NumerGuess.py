repeat = "true"
while repeat == "true":
	guess = raw_input("guess a number (1-10) ")
	if guess == 3:
		print 'correct '
		break
	if guess > 3:
		print 'too high, '
		repeat = raw_input ("repeat? true or false: ")
		if repeat == "false":
			break
	if guess < 3:
		print 'too low, ' 
		repeat = raw_input ("repeat? true or false: ")
		if repeat == "false":
			break		