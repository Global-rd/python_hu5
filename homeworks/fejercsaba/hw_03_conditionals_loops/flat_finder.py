# Feladat: bekéri a felhasználótól a várost és a lakbér árát. 
# Ezután a fentiek alapján printeld ki egy f-string használatával hogy az adott 
# feltételek (város és albérlet ára) mellett be tudna e költözni az adott helyre.

city_name = input("city : ").strip().title()
rent = input("monthly rent : ")
rent_int = int(rent)
move = "can't" # egyéb város 3000 töl nagyobb lakbár esetén marad ez az érték
if city_name in ("New York", "San Francisco") and rent_int < 4000:
    move_status = "can"
elif city_name == "Washington":
    move_status = "can't"
elif city_name == "Chicago":
    move_status = "can"
elif rent_int < 3000:
    move_status = "can"

print(f"Sári  {move_status} move to {city_name}." )
