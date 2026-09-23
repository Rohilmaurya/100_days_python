print("Welcome to the secret auction program.")
name=input("What is your name?: ")
bid=int(input("What is your bid?: Rs."))
bid_list={name:bid}
while True:
    more_bidders=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders=="yes":
        name=input("What is your name?: ")
        bid=int(input("What is your bid?: Rs."))
        bid_list[name]=bid
    elif more_bidders=="no":
        print("Thank you for participating in the auction.")
        break
max=0
for i in bid_list:
    if bid_list[i]>max:
        max=bid_list[i]
        winner=i
print(f"The winner is {winner} with a bid of Rs.{max}.")