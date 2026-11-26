RATE = 98
def inr_to_usd(inr):
 return inr / RATE
def usd_to_inr(usd):
 return usd * RATE
choice = input("Enter 1 for INR to USD, 2 for USD to INR: ")
amount = float(input("Enter amount: "))
if choice == "1":
 print("USD:", round(inr_to_usd(amount), 2))
elif choice == "2":
 print("INR: Rs.", round(usd_to_inr(amount), 2))
else:
 print("Invalid choice")