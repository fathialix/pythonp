class Car():
    def __init__(self, owner, model, color, price):
        self.owner = owner
        self.model = model
        self.color = color
        self.price = price


car_one = Car("James", "Corolla", "Red", "9.5M")
print(car_one.owner)
print(car_one.model)
print(car_one.color)
print(car_one.price)
print("....end of car one....")

car_two = Car("Jake", "Audi A3", "Black", "18M")
print(car_two.owner)
print(car_two.model)
print(car_two.color)
print(car_two.price)
print("....end of car two....")

car_three = Car("Jay", "Volkswagen Golf", "White", "16M")
print(car_three.owner)
print(car_three.model)
print(car_three.color)
print(car_three.price)
print("....end of car three....")

