class Car:
    def __init__(self,model, weight, hp, nm, max_speed, color):
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        return f'Engine on  {self.model} started!'

    def stop_engine(self):
        return f'Engine on  {self.model} stoped!'


    def car_info(self):
        return f'Model: {self.model}\n Weight:{self.weight}\n Hp:{self.hp}\n Nm:{self.nm}\n Max_speed:{self.max_speed}\nColor:{self.color}'


