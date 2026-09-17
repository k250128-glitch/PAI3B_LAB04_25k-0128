
class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        print(f"{self.name} moving")

    def charge(self):
        print(f"{self.battery} charging")


class DeliveryRobot(Robot):
    def move(self):
        if self.battery < 20:
            print("Battery less than 20, cannot move.")
        else:
            print("Moving to a delivery location")


class SecurityRobot(Robot):
    def move(self):
        if self.battery < 20:
            print("Battery is less than 20, cannot move.")
        else:
            print("Patrolling a security area")


class RescueRobot(Robot):
    def move(self):
        if self.battery < 20:
            print("Battery is less than 20, cannot move.")
        else:
            print("Moving towards a disaster location")


d = DeliveryRobot("Delivery Bot", 80)
s = SecurityRobot("Security Bot", 15)
r = RescueRobot("Rescue Bot", 50)

d.move()
s.move()
r.move()
