# if statements = s block of codes that will get executed if it's condition is true
age = int(input("How old are you?: "))

if age == 100:
    print("Damn, you're a century old!!")
elif age >= 18:
    print("You're an adult bro!!")
elif age < 0:
    print("You're not born yet, whoa!!")
else:
    print("You're a child according to your age.")

# logical operators (and, or, not) = used to check if two or more conditional statement

temp = int(input("What is the temperature today outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is nice today.")
    print("You should go outside and enjoy the weather!")
elif temp < 0 or temp > 30:
    print("The temperature is not good today.")
    print("Don't go outside in this weather...")