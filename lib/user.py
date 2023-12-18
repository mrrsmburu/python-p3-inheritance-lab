#!/usr/bin/env python

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


if __name__ == "__main__":
    
    user_instance = User(first_name="John", last_name="Doe")

    
    print(f"First Name: {user_instance.first_name}")
    print(f"Last Name: {user_instance.last_name}")
    pass