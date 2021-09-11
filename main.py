import random

choice=["rock","paper","scissors"]

computerScore = 0
playerScore = 0
print("what's is your choice between this option:",choice) #while player not in choice:
while playerScore < 10 or computerScore < 10:
        playerChoice = None
        computerChoice = random.choice(choice)
        while playerChoice not in choice:
            playerChoice = input("your choice?:").lower()  # lower() is for conver input to lowrcase


        if playerChoice == computerChoice:
            print("both of chioce are the same")
        elif playerChoice == "paper" and computerChoice == "scissors":
            print("pc win")
            computerScore +=1
            print("your score=",playerScore,"pc score=",computerScore)
        elif playerChoice == "rock" and computerChoice == "scissors":
            print("player win")
            playerScore +=1
            print("your score=", playerScore, "pc score=", computerScore)
        elif playerChoice == "rock" and computerChoice == "paper":
            print("pc win")
            computerScore +=1
            print("your score=", playerScore, "pc score=", computerScore)
        elif playerChoice == "scissors" and computerChoice == "paper":
            print("player win")
            playerScore +=1
            print("your score=", playerScore, "pc score=", computerScore)
        elif playerChoice == "scissors" and computerChoice == "rock":
            print("pc win")
            computerScore +=1
            print("your score=", playerScore, "pc score=", computerScore)
        elif playerChoice == "paper" and computerChoice == "rock":
            print("player win")
            playerScore +=1
            print("your score=", playerScore, "pc score=", computerScore)


print(computerScore)
print(playerScore)


