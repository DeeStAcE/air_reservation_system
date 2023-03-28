from planes.airplane import Airplane


class Boeing737Max(Airplane):
    @staticmethod
    def get_model():
        return 'Boeing 737Max'

    @staticmethod
    def get_seating_plan():
        return range(1, 25), 'ABCDEG'

    def num_seats(self):
        rows, seats = self.get_seating_plan()
        return len(rows) * len(seats)
