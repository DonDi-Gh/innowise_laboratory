def generate_profile(curent_age):
    pass



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