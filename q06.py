
class Computer():
    def __init__(self, cpu, ram, battery):
        self.cpuUsage = cpu
        self.ramUsage = ram
        self.batterylevel = battery

    def system_status(self):
        if self.cpuUsage > 80:
            print("Heavy CPU Load")
        if self.ramUsage > 85:
            print("High Memory Usage")
        if self.batterylevel <20:
            print("Low Battery")


c = Computer(6,13,82)
c.system_status()
c1 = Computer(67,0,300)
c1.system_status()

