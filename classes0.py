class Flight:

    counter = 1

    def __init__(self,origin,destination,duration):

        self.id = Flight.counter
        Flight.counter +=1

        self.passengers = []

        self.origin =origin
        self.destination=destination
        self.duration=duration
    
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight origin: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration +=amount

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger:

    def __init__(self,name):
        self.name = name



def main():
    f1 = Flight(origin="New York",destination="Paris",duration=540)
    f2 = Flight("BS","Olav",540)
    #f.duration += 10
    f1.delay(10)
    f1.print_info()
    f2.print_info()

    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")
    leo = Passenger(name="Leo")

    f1.add_passenger(alice)
    f1.add_passenger(bob)
    f1.add_passenger(leo)

    f1.print_info()
    #sdfgit 
    #dsf




if __name__== "__main__":
    main()