query = str(input("Do you write code? "))
query = query.strip() # to ignore any white spaces created by the user. 
query = query.split()[0] # to read only the first word.
if query.lower() in ['yes', 'yeah', 'definitely']: # to convert the inputs to lowercase
    name = str(input(" Hi, My name is Timmo and I Succesful joined your friends list!! \n What's your name? "))
    print("It was a pleasure meeting you "+ name)
else:
    print(" Timmo left the chat!")
    quit()
