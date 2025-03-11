import random

print("Welcome to the food ordering ChatBot.")
name = input("What is your name? ")
age = input("Hello " + name + ", how old are you? ")

print("How may we help you?")
print(" ")
print("Please select one from the following:")

def charity():
    responses = ["Every dollar counts! Thank you so much.", "We appreciate your generosity here at Code2College!", "Thank you for your contribution. We will put your name on the wall!"]
    print(random.choice(responses))

def not_satisfied():
    responses = ["We are so sorry to hear that. We will try to do better.", "Your feedback is so valuable to us! Please write a review and tell us what went wrong.", "We apologize for any inconveniences we caused."]
    print(random.choice(responses))

def leave_review():
    print("We are so happy that you want to leave a positive review!")
    site = input("Please type 'Google', 'Yelp', or 'Facebook': ").strip().lower()
    if site == "google":
        print("Great choice! Leave a review here at www.google.com/reviews")
    elif site == "yelp":
        print("Awesome! Leave a rewview here at www.yelp.com/reviews")
    elif site == "facebook":
        print("Wonderful! Leave a review here at www.facebook.com/reviews")
    else:
        print("You have either inputted the wrong website or did not want to leave a review. Please try again!")
    
print("1. I'd like to donate for your cause!")
print("2. I was not satisfied with my care.")
print("3. I would like to leave a positive review.")
print("4. I would like to speak to your manager.")
print("5. Exit the conversation!")

def main():
    while True:
        choice = input("\nWhat would you like to do? ")
        if choice == "1":
            charity()
        elif choice == "2":
            not_satisfied()
        elif choice == "3":
            leave_review()
        elif choice == "4":
            print("I understand. They will be with you shortly.")
        elif choice == "5":
            print("Goodbye " + name + ", I hope you have enjoyed your stay!")
            break
        else:
            print("Invalid choice. Please pick a different option.")

main()