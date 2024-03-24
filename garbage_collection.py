population = 0


class Human:
    def __init__(self):
        global population
        population += 1

    def __del__(self):
        global population
        population -= 1
        print('Deleted')


people = []

for i in range(1000):
    temp = Human()
    people.append(temp)

print(population)
