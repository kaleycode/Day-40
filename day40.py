print("Day 40 Challenge!")
print()
print("⭐️ Contact Card ⭐️")
print()
print()
name = input("Enter your name: \n").strip()
dateOfBirth = input("Enter your date of birth: \n").strip()
telephoneNumber = input("Enter your telephone number: \n").strip()
email = input("Enter your email: \n").strip()
address = input("Enter your address: \n").strip()
contactCard = {"name": name, "dateOfBirth": dateOfBirth, "telephoneNumber": telephoneNumber, "email": email, "address": address}
print()
print(f"""
Hi, {contactCard['name']}.
  Our dictionary says that you were born on {contactCard['dateOfBirth']}, we can call you on 
{contactCard['telephoneNumber']},
email{contactCard['email']}, or write to {contactCard['address']}. 
      Let us know if any of this is incorrect or if you have any questions!""")