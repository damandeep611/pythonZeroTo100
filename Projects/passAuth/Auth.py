import stdiomask

mongo_db = {"dev": "dam", "git": "shr"}
username_input = input("Enter you registered Username: ")
user_password = stdiomask.getpass("Enter you userPassword: ")

if username_input not in mongo_db:
  print("Erro: Username not found. Please try again.")
else: 
  user_password = stdiomask.getch("Enter you password: ")
  while user_password != mongo_db.get(username_input):
    user_password = stdiomask.getpass("Incorrect Password. Enter you password again")

print("User verified")





