class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.b -= 1
            return self.b > -1
        elif carType == 2:
            self.m -= 1
            return self.m > -1
        else:
            self.s -= 1
            return self.s > -1


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)