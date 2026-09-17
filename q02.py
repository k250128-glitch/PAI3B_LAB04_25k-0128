

class PasswordVault:
    def __init__(self, username, password, vault_status):
        self.username = username
        self.__password = password
        self._vault_status = vault_status

    def getPassword(self):
        return self.__password

    def change_password(self):
        password = input("Enter new Password: ")
        self.__password = password

    def verify_password(self):
        verify = input("Enter password to verify: ")
        if self.__password == verify:
            print("Access Granted")
        else:
            print("Access Denied")

    def display_status(self):
        print(self._vault_status)


p = PasswordVault("huzaifa0128", "huzaifa1234", "protected")
p.change_password()
p.verify_password()
p.display_status()
