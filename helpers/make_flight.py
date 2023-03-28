from pprint import pprint as pp

from flight.flight import Flight
from planes.airbus_a380 import AirbusA380
from planes.boeing737max import Boeing737Max


def make_flight():
    airbus = AirbusA380()
    boeing = Boeing737Max()
    f = Flight('BA234', boeing)
    # print(f.get_airways())
    # print(f.get_number())
    # print(f.get_airplane_model())
    f.allocate_passenger('12A', 'Jarosław K')
    f.allocate_passenger('12B', 'Paweł K')
    f.allocate_passenger('12C', 'Lech K')
    pp(f.seats)
    print(f.get_num_empty_seats())
