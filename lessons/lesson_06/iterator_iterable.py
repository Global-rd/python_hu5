#ITERABLE: egy objektum amely képes egyesével visszaadni az elemeit (pl: string, list)
#ITERATOR: egy objektum amellyel egy iterable elemeit egymás után egyesével kérhetjük le. az iter() function-nel hozzuk létre, és a next() function-t hívjuk meg
#ITERATION: az elemenként való haladás folyamata
#LOOP: automatizálja az iteration folyamatát

#PÉLDA:

#ITERABLE: spotify (vagy bármilyen) lejátszási lista, benne a kedvenc zenéinkkel
#ITERATOR: mi magunk, akik egy zeneszámról a másikra tudunk kattintani a next gombbal. Tudjuk hogy most melyik szám szól, és képesek vagyunk a következőre ugrani
#ITERATION: következő számra való ugrás a next gombbal
#LOOP: automatikus lejátszás anélkül, hogy mi magunk megnyomnánk a next gombot, egészen addig amíg van zene a listában

#ITERABLE:
playlist = ["Warrior", "Meet your maker", "End the transmission", "I'm still fine"]
#ITERATOR
it = iter(playlist)
#ITERATION
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
