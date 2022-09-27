"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary=0, hours=0, rate=0, bonus_rate=0, contracts=0, bonus_salary=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.rate = rate
        self.bonus_rate = bonus_rate
        self.bonus_salary = bonus_salary
        self.contracts = contracts

    def get_pay(self):
        total = 0
        total += self.salary
        total += self.hours * self.rate
        total += self.bonus_rate * self.contracts
        total += self.bonus_salary
        return total

    def __str__(self):
        breakdown = ""

        if self.salary:
            temp = f'{self.name} works on a monthly salary of {self.salary}'
            breakdown += temp
        elif self.hours and self.rate:
            breakdown += f'{self.name} works on a contract of {self.hours} hours at {self.rate}/hour '


        if self.bonus_rate and self.contracts:
            breakdown += f'and recieves a comission for {self.contracts} contract(s) at {self.bonus_rate}/contract'
        elif self.bonus_salary:
            breakdown += f'and recieves a bonus comission of {self.bonus_salary}'

        breakdown += f'. Their total pay is {self.get_pay()}.'

        return breakdown



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', rate=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000,bonus_rate=200, contracts = 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', rate = 25, hours=150, bonus_rate=220, contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, bonus_salary = 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', rate=30, hours = 120, bonus_salary=600)

print(billie)
print(charlie)
print(renee)
print(jan)
print(robbie)
print(ariel)
