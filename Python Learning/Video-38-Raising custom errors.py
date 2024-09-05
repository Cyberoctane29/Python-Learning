# a1=int(input("Enter number between 5 and 9:"))
# if(a1<5 or a1>9):
#    raise ValueError("Value should be between 5 and 9!")
#
# #or
# try:
#    a2=int(input("Enter number between 5 and 9:"))
#    if(a2<5 or a2>9):
#      raise ValueError("Value should be between 5 and 9!")
# except ValueError as ve:
#     print(f"invalid!{ve}")
#
# print("End of program")

# Exception Propagation:

# When the ValueError is raised, Python immediately stops executing the code within the try block and starts looking for
# an except block that matches the type of the exception.

# Handling the Exception:

# Python finds the except ValueError as ve block. This block is designed to catch exceptions of type ValueError.
# The exception object (ve) contains the message and other details about the ValueError that was raised.

# Exception Handling:

# The except block catches the ValueError raised by either the int() conversion or the explicit raise statement.
# The message associated with the ValueError ("Value should be between 5 and 9!" or a message from the failed integer conversion)
# is printed by print(f"An error occurred: {ve}").

# try:
#     a1 = input("Enter a number between 5 and 9 or type 'quit' to exit: ") #.strip(optional)
#     if a1.lower() == "quit":
#         print("User has terminated the program!")
#         exit()
#
#     # Convert the input to an integer after ensuring it's not "quit"
#     a1 = int(a1)
#
#     if a1 < 5 or a1 > 9:
#         raise ValueError("Value should be between 5 and 9!")
# except ValueError as ve:
#     print(f"Invalid input: {ve}")
#
# print("End of program")

while True:
    input_ = input("enter a number between 7 and 15 (enter q or quit): ").lower()
    if input_ == "q" or input_ == "quit":
        print("thank you")
        break
    try:
        num = int(input_)
        if 7 <= num <= 15:
            print(f"the answer is {num}")
        else:
            print("the number should be between 7 and 15")
    except ValueError:
        print("you did not entered a valid number")

    finally:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing.")
            break
        print("Let's play again!\n")

