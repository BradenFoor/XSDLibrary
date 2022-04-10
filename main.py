import pickle

#lu stands for Last Updated ;)
lu = "4/7/2022"

#If this is the first time running do not tag below
#users = ['Default']
#pickle.dump(users, open("users.dat", "wb"))

def main():

    #users = pickle.load(open("users.dat", "rb"))
    separator = ', '

    #print("Loaded Users: " + separator.join(users))

    def userLoop():

        def userAdd():
            users = pickle.load(open("users.dat", "rb"))

            getuser = input("Enter a users name to add one: ")

            users.append(getuser)

            pickle.dump(users, open("users.dat", "wb"))

            users = pickle.load(open("users.dat", "rb"))

            print("Loaded Users: " + separator.join(users))

        userAdd()


        return userLoop()

    print('\n\nWelcome to the XS\'D Library System Version(0.01) :)')
    print("Created By: Braden Foor\n")
    print("Last Updated: " + lu + "\n\n")
    users = pickle.load(open("users.dat", "rb"))
    print("Loaded Users: " + separator.join(users))

    userLoop()
main()