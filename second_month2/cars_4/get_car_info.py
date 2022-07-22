from second_month2.cars.create_car import Car

def get_car_info(model, weight, hp, nm, max_speed, color):
    car = Car (
            model=model,
            weight=weight,
            hp=hp,
            nm=nm,
            max_speed=max_speed,
            color=color
    )
    return car