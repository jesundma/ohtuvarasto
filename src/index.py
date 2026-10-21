from varasto import Varasto


def nayta_luonti(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")
    if mehua.paljonko_mahtuu() > 0:
        print("Mehuvarastoon mahtuu vielä tilaa")
    if mehua.paljonko_mahtuu() > 0 and olutta.paljonko_mahtuu() > 0:
        print("Olutvarastoon mahtuu vielä tilaa")
        print("Yhteensä varastoon mahtuu vielä tilaa")


def nayta_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def nayta_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def nayta_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def nayta_lisays(mehua, olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def nayta_oluen_otto(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def nayta_mehun_otto(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def nayta_otto(mehua, olutta):
    nayta_oluen_otto(olutta)
    nayta_mehun_otto(mehua)


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    nayta_luonti(mehua, olutta)
    nayta_getterit(olutta)
    nayta_setterit(mehua)
    nayta_virhetilanteet()
    nayta_lisays(mehua, olutta)
    nayta_otto(mehua, olutta)


if __name__ == "__main__":
    main()
