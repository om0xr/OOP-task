class Phone:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name):
        self.contacts.append(name)

    def remove_contact(self, name):
        if name in self.contacts:
            self.contacts.remove(name)

    def make_call(self, name):
        if name in self.contacts:
            print(f"Calling {name}...")
        else:
            print(f"{name} is not in contacts.")

class Camera:
    def take_pic(self):
        print("The picture was taken successfully.")

class Smartphone(Phone, Camera):
    pass

s = Smartphone()
s.add_contact("Omar")
s.make_call("Omar")
s.take_pic()
s.remove_contact("Omar")