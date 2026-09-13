order = input("(if you new type(help))>")
if order.upper() == "HELP":
    print('''start=start.car
stop=stop.car
quit=to.exit.game''')
elif order.upper() == "START":
        print("car started... ready to go!")
elif order.upper() == "STOP":
        print("car stoped.")
else:
    print("sorry idon't understand")
while order.upper() != "QUIT":
    order = input("(if you new type'help'>")
    if order.upper() == "START":
        print("car started... ready to go!")
    elif order.upper() == "STOP":
        print("car stoped.")
    elif order.upper() == "HELP":
        print('''start=start.car
        stop=stop.car
        quit=to.exit.game''')
    elif order.upper() == "QUIT":
        break
    else:
        print("i don't understand")



