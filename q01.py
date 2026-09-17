

class ThreatDetector:
    def __init__(self, name, ip, threat):
        self.device_name = name
        self.ip_address = ip
        self.threat_level = threat

    def scan(self):
        if self.threat_level == "Low":
            return "System Safe"
        if self.threat_level == "Medium":
            return "Suspicious Activity"
        if self.threat_level == "High":
            return "Critical Threat Detected"


t = ThreatDetector("huzaifa", "7", "medium")
print(t.scan())

