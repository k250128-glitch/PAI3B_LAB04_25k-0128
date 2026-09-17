
class CyberAgent:
    def __init__(self, name, status, threat):
        self.name = name
        self.status = status
        self.__threatScore = threat

    def updateThreatScore(self):
        self.__threatScore = int(input("Enter new threat score: "))

    def retrieveThreatScore(self):
        return self.__threatScore

    def analyze(self):
        print("Analyzing security")

    def respond(self):
        print("Responding to security")

class NetworkAgent(CyberAgent):
    def analyze(self):
        print(f"{self.name} is analyzing network activity")

    def respond(self):
        print(f"{self.name} is responding to network threats")


class MalwareAgent(CyberAgent):
    def analyze(self):
        print(f"{self.name} is analyzing malware")

    def respond(self):
        print(f"{self.name} is responding to malware")


class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        print(f"{self.name} is analyzing the incident")

    def respond(self):
        print(f"{self.name} is handling the incident")


n = NetworkAgent("Network Agent", "Active", 85)
n.analyze()
n.respond()
m = MalwareAgent("Malware Agent", "Active", 65)
m.analyze()
m.respond()
i = IncidentResponseAgent("Response Agent", "Active", 40)
i.analyze()
i.respond()

