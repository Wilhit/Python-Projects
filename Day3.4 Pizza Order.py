#User input
print("Welcome to Wilhit Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 80
    if pepperoni == "Y":
        bill += 15
    if cheese == "Y":
        bill += 10
    
elif size == "M":
    bill = 110
    if pepperoni == "Y":
        bill += 20
    if cheese == "Y":
        bill += 10
elif size == "L":
    bill = 150
    if pepperoni == "Y":
        bill += 20
    if cheese == "Y":
        bill += 10
print(f"Your final bill is: N${bill}")
