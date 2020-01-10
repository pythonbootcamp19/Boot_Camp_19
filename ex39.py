#In dictionary we save in pairs. For e.g. cities = {"Vikas" : "Bombay"}. print(cities["Vikas")
#create a mapping of state to abbreviation

states = {
    'Maharashtra': 'Mah',
    'Karnataka': 'Kar',
    'Andra Pradesh': 'AP',
    'Utter Pradesh': 'UP',
    'Kerala': 'Ker',
}

# create a basic set of states and some cities in them

cities = {
    'Mah': 'Mumbai',
    'Kar': 'Bangalore',
    'AP': 'Vishakapatnam',
    
}

# add some more cities

cities['UP'] = 'Lucknow',
cities['Ker'] = 'Coachin',

#print out some cities
print('-' * 10)
print("Utter Pradesh state has: ", cities['UP'])
print("Kerala state has: ", cities['Ker'])

#print some states
print('_' * 10)
print("Maharashtra's abbreviation is: ", states['Maharashtra'])
print("Utter Pradesh's abbreviation is: ", states['Utter Pradesh'])

#do it by using the state then cities dict
print('_' * 10)
print("Maharashtra has: ", cities[states['Maharashtra']])
print("Andhra Pradesh has: ", cities[states['Andra Pradesh']])

#print every state abbreviation
print('_' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('_' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('_'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('_'*10)
#safely get a abbreviation by state that might not be there
state = states.get('Madhya Pradesh')
if not state:
    print("Sorry, no Madhya Pradesh.")

#get a city with a default value
city = cities.get('MP', 'Does not Exist')
print(f"The city for the state 'MP' is: {city}")