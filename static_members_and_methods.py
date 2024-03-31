class Human:
    population = 0  # Static variable

    def __init__(self):
        Human.population += 1

    @staticmethod
    def check_population():
        print(f'Total population is {Human.population}')

    @classmethod
    def check_population_class(cls):
        print(f'Total class population is {cls.population}')


mohit = Human()
rahul = Human()

print(Human.population)
print(rahul.population)
print(Human.check_population_class())
