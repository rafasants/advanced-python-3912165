# Example file for Advanced Python by Joe Marini
# Demonstrate how to use dictionary comprehensions

# define a list of temperature values
ctemps = [0, 12, 34, 100]

# Use a comprehension to build a dictionary
tempDict = {
  celsius_temp: (celsius_temp * 9/5) + 32
  for celsius_temp in ctemps
  if celsius_temp < 100
}
print(tempDict)

# Merge two dictionaries with a comprehension
team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}

new_team = {
  last_name: jersey_number
  for team in (team1,team2)
  for last_name, jersey_number in team.items()
}
print(new_team)