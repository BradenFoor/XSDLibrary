import pickle

#lu stands for Last Updated ;)
lu = "4/7/2022"



users = ['default']

booksAvailable = ['default']
booksNotAvailable = ['default']

assigned = ['default']

#If this is the first time running do not tag below
pickle.dump(users, open("users.txt", "wb"))
pickle.dump(booksAvailable, open("users.txt", "wb"))
pickle.dump(booksNotAvailable, open("users.txt", "wb"))
pickle.dump(assigned, open("users.txt", "wb"))

def main():

    #users = pickle.load(open("users.txt", "rb"))
    separator = ', '

    #print("Loaded Users: " + separator.join(users))
    
    def searchLoop():
        searchOption = input("\n\nType F to find a book, A to assign a book to a user, U to unassign a book from a user or Q to return: ")
        if searchOption == "Q" or searchOption == "q":
            return taskManage()
            
    def userLoop():
        
        option = input("\n\nType A to add a user, R to remove a user or Q to return: ")

        def userAdd():
            users = pickle.load(open("users.txt", "rb"))

            getuser = input("Enter a usersname to add one: ")

            users.append(getuser.lower())

            pickle.dump(users, open("users.txt", "wb"))

            users = pickle.load(open("users.txt", "rb"))

            print("Loaded Users: " + separator.join(users))

        def userRemove():
            users = pickle.load(open("users.txt", "rb"))
            
            removeuser = input("Enter a username to remove one: ")
            
            userIndex = users.index(removeuser.lower())
            users.pop(userIndex)

            pickle.dump(users, open("users.txt", "wb"))

            users = pickle.load(open("users.txt", "rb"))

            print("Loaded Users: " + separator.join(users))
            
        if option == "A" or option == "a":
            userAdd()
        elif option == "R" or option == "r":
            userRemove()
        elif option == "Q" or option == "q":
            return taskManage()

        return userLoop()
    
    def taskManage():
        task = input("\n\n\nType X to add or remove a new user\nType S to access book information\nType D to access the book log\n")
        if task == "X" or task == "x":
            userLoop()
        elif task == "S" or task == "s":
            searchLoop()

    print('\n\nWelcome to the XS\'D Library System Version(0.01) :)')
    print("Created By: Braden Foor\n")
    print("Last Updated: " + lu + "\n\n")
    users = pickle.load(open("users.txt", "rb"))
    print("Loaded Users: " + separator.join(users))

    taskManage()
main()
