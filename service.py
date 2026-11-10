# -----------------------------
# 1. IMPORTS
# -----------------------------
# from random import randint, randrange

# -----------------------------
# 2. SETUP (CONSTANTS & DICTIONARIES)
# -----------------------------
# always 1.2 - we are calculating CML without any daily exercise
TODAYS_ACT_FACTOR = 1.2
TITLES = {
    'Female': 'dear Madam',
    'Male': 'dear Sir'
    }

# Using a List of Dictionaries to store complete user profiles
users = [
    {
        "name": "Anna",
        "weight": 65.0, 
        "reference": "dear Madam", 
        "skinfolds_sum": 55, 
        "age_in_years": 47
        },
    {
        "name": "John",
        "weight": 82.5,
        "reference": "dear Sir",
        "skinfolds_sum": 45, 
        "age_in_years": 55
        },
    {
        "name": "Sasha",
        "weight": 70.0,
        "reference": "dear Madam",
        "skinfolds_sum": 50,
        "age_in_years": 30
        }
]

# -----------------------------
# 3. FUNCTIONS
# -----------------------------
def calc_user_cml(user_weight, user_act_factor):
    bmr = user_weight * 24.2  # Basal Metabolic Rate (in kcal/day)
    return round(bmr * user_act_factor, 2)  # Calorie Maintenance Level (in kcal/day)

def calc_user_fat_perc(skinfolds_sum, age_in_years, reference): 
    if reference == TITLES['Male']:
        body_density = 1.10938 - (0.0008267 * skinfolds_sum) + \
        (0.0000016 * (skinfolds_sum ** 2)) - (0.0002574 * age_in_years)
    elif reference == TITLES['Female']:
        body_density = 1.0994921 - (0.0009929 * skinfolds_sum) + \
        (0.0000023 * (skinfolds_sum ** 2)) - (0.0001392 * age_in_years)
    return round((495 / body_density) - 450, 2)  # Current Body Fat Percentage (in %)

def calc_user_fat_lvl(user_weight, fat_perc): 
  return round(user_weight / 100 * fat_perc, 2)  # Current Body Fat Level (in kg)

def input_weight_fail_proof():
    while True:
        try:
            # Check if the user input for the 'weight' variable is the correct data type
            user_weight = float(input('\nWhat is your current weight? '))
            print("\nThank you.")
            return user_weight
        except:
            # If an error occurs (like typing text instead of a float)
            print("You need to type a whole or decimal number. Try again.")

def input_sex_fail_proof():
    while True:
        # .strip() removes accidental spaces, .title() capitalizes the first letter
        sex = input('What is your sex? (Male/Female) ').strip().title()
        # Check if the user input is correct
        if sex in TITLES:
            return TITLES[sex]
        print("You need to type 'Male' or 'Female'. Try again.")

"""
def generate_a_squat_challenge():
    # Generates a random integer from 1 to 10.
    squat_number_now = randint(1, 10)
    # Generates a random integer from 20 to 100 divisible by 10.
    squat_number_today = randrange(20, 100, 10)
    print(
        "\nHow about some challenge to burn more calories? " 
        f"Let's do {squat_number_now} squats right now!"
        "\n\nHow about some greater challenge to burn even more calories? "
        f"Let's do {squat_number_today} squats today!\n"
    )
"""

def print_username_letters_top_down(): 
    # To get your EXACT original output (letters, commas, and a trailing space), 
    # we dynamically build the original string format from the new database.
    users_string = ",".join(user['name'] for user in users) + " "
    for letter in users_string: # Does something to every letter in the variable "users"
        print(letter) # Each letter is printed

def print_whole_usernames_top_down(): # Print exisitng usernames individually
    print("These are existing users: ")
    for user in users:
        print(user["name"])

def input_whole_number_fail_proof(prompt_text):
    while True:
        try:
            return int(input(prompt_text))
        except ValueError:
            print("You need to type a whole or decimal number. Try again.")

def save_user_record():
    name = input("What is your name? ")
    weight = input_weight_fail_proof()
    reference = input_sex_fail_proof()
    # Watch https://youtu.be/hvC2TDs95xY?si=eVcK6IbKbOleZs-M 
    skinfolds_sum = input_whole_number_fail_proof("What is your skinfolds sum? ") 
    age_in_years = input_whole_number_fail_proof("What is your age in years? ")
    users.append({
        "name": name,
        "weight": weight,
        "reference": reference,
        "skinfolds_sum": skinfolds_sum,
        "age_in_years": age_in_years
        })
    print(f"User {name} has been added to the database.")

def print_my_stats():
    user_name = input("What is your username? ")
    while True: 
        for user in users:
            if user["name"] == user_name:
                user_fat_perc = calc_user_fat_perc(user['skinfolds_sum'], user['age_in_years'],
                      user['reference'])
                print(
                    f"\nWithout any exercise at all, {user['reference']},"
                    "\nyou could consume up to"
                    f" {calc_user_cml(user['weight'],
                     TODAYS_ACT_FACTOR)}kcal today\n"
                    "to preserve your current weight."
                    "\n\nYour current fat balance is:"
                    f"\n{calc_user_fat_lvl(user['weight'],
                     user_fat_perc)}kg fat "
                    f"({user_fat_perc}% of your body weight)\n"
                )
                return
        print("\nUser not found. Please try again.")
        user_name = input("What is your username? ")

# -----------------------------
# 4. MAIN PROGRAM
# -----------------------------
def main():
    while True:
        print(
            "What do you want to do? "
            "1 Register "
            "2 Print my stats "
            "3 Exit"
        )
        choice = input()
        if choice == "1":
            save_user_record()
        elif choice == "2":
            print_whole_usernames_top_down()
            print_my_stats()
        elif choice == "3":
            break
        else:
            print("Invalid choice. You must type 1-3. Please try again.")

    # generate_a_squat_challenge()
    # print_username_letters_top_down()
    # print_whole_usernames_top_down()

if __name__ == "__main__":
    main()