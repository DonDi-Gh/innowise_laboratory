def generate_profile(age):
    if 0<=age<=12:
        return "Child"
    elif 13<=age<=19:
        return "Teenager"
    return "Adult"
    


user_name = input("Hi, what is your name? ")
birth_year_str = input("What year did you born? ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year
hobbies = list()

hobbie = input("Enter a favourite hobby or type 'stop' to finish: ")

while hobbie != 'stop':
    hobbies.append(hobbie)
    hobbie = input("Enter a favourite hobby or type 'stop' to finish: ")


life_stage = generate_profile(current_age)

user_profile = {'name':user_name, 'age': current_age, 'stage':life_stage, 'hobbies_list':hobbies}

print(f'--- \nProfile Summary: \nName: {user_profile['name']}\nAge: {user_profile['age']}\nLife Stage: {user_profile['stage']}')
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies({len(hobbies)}):\n - {'\n - '.join(hobbies) }\n---")
