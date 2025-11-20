# Life stage determination
def generate_profile(age):
    if 0<=age<=12:
        return "Child"
    elif 13<=age<=19:
        return "Teenager"
    return "Adult"


user_name = input("Hi, enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = list()
hobbie = input("Enter a favorite hobby or type 'stop' to finish: ")

# Loop for getting hobbies
while hobbie != 'stop':
    hobbies.append(hobbie)
    hobbie = input("Enter a favorite hobby or type 'stop' to finish: ")

life_stage = generate_profile(current_age)
# Creation of summary for all information
user_profile = {'name':user_name, 'age': current_age, 'stage':life_stage, 'hobbies_list':hobbies}
# Output for all data
print(f'--- \nProfile Summary: \nName: {user_profile['name']}\nAge: {user_profile['age']}\nLife Stage: {user_profile['stage']}')
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies({len(hobbies)}):")
    for element in hobbies:
        print(f" - {element}")
print('---')
