# create a list of prime numbers
print("--- PROGRAM 1 ---")

prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print('Reversed List:', prime_numbers)


#2
# Operating System List
print("\n=== PROGRAM 2 ===")

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()
print('Updated List:', systems)


#3
print ("\n=== PROGRAM 3 ===")

systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)

# Reversing a list	
# Syntax: reversed_list = systems[start:stop:step] 
reversed_list = systems[::-1]
print('Updated List:', reversed_list)

#4
# Operating System List
systems = ['Windows', 'macOS', 'Linux']

# Printing Elements in Reversed Order
for o in reversed(systems):
    print(o)