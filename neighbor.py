class Neighborhood:
    def __init__(self, street, neighborhood):
        self.street = street
        self.neighborhood = neighborhood

    def add(self, street, neighborhood):
        pass

    def streets_certain_neighborhood(self, neighborhood_name: str):
        pass

    def __str__(self):
        pass


a = [2,3]
b = a
b = b + [1]
print(a)