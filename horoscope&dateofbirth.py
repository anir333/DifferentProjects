year_of_birth = input("What year were you born? ")
month_of_birth = input("What month were you born? ")
day_of_birth = input("What day were you born? ")

horoscope = ""
if int(day_of_birth) > 20 and month_of_birth.lower() == "march":
    horoscope = "Aries"
elif int(day_of_birth) < 20 and month_of_birth.lower() == "april":
    horoscope = "Aries"
elif int(day_of_birth) > 19 and month_of_birth.lower() == "april":
    horoscope = "Taurus"
elif int(day_of_birth) < 21 and month_of_birth.lower() == "may":
    horoscope = "Taurus"
elif int(day_of_birth) > 20 and month_of_birth.lower() == "may":
    horoscope = "Gemini"
elif int(day_of_birth) < 21 and month_of_birth.lower() == "june":
    horoscope = "Gemini"
elif int(day_of_birth) > 20 and month_of_birth.lower() == "june":
    horoscope = "Cancer"
elif int(day_of_birth) < 23 and month_of_birth.lower() == "july":
    horoscope = "Cancer"
elif int(day_of_birth) > 22 and month_of_birth.lower() == "july":
    horoscope = "Leo"
elif int(day_of_birth) < 23 and month_of_birth.lower() == "august":
    horoscope = "Leo"
elif int(day_of_birth) > 22 and month_of_birth.lower() == "august":
    horoscope = "Virgo"
elif int(day_of_birth) < 23 and month_of_birth.lower() == "september":
    horoscope = "Virgo"
elif int(day_of_birth) > 22 and month_of_birth.lower() == "september":
    horoscope = "Libra"
elif int(day_of_birth) < 23 and month_of_birth.lower() == "october":
    horoscope = "Libra"
elif int(day_of_birth) > 22 and month_of_birth.lower() == "october":
    horoscope = "Scorpio"
elif int(day_of_birth) < 22 and month_of_birth.lower() == "november":
    horoscope = "Scorpio"
elif int(day_of_birth) > 21 and month_of_birth.lower() == "november":
    horoscope = "Sagittarius"
elif int(day_of_birth) < 22 and month_of_birth.lower() == "december":
    horoscope = "Sagittarius"
elif int(day_of_birth) > 21 and month_of_birth.lower() == "december":
    horoscope = "Capricorn"
elif int(day_of_birth) < 20 and month_of_birth.lower() == "january":
    horoscope = "Capricorn"
elif int(day_of_birth) > 19 and month_of_birth.lower() == "january":
    horoscope = "Aquarius"
elif int(day_of_birth) < 19 and month_of_birth.lower() == "february":
    horoscope = "Aquarius"
elif int(day_of_birth) > 18 and month_of_birth.lower() == "february":
    horoscope = "Pisces"
elif int(day_of_birth) < 21 and month_of_birth.lower() == "march":
    horoscope = "Pisces"
else:
    print("Wrong! Try again.")


print(f"""

Your date of birth is {day_of_birth}/{month_of_birth}/{year_of_birth},
and your sign is {horoscope}

""")
