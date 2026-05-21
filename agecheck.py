name = input("Enter name: ")
year = int(input("Enter your year of birth: "))
currentYear = 2026
age = currentYear - year
print("Name:",name)
print("Age:",age)
if age>=60:
  print(name,"is a senior citizen")
else:
  print(name,"is not a senior citizen")
