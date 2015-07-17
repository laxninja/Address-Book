def address():

	print"hi i'm your address book."

	print"""1-open address book
	2-add entry
	3-remove entry
	4-store address book
	5-view address book name,alphabetically
	6-view address book email,alphabetically
	7-search email addresses
	8-search names
	9-search names and emails
	10-quit"""
	print"please pick a number"
	anwser = int(raw_input())
	if anwser > 10:
		print"pick a number less then 11"
	
	if anwser == 1:
		print".csv at the end of the file name"

		print"please enter a file name"
		file = raw_input()

		print"please enter the name of the person"
		name = raw_input()

		print"please enter there email"
		email = raw_input()

		dog = open(file,"a")


		dog.write(name)
		dog.write("\n")
		dog.write(email)

		print file

		dog.close()

address()