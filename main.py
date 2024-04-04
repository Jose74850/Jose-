# initilaize an empty list to hold favorite numbers
favorite_numbers = []

# Loop until a non-inteager is entered, adding valid integers to the list
while True:
  try:
    number = int(input("Enter your favorite number(or a non-integer to quit)"))
  except ValueError: 
    print("Non-integer entered. Exiting the loop and displaying favorite numbers.")
    break 
  else:
    favorite_numbers.append(number)
    print(f"Number{number} added to favorite numbers.")
  finally:
    print("Attempt to add favorite number completed")

# Display the list of favorite numbers
print(f"Your favorite numbers are:", favorite_numbers)