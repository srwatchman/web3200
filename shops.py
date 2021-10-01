class Restaurant():
    def __init__(self, name_type, cuisine_type):
        self.name_type = name_type
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("This restaurant is named " + self.name_type + ". Go here if you like " + self.cuisine_type)

    def open_restaurant(self):
        print("This restaurant is open")


class IceCreamStand(Restaurant):
    def __init__(self, name_type, cuisine_type, flavor, flavor1, flavor2):
        super().__init__(name_type, cuisine_type)
        self.flavor = flavor
        self.flavor1 = flavor1
        self.flavor2 = flavor2

    def display_flavors(self):
        print("At this ice cream stand named " + self.name_type + " we serve the following flavors: " + self.flavor + ", " + self.flavor1 + ", " + self.flavor2)

if __name__ == '__main__':
    emilios = IceCreamStand("Emilios", "Italian", "Chocolate", "Vanilla", "Strawberry")
    emilios.describe_restaurant()
    emilios.open_restaurant()
    emilios.display_flavors()