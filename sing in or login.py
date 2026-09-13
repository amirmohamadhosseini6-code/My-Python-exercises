sing_in = input("sing in or login:").lower()
if sing_in == "sing in":
    first_name = input("your first name:").upper()
    last_name = input("your last name:").upper()
    print(f"you singed in wellcome {first_name} {last_name}")
elif sing_in == "login":
    password = input("your password:")
    user_name1 = input("your user name:")
    print(f"welcome {user_name1}")
else:
    print("sorry i dont understand")
exit = input("press enter to exit")



