import random

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is book in train no: {slf.trainNo}, from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no {slf.trainNo} is running on time")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo}, from {fro} to {to} is {random.randint(222, 5555)}")


t = Train(12300)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")