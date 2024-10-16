#generator losowych liczb

print("Wiatj w naszym klaskulatorze podatkowym!")
q1 = str(input("Z jakiego klakulatrora chcesz korzytsać? 1.Policz ile podaktów zostanie odciągniętych od twojej pensji."))
if q1 == "1":
    wynagrodzenie = float(input(("Dobrze zatem podaj nam ile będziesz dostawał netto (bez podatków.):  ")))
    podatek = str(input("Jaka stawka podaku obowiązuje ciebie? 17% czy 32%: "))
    ulgi = str(inpu("CZy masz mniej niz 26 lat? Tak/Nie:  "))
    if podatek == "17%":
        brutto = ((wynagrodzenie * 0.83) - (wynagrodzenie * 0.0775 ))
        print(f"Twoja pensja po odliczneiu {brutto} PLN.")
    elif podatek == "32%":

    
    else:

