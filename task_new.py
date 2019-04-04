import random
import time

class Car:
	def __init__(self, model = '', speed = 0):
		self.speed = speed
		self.model = model
	def rand_model(self, model):
		list_models = ['Opel', 'Fiat', 'Suzuki', 'Jeep']
		self.model = random.choice(list_models)
		print("You're driving {}".format(self.model))
	def starting(self, speed):
		self.speed = 10
		print("Stalling the engine. Current speed: {}".format(self.speed))
	def accelerating(self, speed):
		self.speed += 10
		print("Current speed: {}".format(self.speed))
	def slowing_down(self, speed):
		self.speed -= 10
		print("Current speed {}".format(self.speed))
	def stopping(self, speed):
		self.speed = 0
		print("Stopping the car")
	def user_events(self, speed):
		while True:	
			choice = input().upper()	
			if choice == 'L':
				print("Turning left.")
			elif choice == 'R':
				print("Turning right.")
			elif choice == 'K':
				continue
			elif choice == 'D':
				self.slowing_down(self.speed)
			elif choice == 'S':
				self.stopping(self.speed)
				break
			elif choice == 'A':
				self.accelerating(self.speed)
		print("You've got to the destination point.")	
		

def menu():
	print("'L' to turn left")
	print("'R' to turn right")
	print("'K' to keep driving")
	print("'A' to accelerate\n")
	print("'S' to slow down\n")
	print("'S' to stop\n\n")

	
	
def main():
	print("This is simulation of autonomic car.")
	menu()
	
	user_car = Car()
	user_car.rand_model(user_car.model)
	user_car.starting(user_car.speed)
	
	user_car.user_events(user_car.speed)
	
	time.sleep(10)

if __name__ == "__main__":
    main()
