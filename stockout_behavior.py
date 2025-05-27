import random

class Person:
    def __init__(self, location, intends_to_use_fp, preferred_method=None, current_method=None):
        self.location = location
        self.intends_to_use_fp = intends_to_use_fp
        self.can_reach_facility = False
        self.preferred_method = preferred_method
        self.current_method = current_method
        self.received_method = False

def assign_preferred_method(person, methods):
    if person.intends_to_use_fp:
        person.preferred_method = random.choice(methods)

def check_stock(person, method, stockout_risks):
    if method is None:
        return False
    return random.random() >= stockout_risks[method]  # True = in stock

def handle_stockout(person, methods, stockout_risks):
    preferred = person.preferred_method
    if preferred is None:
        return

    # Check if preferred method is in stock
    if check_stock(person, preferred, stockout_risks):
        person.current_method = preferred
        person.received_method = True
        print(f"→ {preferred} is in stock. Person uses preferred method.")
    else:
        # Preferred method stocked out
        print(f"→ {preferred} is OUT of stock.")
        # Behavior 1: New user does not initiate
        if person.current_method is None:
            person.current_method = None
            person.received_method = False
            print("   ↳ Person does NOT initiate method use.")
        else:
            # Behavior 2: Existing user discontinues
            print("   ↳ Person DISCONTINUES use due to stockout.")
            person.current_method = None
            person.received_method = False
            
            # Behavior 3: Attempt switch if other methods are in stock
            available_methods = [m for m in methods if m != preferred and check_stock(person, m, stockout_risks)]
            if available_methods:
                new_method = random.choice(available_methods)
                person.current_method = new_method
                person.received_method = True
                print(f"   ↳ Person SWITCHES to non-preferred method: {new_method}")

# Sample data
METHODS = ["implant", "IUD", "pill", "injectable"]
stockout_risks = {
    "implant": 0.09,
    "IUD": 0.26,
    "pill": 0.17,
    "injectable": 0.49
}

people = [
    Person("urban", True),
    Person("rural", True),
    Person("urban", False)
]

# Simulate
for person in people:
    person.can_reach_facility = True  # Assume all made it
    assign_preferred_method(person, METHODS)
    if person.intends_to_use_fp and person.can_reach_facility:
        handle_stockout(person, METHODS, stockout_risks)
    else:
        print("→ Person did not intend to use or could not reach facility.")

    print(f"{person.location} | Intends: {person.intends_to_use_fp} | Preferred: {person.preferred_method} | Current: {person.current_method} | Received: {person.received_method}")
    print("–––")
