
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature): 
  if temperature > 100.4:
    return True
  else:
    return False


# Get temperature from user and convert to float


temp = int(input("Tell me a number: "))
if check_fever(temp):
  print("You have a fever.")
else:
  print("You don't have a fever.")