ser_info = { 
"name": "Mike", 
"age": 25, 
"favourite_meals": [ 
"pizza", 
"carbonara", 
"sushi" 
], 
"phone_contacts": { 
"Mary": "+36701234567", 
"Tim": "+36207654321", 
"Tim2": "+36304567321", 
"Jim": "+364005000" 
} 
} 
# 1.
prog_lang = input("Négy prog. nyelv vesszővel elválasztva: ")
prog_list = prog_lang.split(",")    # stringet listává konvertál
ser_info["skills"] = prog_list      #hozzáadja a listát
print(ser_info)
#2. Rendezd a favourite_meals lista elemeit abc szerinti növekvő sorrendbe. 
ser_info["favourite_meals"].sort()
print(ser_info["favourite_meals"])
#3. Printeld ki a favourite_meals lista utolsó előtti elemét 
print(ser_info["favourite_meals"][-2])
#4. Adj hozzá egy “spaghetti” string-et ugyanehhez a listához. 
ser_info["favourite_meals"].append("spaghetti")
#print(ser_info["favourite_meals"]) 
#5. Add hozzá a favourite_meals-hez az aktuális favourite_meals lista harmadik és negyedik elemét (nem az index-ét) újra. 
ser_info["favourite_meals"].append(ser_info["favourite_meals"][2]) #3. elem inbdexe 2
ser_info["favourite_meals"].append(ser_info["favourite_meals"][3])

#7. Cseréld fel a favourite_meals lista első és utolsó elemét! 
tempor_var = ser_info["favourite_meals"][0]                         # első elem ideiglenes változóba
ser_info["favourite_meals"][0] = ser_info["favourite_meals"][-1],    #első elem helyére az utolsót teszi
ser_info["favourite_meals"][-1] = ser_info                          #utolsó elem helyére beteszi az elmentett régi első elemet

#8. A “phone_contacts” dictionary-hez adj hozzá egy új elemet, tetszőleges névvel és telefonszámmal.
ser_info["phone_contacts"]["Tom"] = "+36304563210"
print(ser_info["phone_contacts"]) 
