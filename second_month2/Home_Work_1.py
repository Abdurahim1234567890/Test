class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'Engine on {self.title}  {self.model} started!')

    def stop_engine(self):
        print(f'Engine on {self.title}  {self.model} stoped!')

    def info(self):
        print(f'Title:{self.title}\nModel:{self.model}\nWeight{self.weight}'
        f"Hp:{self.hp}\nNm:{self.nm}\nMax_speed:{self.max_speed}\nColor:{self.color}")


# mers = Car('Mersedes', 'Maybach', '2800 kg', '530hp', '1500nm', '350km/h', 'black')
# mers.start_engine()
# mers.stop_engine()
# mers.info()

bmw = Car('BMW', 'X3', '1800 kg', '184hp', '410nm', '210km/h', 'red')
bmw.start_engine()
bmw.stop_engine()
bmw.info()