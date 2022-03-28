import random
  
weights = (6,5,7,2,3,4,5,6,7)

while True:
    numbers = [
                random.randint(1,9),
                random.randint(0,9),
                random.randint(1,9),
                random.randint(0,9),
                random.randint(0,9),
                random.randint(0,9),
                random.randint(0,9),
                random.randint(0,9),
                random.randint(0,9)
            ]
    control_number = sum([i * j for i,j in zip(numbers, weights)]) % 11
    if control_number < 10:
        break

numbers.append(control_number)

print("".join(map(str,numbers)))
