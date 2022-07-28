age = input("What is your current age?\n")
# 1 year = 365 days
# 1 year = 12 months
# 1 year = 52 weeks
yearsleft = 90 - int(age)

days = yearsleft * 365
weeks = yearsleft * 52
months = yearsleft * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")