
from car import Car,  FuelOverloadException, NotEnoughFuelException
from fleet import Fleet


def main():
    trabi = Car('Trabant', 'Hycomat', 1970)
    ezerkecske = Car('Lada', '1200', 1982)
    ezerocsi = Car('Lada', '1500', 1987)
    wartbi = Car('Wartburg', '353', 1981 )
    bogar = Car('Volkswagen','Käfer 1300', 1971)
    kispolszki = Car('Polski Fiat', '126p', 1984)

    fleet = Fleet()
    fleet.add_car(trabi)
    fleet.add_car(bogar)
    fleet.add_car(ezerkecske)
    fleet.add_car(wartbi)

    print(fleet)

    print('=======================================')
     
    fleet.remove_car(wartbi)
    print('After removing Wartburg')        
    print(fleet)

    print('=======================================')
         
    print('Trabi drives 300 km:')
    trabi.drive(300)

    print('Trabi refueling 5 %')
    trabi.refuel(5)
    
    print(fleet)
    
    print('=======================================')
         
    # Attempt to drive 2000 km with Lada
    try:
        ezerkecske.drive(2000)
    except Exception as e:
        print(f'Error occured: {e}')

    print(fleet)

    # attempt to remove kispolszki from the fleet
    fleet.remove_car(kispolszki)
    
if __name__=='__main__':
    main()