
class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        print(f"{self.name} is performing task")

class SecurityAgent(Agent):
    def perform_task(self):
        print("Detecting cyber threat")

class MonitoringAgent(Agent):
    def perform_task(self):
        print("Monitoring system activity")

class RecoveryAgent(Agent):
    def perform_task(self):
        print("Recovering system services")

s = SecurityAgent("Security Bot", "Active")
m = MonitoringAgent("Monitoring Bot", "Active")
r = RecoveryAgent("Recovery Bot", "Active")

s.perform_task()
m.perform_task()
r.perform_task()
