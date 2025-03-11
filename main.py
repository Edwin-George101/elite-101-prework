import random

print("Welcome to the food ordering ChatBot.")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

print("How may we help you?")
print(" ")
print("Please select one from the following:")

def charity():
    responses = ["Every dollar counts! Thank you so much.", "We appreciate your generosity here at Code2College!", "Thank you for your contribution. We will put your name on the wall!"]
    print(random.charity(responses))

print("1. I'd like to donate for your cause!")
print("2. I was not satisfied with my care.")
print("3. I would like to leave a positive review.")
print("4. I would like to speak to your manager.")
print("5. Exit the conversation!")

while True:
    choice = input("\nWhat would you like to do? ")
    if choice == "1":
        charity()
    elif choice == "2":
        print("What can we do to make things better?")
    elif choice == "3":
        print("Thank you so much! ")
    elif choice == "4":
        print("I understand. They will be with you shortly.")
    elif choice == "5":
        print("Goodbye " + name + ", I hope you have enjoyed your stay!")
        break
    else:
        print("Invalid choice. Please pick a different option.")
