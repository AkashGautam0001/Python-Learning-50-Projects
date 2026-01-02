import math
def calculate_minutes(age_years):
    age_years = float(age_years)
    DAYS_IN_YEAR = 365.25
    HOUR = 24
    MINUTES = 60
    
    day_age = age_years*DAYS_IN_YEAR
    hour_age = day_age*HOUR
    minutes_age = hour_age*MINUTES

    return [day_age, hour_age, minutes_age]
        

while True :
    age = input("Enter Your Age in years : ")
    lives_age = calculate_minutes(age)
    print(f"""\nYou are approximately:
      - {lives_age[0]:,.2f} days old
      - {lives_age[1]:,.2f} hours old
      - {lives_age[2]:,.2f} minutes old
        """)
