#Імпортуємо всяке-всіляке
import json
import requests
import os
import time

#Нескінченний цикл раз в 10 секунд
while 1:
    os.system("cls")
    r = requests.get('https://sirens.in.ua/api/v1/')
    status_ar = r.text
    data = json.loads(status_ar) #
    
    #Словничок щоб назвати місто по своєму)
    nmpls = {
        "Chernivtsi": "Рідні Чернівці 🥰"
    }
    
    trivogas = 0
    trivog_obl = []
    
    #Проходимось по областях в данних (я дибіл написав район)
    for rayon in data:
        st_ra = str(data[rayon])
        if st_ra == "None":
            st_ra = "Все тихо... ✔️"
        if st_ra == "no_data":
            st_ra = "Нема інфи( 📡"
        if st_ra == "full":
            st_ra = "капец, тікай в підвал ❌"
            trivogas += 1
            trivog_obl.append(rayon)
    
        #Дістаємо з словника назву, якщо нема то те що було спарсено
        rayon = nmpls.get(rayon, rayon)

        print(str(rayon) + " ->", st_ra)

    print("Всього тривог: ", str(trivogas) +", в", *trivog_obl)
        
    time.sleep(10)