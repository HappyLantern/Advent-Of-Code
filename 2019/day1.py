total_fuel_req = 0

# PART 1
input = open('day1_input.txt', 'r')
total_fuel_req = sum([int(nbr) // 3 - 2 for nbr in input])
print(total_fuel_req)

# PART 2
input = open('day1_input.txt', 'r')
total_fuel_req = 0
module_masses = [int(nbr) for nbr in input]

additional_fuel = any(i >= 0 for i in module_masses)
while additional_fuel:
    module_masses = [module_mass // 3 - 2 if module_mass // 3 - 2 >= 0 else 0 for module_mass in module_masses]
    total_fuel_req += sum(module_masses)
    additional_fuel = any(i > 0 for i in module_masses)
print(total_fuel_req)

