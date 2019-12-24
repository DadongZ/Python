
import datetime

class User:
    """Storing name and birthday. Soon we will add other info such address, phone, email etc."""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday
        #Extract first and last name
        self.first_name = full_name.split(" ")[0]
        self.last_name = full_name.split(" ")[-1]
    
    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2019, 12, 23)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365.25
        return int(age_in_years)


user =User("Dadong Zhang", "19771202")

print(user.name)
print(user.birthday)
print(user.age())

help(User)


