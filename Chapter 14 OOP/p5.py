import random

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is book in train no: {self.trainNo}, from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo}, from {fro} to {to} is {random.randint(222, 5555)}")


t = Train(12300)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")