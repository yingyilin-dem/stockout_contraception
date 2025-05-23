import random

class Person:
    def __init__(self, location, intends_to_use_fp):
        self.location = location
        self.intends_to_use_fp = intends_to_use_fp
        self.can_reach_facility = False
        self.method = None
        self.received_method = False

def assign_method(person, methods):
    if person.intends_to_use_fp and person.can_reach_facility:
        person.method = random.choice(methods)
    else:
        person.method = None

def check_stockout(person, risks):
    if person.method is None:
        return False
    return random.random() >= risks[person.method]  # True = in stock

# Sample data
METHODS = ["implant", "IUD", "pill", "injectable"]
stockout_risks = {
    "implant": 0.20,
    "IUD": 0.15,
    "pill": 0.05,
    "injectable": 0.10
}

people = [
    Person("urban", True),
    Person("rural", True),
    Person("urban", False)
]

# Simulate method assignment and stockout
for person in people:
    person.can_reach_facility = True  # Assume they all made it
    assign_method(person, METHODS)

    if person.method:
        person.received_method = check_stockout(person, stockout_risks)
    else:
        person.received_method = False

    print(f"{person.location} | Intends: {person.intends_to_use_fp} | Method: {person.method} | Received: {person.received_method}")
