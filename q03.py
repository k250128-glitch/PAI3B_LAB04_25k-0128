
class SecuritySystem():
    def respond(self):
        print("Security system resonse")

class Firewall(SecuritySystem):
    def respond(self):
        print("Block suspicious network traffic")

class Antiviurus(SecuritySystem):
    def respond(self):
        print("Isolate malicious files")

class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Generate security alert")

f =Firewall()
f.respond()

a= Antiviurus()
a.respond()

i= IntrusionDetectionSystem()
i.respond()
