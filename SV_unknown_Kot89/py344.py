import asyncio

# SOLID: Single Responsibility Principle
# Fiecare corutina face un singur lucru clar (inmultire, adunare, anulare).
# Pipeline-ul doar deleaga executia in ordine.

async def inmultire_constanta(dict_date: dict, constanta: int):
    # Prima corutina inmulteste elementele cu o constanta
    for k in dict_date:
        dict_date[k] *= constanta
    return dict_date

async def adunare_doua_cate_doua(dict_date: dict):
    # A doua corutina aduna doua cate doua si suprascrie in primul loc
    chei = list(dict_date.keys())
    for i in range(0, len(chei) - 1, 2):
        k1 = chei[i]
        k2 = chei[i+1]
        dict_date[k1] = dict_date[k1] + dict_date[k2]
    return dict_date

async def anulare_elemente_pare(dict_date: dict):
    # A treia corutina inlocuieste cu 0 valorile pare
    for k in dict_date:
        if dict_date[k] % 2 == 0:
            dict_date[k] = 0
    return dict_date

async def pipeline_asincron(dict_date: dict):
    # Se construieste pipeline-ul asteptand dupa futures
    await inmultire_constanta(dict_date, 2)
    await adunare_doua_cate_doua(dict_date)
    await anulare_elemente_pare(dict_date)
    return dict_date

def main():
    date = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
    
    # Rulam pipeline-ul asincron folosind asyncio.run
    rezultat = asyncio.run(pipeline_asincron(date))
    
    print("Dictionar rezultat in urma pipeline-ului asyncio:", rezultat)

if __name__ == "__main__":
    main()
