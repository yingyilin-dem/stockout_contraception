import random

class Person:
    def __init__(self, location, intends_to_use_fp):
        self.location = location  # 'urban' or 'rural'
        self.intends_to_use_fp = intends_to_use_fp
        self.can_reach_facility = False

def check_accessibility(person, params):
    """Determine whether a person can reach a facility based on location and barrier probability."""
    if person.location == "urban":
        return random.random() < params["urban_access_probability"]
    else:
        return random.random() < params["rural_access_probability"]

# Example usage:
params = {
    "urban_access_probability": 0.95,
    "rural_access_probability": 0.7
}

people = [
    Person("urban", True),
    Person("rural", True),
    Person("urban", False)
]

for person in people:
    if person.intends_to_use_fp:
        person.can_reach_facility = check_accessibility(person, params)
    else:
        person.can_reach_facility = False

    print(f"{person.location} | Intends: {person.intends_to_use_fp} | Can reach: {person.can_reach_facility}")
