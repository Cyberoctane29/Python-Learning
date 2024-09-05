quesAns = [
    ["Whats the colour of apple? ", "red", "blue", "green", "grey", 1],
    ["Whats the colour of Banana? ", "yellow", "blue", "grey", "red", 1],
    ["Whats the colour of the sky? ", "blue", "red", "green", "yellow", 1],
["Whats the colour of apple? ", "red", "blue", "green", "grey", 1],
    ["Whats the colour of Banana? ", "yellow", "blue", "grey", "red", 1],
    ["Whats the colour of the sky? ", "blue", "red", "green", "yellow", 1],
["Whats the colour of apple? ", "red", "blue", "green", "grey", 1],
    ["Whats the colour of Banana? ", "yellow", "blue", "grey", "red", 1],
    ["Whats the colour of the sky? ", "blue", "red", "green", "yellow", 1],
["Whats the colour of apple? ", "red", "blue", "green", "grey", 1],
    ["Whats the colour of Banana? ", "yellow", "blue", "grey", "red", 1],
    ["Whats the colour of the sky? ", "blue", "red", "green", "yellow", 1]
]

money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
amt = 0

while True:
    for i in range(0, len(quesAns)):
        question = quesAns[i]
        print(f"Question for Rs.{money[i]}")
        print(question[0])
        print("Options:")
        print(f"1. {question[1]}    2. {question[2]}")
        print(f"3. {question[3]}    4. {question[4]}")

        try:
            ans = int(input("Answer the question (enter option number 1-4): "))
            if ans < 1 or ans > 4:
                raise ValueError("Invalid option!")
                if amt!=0:
                    amt-=money[i-1]
        except ValueError:
            print("Invalid option! Please enter a number between 1 and 4.")
            continue

        # Check if the answer is correct immediately after receiving it
        if ans == question[-1]:
            print("Correct Answer!")
            print(f"You won Rs.{money[i]}")
            amt += money[i]  # Update amount won based on current question
            if i == 4:
                amt = 10000
            elif i == 9:
                amt = 320000
            elif i == 14:
                amt = 10000000
        else:
            print("Wrong Answer!")
            break  # End game if the answer is wrong

    o = input("Do you want to play again? (yes/no): ").lower()
    if o == "no":
        break

print(f"Total amount you won: Rs.{amt}")

#bugs: if the person puts an invalid option after a question or in the first question the amount is still being added,
# ig I need to remove the exception handling here