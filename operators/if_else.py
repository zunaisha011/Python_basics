# age=19
# if age>18:
#     print('allowed')
# print('Not allowed')


# marks=85
# if marks>=85:
#     print('A+ grade')
# else:
#     print('Belowv A+')


# marks=85
# if marks==100:
#     print('A+ grade')
# elif marks>=50 and marks<=99:
#     print('Normal')
# else:
#     print('Fail')

user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0:
        print("Amount dispensed: ", amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")



# # QUIZ
# # Write a Python program to check if a player Lionel Messi has more than 10 achievements. If the condition is true, print the player's name, sport, and achievements else print does not have more than 10 achievements.

# player_name = "Lionel Messi"
# sport = "Soccer"
# achievements = 7
# if achievements > 10:
#     print(f"{player_name} plays {sport} and has {achievements} achievements.")
# else:
#     print(f"{player_name} does not have more than 10 achievements.")


# # Write a Python program to check if a player belongs to the sport Tennis or has exactly 20 achievements. If the condition is true, print a success message.

# player_name = "Roger Federer"
# sport = "Tennis"
# achievements = 20
# if sport == "Tennis" or achievements == 20:
#     print(f"{player_name} meets the criteria! They play {sport} and have {achievements} achievements.")
# else:
#     print(f"{player_name} does not meet the criteria.")