#Creates a program with 3 parts

#Main function which contains the 3 lists used in this program
def main():
    #List1 - PART 1
    list1 = ["Red", "Green", "Yellow"]
    #List2 - PART 2
    list2 = [1,2,3,4,5]
    #List3 - PART 3
    list3 = []

    #PART 1
    #Formats the list elements into a single string with commas separating them but no quotation marks
    joined_list1 = ','.join(list1)
    #Prints the formatted string with square brackets
    print(f'[{joined_list1}]')  
    
    #PART 2
    #Loops through the list to display the list as a column
    for item in list2:
        print(item)

    #PART 3
    #Loops through the user input until they've entered something 3 times
    for i in range(3):
        while True:
            input_list3 = input("Please enter a word or number: ")
            
            #Checks if user has entered a character, if not it recalls the input to reask the user
            if input_list3.strip():
                list3.append(input_list3)
                break
            else:
                print("You did not enter anything. Please try again.")
            
    #Removes the quotes from the list
    joined_list3 = ','.join(list3)
         
    #Prints the complete list
    print("This is your list: ", joined_list3)

#Calls the main function
if __name__ == "__main__":
    main()