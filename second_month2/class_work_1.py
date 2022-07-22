class Transport:

    def __init__(self, title, model, engine, max_speed, speed):
        self.title = title
        self.model = model
        self.engine = engine
        self.max_speed = max_speed
        self.speed = speed

    def start_engine(self):
        print(f'Engine on {self.title} {self.model} started!')


class Car(Transport):

    _current_speed = 0

    def __init__(self, title, model, engine, max_speed, speed, color):

        super().__init__(title, model, engine, max_speed, speed)
        self.color = color

    def stop_engine(self):
        print(f' Its stop_engine in Car')

    def gas(self):
        if self._current_speed + self.speed >= self.max_speed:
            print('CHECK on!')
        else:self._current_speed += self.speed
        print(self._current_speed)

    def stop(self):
        if self._current_speed - self.speed > 0:
            self._current_speed -= self.speed
        else:
            self._current_speed = 0
        print(self._current_speed)

class Airplane(Transport):

    def stop_engine(self):
        print(f' Its stop_engine in Airplane')


bmw = Car('BMW', 'e36', 'v10', 330, 60, 'black')
bmw.start_engine()
bmw.gas()
bmw.gas()
bmw.gas()
bmw.gas()