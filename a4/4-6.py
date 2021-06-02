nums = list(range(1, 20, 1))
for num in nums:
	print(num)

tribles = [value*3 for value in range(1, 10)]
print(tribles)

cubes = []
for num in range(1, 11):
	cube = num**3
	cubes.append(cube)
for cube in cubes:
	print(cube)