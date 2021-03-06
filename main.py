import pickle

#lu stands for Last Updated ;)
lu = "5/2/2022"



users = ['default']
booksAvailable = ['default']
booksNotAvailable = ['default']
assigned = ['default']

#If this is the first time running do not tag below
pickle.dump(users, open("users.txt", "wb"))
pickle.dump(booksAvailable, open("booksAvailable.txt", "wb"))
pickle.dump(booksNotAvailable, open("booksNotAvailable.txt", "wb"))
pickle.dump(assigned, open("assigned.txt", "wb"))

def main():

    #users = pickle.load(open("users.txt", "rb"))
    separator = ', '

    #print("Loaded Users: " + separator.join(users))
    
    def searchLoop():
        searchOption = input("\n\nType F to find a book, A to assign a book to a user, U to unassign a book from a user or Q to return: ")
        if searchOption == "Q" or searchOption == "q":
            return taskManage()
    
    def logLoop():
        logOption = input("\n\nType A to add a book, or R to remove a book or Q to return: ")
        
        def bookAdd():
            books = pickle.load(open("booksAvailable.txt", "rb"))

            getbook = input("Enter a bookname to add one: ")

            books.append(getbook.lower())

            pickle.dump(books, open("booksAvailable.txt", "wb"))

            books = pickle.load(open("booksAvailable.txt", "rb"))

            print("Loaded Books: " + separator.join(books))

        def bookRemove():
            rbooks = pickle.load(open("booksAvailable.txt", "rb"))
            
            removebook = input("Enter a book to remove one: ")
            
            bookIndex = rbooks.index(removebook.lower())
            rbooks.pop(bookIndex)

            pickle.dump(rbooks, open("booksAvailable.txt", "wb"))

            rbooks = pickle.load(open("booksAvailable.txt", "rb"))

            print("Loaded Books: " + separator.join(rbooks))
            
        if logOption == "Q" or logOption == "q":
            return taskManage()
        elif logOption == "A" or logOption == "a":
            bookAdd()
        elif logOption == "R" or logOption == "r":
            bookRemove()
            
        return logLoop()
            
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
        elif task == "D" or task == "d":
            logLoop()

    print('\n\nWelcome to the XS\'D Library System Version(0.01) :)')
    print("Created By: Braden Foor\n")
    print("Last Updated: " + lu + "\n\n")
    users = pickle.load(open("users.txt", "rb"))
    print("Loaded Users: " + separator.join(users))

    taskManage()
main()
