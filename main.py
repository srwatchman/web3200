from vehicles import Car, ElectricCar

ferrari = Car("Ferrari", "200")
ferrari.run_car()

leaf = ElectricCar("Leaf", "70", "all electric")
leaf.run_car()
leaf.display_electric_type()

# alternatively one can import all the classes at once by just naming
# the module.  but then you
# can't access the classes unless you prefix them with the
# module name:
import vehicles

ferrari = vehicles.Car("Ferrari", "200")
ferrari.run_car()

leaf = vehicles.ElectricCar("Leaf", "70", "all electric")
leaf.run_car()
leaf.display_electric_type()

from shops import Restaurant, IceCreamStand

paris = Restaurant("Le Petit Paris", "French")
paris.describe_restaurant()
paris.open_restaurant()

friendlies = IceCreamStand("Friendlies", "Ice Cream", "Rocky Road", "Orange", "Sherbert")
friendlies.describe_restaurant()
friendlies.display_flavors()


