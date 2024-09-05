# import sys
import random

# Reference list
reflist = [
    [0, 1, -1],
    [-1, 0, 1],
    [1, -1, 0]
]

# Initial input
# flag = int(input("Do you wanna start or stop (1/0): "))
#
# # Main loop
# while flag == 1:
#     print("Game is running...")
#
#     # Placeholder for game logic
#     # You can add your game logic here
#
#     # Update flag to check if the user wants to continue or stop
#     flag = int(input("Do you wanna continue or stop (1/0): "))
#
# else:
#     print("Game stopped!")
#     sys.exit()

#OR

# flag=int(input("Do you wanna start or stop:(1/0): "))
# # while flag==1:
# #     print("Game started!")
# #     inp=int(input("Enter an option outta snake,water and gun (0,1,2): "))
# #     inp1=random.randint(0,2)
# #     print(inp)
# #     print(inp1)
# #     if inp==0 and inp1==0 or inp==1 and inp1==1 or inp==2 and inp1==2:
# #         print("Draw!")
# #         flag = int(input("Do you wanna start or stop:(1/0): "))
# #
# #     elif inp==1 and inp1==0 or inp==0 and inp1==2 or inp==1 and inp1==0 or inp==2 and inp1==1 or inp==0 and inp1==2 or inp==2 and inp1==1:
# #         print("lose!")
# #         flag = int(input("Do you wanna start or stop:(1/0): "))
# #     else:
# #         print("won!")
# #         flag = int(input("Do you wanna start or stop:(1/0): "))
# #
# # print("Game stopped!")


#or

flag = int(input("Do you wanna start or stop (1/0): "))
while flag == 1:
    print("Game started!")
    inp = int(input("Enter an option out of snake, water, and gun (0, 1, 2): "))
    inp1 = random.randint(0, 2)

    print("Your choice:", inp)
    print("Computer's choice:", inp1)

    if reflist[inp][inp1] == 0:
        print("Draw!")
    elif reflist[inp][inp1] == 1:
        print("Won!")
    else:
        print("Lose!")

    flag = int(input("Do you wanna continue or stop (1/0): "))

print("Game stopped!")

#or

# flag = int(input("Do you wanna start or stop (1/0): "))
# while flag == 1:
#     print("Game started!")
#
#     inp = int(input("Enter an option out of snake (0), water (1), and gun (2): "))
#     inp1 = random.randint(0, 2)
#
#     result = reflist[inp][inp1]
#     if result == 0:
#         print(f"Computer chose {inp1}. It's a Draw!")
#     elif result == 1:
#         print(f"Computer chose {inp1}. You Won!")
#     else:
#         print(f"Computer chose {inp1}. You Lose!")
#
#     # Ask if the player wants to continue or stop
#     flag = int(input("Do you wanna continue or stop (1/0): "))
#
# print("Game stopped!")