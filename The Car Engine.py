#******PROJECT THE CAR******

#...Our Messages...
started = 'Car Engine On! Ready to go'
stopped = 'Engine Stopped.'
error = "Uh... i don't understand that. Try 'help'"
exit = 'Hope to see you soon.'
help = """Instructions:
start - To start the car.
stop - To stop the car.
help - To display this message.
quit/exit - To exit the game."""

#...Runtime variables...
run = 0
start = 0
stop = 1
print("Tip - try using 'help'")

#...Logic...
while run == 0:
    car_input = input('> ')
    if car_input == "start" and start == 0:
        print(started)
        start += 1
        stop = 0
    elif car_input == "start" and start > 0:
        print("It is on already!")
    elif car_input == "stop" and stop == 0:
        print(stopped)
        stop += 1
        start = 0
    elif car_input == "stop" and stop > 0:
        print("It isn't moving bruh.")
    elif car_input == "help":
        print(help)
    elif car_input == "exit" or car_input == "quit":
        print(exit)
        break
    else:
        print(error)

#------------------------------------------------------


