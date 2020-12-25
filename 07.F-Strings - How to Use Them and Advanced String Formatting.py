# https://youtu.be/nghuHvKLhJA

from datetime import datetime as dt
first_name = 'Joseph'
last_name = 'Yu'

# Use f-string
sentence = f"Merry Christmas {first_name.upper()} {last_name.upper()}!"

print(sentence)


# Use dictionary
# 👀 Make sure to use f"double_quotes"

person = {'name': 'Corey', 'age': '23'}

sentence = f"My name is {person['name']} and I am {person['age']} years old."

print(sentence)

# Perform calculation

calculation = f"4 times 11 is equal to {4 * 11}"

print(calculation)

# 🧠 {n:02}
# Specify leading zero

for n in range(1, 11):
    print(f"The value is {n:02}")

pi = 3.1415926

# Limit to certain digits
print(f"Pi is equal to {pi:.4f}")


birthday = dt(1990, 1, 1)

print(f"Jenny has a birthday on {birthday:%b %d, %Y}")
