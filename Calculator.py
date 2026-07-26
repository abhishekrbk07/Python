# Movie Ticket Price Calculator
movie = input("Movie name: ")
tickets = int(input("How many tickets? "))
is_weekend = input("Is it weekend? (yes/no): ")

price_per_ticket = 250
if is_weekend == "yes":
    price_per_ticket = 350

total = tickets * price_per_ticket
snack_combo = 150

print(f"Movie: {movie}")
print(f"Tickets: {tickets} x Rs.{price_per_ticket} = Rs.{total}")
print(f"Add snack combo? Rs.{snack_combo}/person")

grand_total = total + (tickets * snack_combo)
print(f"Grand Total (with snacks): Rs.{grand_total}")
print(f"Total (without snacks): Rs.{total}")
print("Enjoy the movie!")
