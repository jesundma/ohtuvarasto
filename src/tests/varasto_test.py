import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
    
    def test_konstruktori_luo_tyhjan_varaston(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    # --- Mandatory Branch Coverage Expansions ---

    # 1. Constructor Branches
    def test_konstruktori_virheellinen_tilavuus_nollataan(self):
        # Covers: 'else' branch of 'if tilavuus > 0.0'
        huono_varasto = Varasto(-5)
        self.assertAlmostEqual(huono_varasto.tilavuus, 0.0)

    def test_konstruktori_virheellinen_alkusaldo_nollataan(self):
        # Covers: 'if alku_saldo < 0.0' branch
        huono_varasto = Varasto(10, -3)
        self.assertAlmostEqual(huono_varasto.saldo, 0.0)

    def test_konstruktori_alkusaldo_suurempi_kuin_tilavuus(self):
        # Covers: 'else' branch where 'alku_saldo > tilavuus'
        liian_taysi = Varasto(10, 15)
        self.assertAlmostEqual(liian_taysi.saldo, 10.0)

    # 2. Method: lisaa_varastoon Branches
    def test_lisays_negatiivinen_maara_ei_muuta_saldoa(self):
        # Covers: 'if maara < 0' branch
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisays_yli_vapaan_tilan_tayttaa_varaston(self):
        # Covers: 'else' branch of 'if maara <= self.paljonko_mahtuu()'
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10.0)

    # 3. Method: ota_varastosta Branches
    def test_ottaminen_negatiivinen_maara_palauttaa_nollan(self):
        # Covers: 'if maara < 0' branch
        saatu = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu, 0.0)

    def test_ottaminen_enemman_kuin_varastossa_tyhjentaa_varaston(self):
        # Covers: 'if maara > self.saldo' branch
        self.varasto.lisaa_varastoon(5)
        saatu = self.varasto.ota_varastosta(8)
        self.assertAlmostEqual(saatu, 5.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    # 4. Method: __str__ Branch
    def test_merkkijonoesitys_tulostuu_oikein(self):
        # Covers: __str__ string formatting conversion evaluation
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(str(self.varasto), "VIRHE = 4, vielä tilaa 6")
