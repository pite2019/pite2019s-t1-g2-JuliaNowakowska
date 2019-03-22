print("This is simulation of autonomic car.")

def menu():
	"""This is what user can do with a car"""
	print("'L' to turn left")
	print("'R' to turn right")
	print("'K' to keep driving")
	print("'S' to stop")
	print("'A' to accelerate\n\n")
		
#Telling user what can he or she do with a car	
menu()

while True:
	#Infinite loop - user is driving	
	print("driving, speed: 50km/h")
	#Asking for input, if user want to make an action
	choice = input().upper()
	
	if choice == 'L':
		print("Turning left.")
	elif choice == 'R':
		print("Turning right.")
	elif choice == 'K':
		continue
	elif choice == 'S':
		#Breaking the loop
		print('Stopping the car')
		break;
	elif choice == 'A':
		print("Accelerating, speed: 60km/h")

#Final message
print("You've got to the destination point.")
