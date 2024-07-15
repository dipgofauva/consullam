def my_generator():
    yield [11, 5, 0.002746942550584391]

# Create a generator object
gen = my_generator()

# Iterate over the values yielded by the generator
for value in gen:
    print(value)
