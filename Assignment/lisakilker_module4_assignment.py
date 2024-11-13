#Program that stores data in one file and asks the user to pull up the data store from the main file

#Imports the user file
from user import User

def main():
    #Saves the data into a list
    user_data = []
        
    while True:
        #Asks the user to select A, S, or L.
        user_input = input("Please select A, L, or S: ").strip().upper()
    
        #A response
        if user_input == "A":
            user_id = int(input("Please enter your ID (integer): "))
            
            #Checks for duplicate ID
            if any(user.get_user_id() == user_id for user in user_data):
                print("User ID already exists.")
            else:
                first_name = input("Please enter your first name: ")
                last_name = input("Please enter your last name: ")
                birthday = input("Please enter your birthday (mm/dd/yyyy format): ")
                phone_number = input("Please enter your phone number (xxx-xxx-xxxx format): ")

                #Get/set user from "User" file and prints the user info
                user = User(user_id, first_name, last_name, birthday, phone_number)
                user_data.append(user)
                print("\nUser Info:")
                print(user)

        #L response
        elif user_input == "L":
            print("User info:\n")
            for user in user_data:
                print(user)
                print()
                
        #S response
        elif user_input == "S":
            #Open the file to write to
            with open("info.rtf", 'w') as write_file:
                #Adds a header on the top of the file
                write_file.write("User Info:\n\n")
                #Writes info to file
                for user in user_data:
                    write_file.write(str(user) + "\n\n")
            print("All user data saved to info.rtf. Exiting the program.")
            break
                
        #Forces the user to re-enter a valid option
        else:
            print("That isn't valid. Please try again.")

        #Prints the options for the user to reselect another option
        print("\nOptions:")
        print("A - Add another user")
        print("L - List all users")
        print("S - Save all users in memory and exit")

#Calls the main function
if __name__ == "__main__":
    main()