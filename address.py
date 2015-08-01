

d ={}

def address():

	print"hi i'm your address book."

	print"""	1-open address book
	2-add entry
	3-remove entry
	4-store address book
	5-view address book name,alphabetically
	6-view address book email,alphabetically
	7-search email addresses
	8-search names
	9-search names and emails
	10-quit"""
	
	print "you always have to pick the number 1 if you pick 2 and 4"
	print"please pick a number"
	answer = (raw_input())
	if answer == "1" or answer == "2" or answer == "10" or answer == "4" or answer == "5" or answer == "6":
		answer = int(answer)
	
	if answer > 10:
		print"pick a number less then 11"
		address()
	elif answer == 1:
		global dog
		global file
		print".csv at the end of the file name"
		print"please enter a file name"
		file = raw_input()
		dog = open(file,"w+")
		address()
	elif answer == 2:
		
		print"please enter the name of the person"
		name = raw_input()
		print"please enter there email"
		email = raw_input()
		dog.write(name)
		dog.write(",")
		dog.write(email)
		

		for line in dog:
			keyval = line.split(",")
			d[keyval[0]] = keyval[1]
		print d
		dog.close()

		
		address()
		
	elif answer == 4:
		print"please enter the name of the person"
		name = raw_input()
		
		address()
	
	elif answer == 5:
		list = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
		list.sort()
		print list
		print """ |-----------------------------------------|
				  |				       |			   	    |
				  |-----------------------------------------|
				  |				       |                    |
				  |-----------------------------------------|
				  |				       |                    |
				  |-----------------------------------------|
				  |			    	   |                    |	
				  |-----------------------------------------|
				  |				       |                    |
				  |-----------------------------------------|      
				  |				       |                    |
				  |-----------------------------------------|
				  |				       |                    |  
				  |-----------------------------------------|
				  |				       |                    |
				  |-----------------------------------------|
				  |				       |                    | 
				  |-----------------------------------------|
				  |				       |	     		    |
				  |-----------------------------------------| 
				  |				       |                    |
			   	  |-----------------------------------------| 
				  |				       |                    |        
				  |-----------------------------------------|         
				  |				       |                    |                  
				  |-----------------------------------------|  
				  |				       |                    |                  
				  |-----------------------------------------|                          
				  |				       |                    |                                       
				  |-----------------------------------------|                                        
				  |				       |                    |                   
			      |-----------------------------------------|                       
				  |				       |                    |                               
				  |-----------------------------------------|                    
				  |				       |                    |                         
				  |-----------------------------------------|                           
				  |				       |                    |                           
				  |-----------------------------------------|                               
				  |				       |                    |                                 
				  |-----------------------------------------|                          
				  |				       |                    |                             
				  |-----------------------------------------|                             
				  |				       |                    |                              
				  |-----------------------------------------|                            
				  |				       |                    |                                                
				  |-----------------------------------------|          
				  |				       |                    |                     
				  |-----------------------------------------|                          
				  |				       |                    |                                                     
				  |-----------------------------------------|                        
				  |				       |                    |                         
				  |-----------------------------------------| """           	      
	elif answer == 6:
		print "not done"
	
	elif answer == 10:
		print 'Good bye.'

address()