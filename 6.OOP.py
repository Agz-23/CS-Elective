class Car:
  def __init__(self, model, color):
    self.model = model
    self.color = color

  def myfunc(self):
    print(f"My favorite car is {self.model} and color is {self.color}")

car = Car("TOYOTA SUPRA", 'BLACK+')

car.myfunc()