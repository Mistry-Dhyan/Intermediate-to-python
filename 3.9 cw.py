zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries",
"Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini",
"Libra", "Aquarius"]}

print(zodiac_elements.get('earth'))

print(zodiac_elements.get('fire'))

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam":
123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)

stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir":
20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}

available_items.pop('power stew')
print(available_items)

available_items.pop('stamina grains')
print(available_items)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22,
"lists": 19, "classes": 18, "dictionaries": 18}

number_of_exercises_is_in_this_list_or_you_can_call_it_lessions = []
for list in num_exercises.keys():
    number_of_exercises_is_in_this_list_or_you_can_call_it_lessions.append(list)
print(number_of_exercises_is_in_this_list_or_you_can_call_it_lessions)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22,
"lists": 19, "classes": 18, "dictionaries": 18}

number_of_exercises_is_in_this_list_or_you_can_call_it_total = []
for list in num_exercises.values():
    number_of_exercises_is_in_this_list_or_you_can_call_it_total.append(list)
print(number_of_exercises_is_in_this_list_or_you_can_call_it_total)

women_in_occupation = {"CEO": 28, "Engineering Manager": 9,
"Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in women_in_occupation.items():
    print('Women make up ' + str(value) + ' percent of ' + key + 's.')
