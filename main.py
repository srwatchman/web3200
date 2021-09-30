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


