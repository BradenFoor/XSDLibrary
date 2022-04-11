import pickle

#lu stands for Last Updated ;)
lu = "4/7/2022"

#If this is the first time running do not tag below
users = ['Default']
pickle.dump(users, open("users.dat", "wb"))

def main():

    #users = pickle.load(open("users.dat", "rb"))
    separator = ', '

    #print("Loaded Users: " + separator.join(users))

    def userLoop():
        
        option = input("Type A to add a user or R to remove a user: ")

        def userAdd():
            users = pickle.load(open("users.dat", "rb"))

            getuser = input("Enter a usersname to add one: ")

            users.append(getuser.lower())

            pickle.dump(users, open("users.dat", "wb"))

            users = pickle.load(open("users.dat", "rb"))

            print("Loaded Users: " + separator.join(users))

        def userRemove():
            users = pickle.load(open("users.dat", "rb"))
            
            removeuser = input("Enter a username to remove one: ")
            
            userIndex = users.index(removeuser.lower())
            users.pop(userIndex)

            pickle.dump(users, open("users.dat", "wb"))

            users = pickle.load(open("users.dat", "rb"))

            print("Loaded Users: " + separator.join(users))
            
        if option == "A" or option == "a":
            userAdd()
        elif option == "R" or option == "r":
            userRemove()

        return userLoop()

    print('\n\nWelcome to the XS\'D Library System Version(0.01) :)')
    print("Created By: Braden Foor\n")
    print("Last Updated: " + lu + "\n\n")
    users = pickle.load(open("users.dat", "rb"))
    print("Loaded Users: " + separator.join(users))

    userLoop()
main()
