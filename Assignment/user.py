#Holds the data of the user
class User:
    def __init__(self, user_id, first_name, last_name, birthday, phone_number):
        self.__user_id = user_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birthday = birthday
        self.__phone_number = phone_number

    #Gets/sets user ID
    def get_user_id(self):
        return self.__user_id
    
    def set_user_id(self, user_id):
        self.__user_id = user_id
    
    #Gets/sets first name
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    #Gets/sets last name
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    #Gets/sets birthday
    def get_birthday(self):
        return self.__birthday
    
    def set_birthday(self, birthday):
        self.__birthday = birthday
    
    #Gets/sets phone number
    def get_phone_number(self):
        return self.__phone_number
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    #Formats to a string
    def __str__(self):
        return f"User ID: {self.__user_id}\n\n{self.__first_name} {self.__last_name}\n\n{self.__birthday}\n\n{self.__phone_number}"