from datetime import datetime
birthdate=input("enter your birthdate: (YYYY-MM-DD)")
today=datetime.now()
birth_input=datetime.strptime(birthdate, "%Y-%m-%d")
age_days= today - birth_input
age_years = age_days.days // 365

# Output
print(f"You are approximately {age_years} years old.")
print(f"You have been alive for {age_days.days} days!")
print(f"That is approximately {age_years} years!")
print("Keep going! 🚀")