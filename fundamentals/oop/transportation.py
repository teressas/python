class Automobile:
    def __init__(self, color, wheel_count, door_count, is_started=False):
        self.wheel_count = wheel_count
        self.door_count = door_count
        self.color = color
        self.is_started = is_started
    
    def info(self):
        print("**************")
        print(f"wheel_count: {self.wheel_count}")
        print(f"door_count: {self.door_count}")
        print(f"color: {self.color}")
        print(f"is_started: {self.is_started}")
        return self

    def toogle_ignition(self):
        # self.is_started = not self.is_started
        if self.is_started:
            self.is_started = True
        else:
            self.is_started = False
        return

auto1 = Automobile(4,4, color = 'red')

auto1.info().toogle_ignition().info()

class Motorcycle(Automobile):
    def __init__(self,color, wheel_count=2, door_count=0, has_front_fairing=False):
        super().__init__(wheel_count, door_count, color)
        self.has_front_fairing = has_front_fairing

class Truck(Automobile):
    def __init__(self, color, wheel_count=4, door_count=2, bed_length=8):
        super().__init__(wheel_count, door_count, color)
        self.bed_length = bed_length

motor1 = Motorcycle("black", wheel_count=3)
motor1.info()

truck1 = Truck('Silver')
truck1.info()