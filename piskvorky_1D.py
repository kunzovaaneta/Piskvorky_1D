def vyhodnot(hraci_pole):
    assert 'x' or 'o' or '-' in hraci_pole #kontrola, zda v poli jsou povolené znaky
    if 'xxx' in hraci_pole:
        return 'x' #vyhrál hráč s x
    elif 'ooo' in hraci_pole:
        return 'o' #vyhrál hráč s o
    elif '-' not in hraci_pole:
        return '!' #remiza
    else:
        return '-' #hra pokračuje dále
#print(vyhodnot(hraci_pole))

def tah(hraci_pole, pozice, znak):
    hraci_pole = hraci_pole[:pozice] + znak + hraci_pole[(pozice+1):]
    return hraci_pole
#print(tah(hraci_pole, 2, 'o'))

def tah_hrace(hraci_pole):
    while True:
        pozice = int(input('Zadej číslo pozice, na kterou chceš hrát: '))
        znak = 'x' # hráč má defaultně křížek
        if pozice > len(hraci_pole) or pozice < 0:
            print('Upss, zadal jsi číslo mimo rozsah (0-19), zkus to znovu.')
        elif hraci_pole[pozice] != '-':
           print ('Upss, na pozici {p} je už obsazeno, zkus to jinde.'.format(p=pozice))
        else:
            return tah(hraci_pole, pozice, znak)  
#print(tah_hrace(hraci_pole))

def tah_pocitace(hraci_pole):
    import random
    znak = 'o' # počítač má defaultně o
    while True:
        pozice = random.randint(0,19)
        if hraci_pole[pozice] != '-':
            print ('Upss, na pozici {p} je už obsazeno, zkus to jinde.'.format(p=pozice))
        else:
            print ('Počítač hrál na pozic: {p}'.format(p=pozice))
            return tah(hraci_pole, pozice, znak)  
#print(tah_pocitace(hraci_pole))

def hra():
    hraci_pole = 20 * '-'
    na_tahu = 'x'
    while True:
        print('Hrací pole: {h}'.format(h=hraci_pole))
        if na_tahu == 'x':
            hraci_pole = tah_hrace(hraci_pole)
            na_tahu = 'o'
        elif na_tahu == "o":
            hraci_pole = tah_pocitace(hraci_pole)
            na_tahu = 'x'
        
        if vyhodnot(hraci_pole) == 'x':
            return 'Vyhrál hráč'
            break
        elif vyhodnot(hraci_pole) == 'o':
            return 'Vyhrál počítač'
            break
        elif vyhodnot(hraci_pole) == '!':
            return 'Remíza nikdo nevyhrál'
            break
      
print(hra())

