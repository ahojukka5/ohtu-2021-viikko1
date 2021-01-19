import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus(self):
        self.assertAlmostEqual(Varasto(-1.0).tilavuus, 0.0)

    def test_virheellinen_alkusaldo(self):
        self.assertAlmostEqual(Varasto(1.0, alku_saldo = -1.0).saldo, 0.0)

    def test_lisaa_virheellinen_maara(self):
        self.varasto.lisaa_varastoon(-1.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_lisaa_normaalisti(self):
        self.varasto.lisaa_varastoon(1.0)
        self.assertAlmostEqual(self.varasto.saldo, 1.0)

    def test_lisaa_yli_paljonko_mahtuu(self):
        self.varasto.lisaa_varastoon(11.0)
        self.assertAlmostEqual(self.varasto.saldo, 10.0)

    def test_ota_varastosta_negatiivinen_maara(self):
        m = self.varasto.ota_varastosta(-1.0)
        self.assertAlmostEqual(m, 0.0)

    def test_ota_varastosta_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(1.0)
        m = self.varasto.ota_varastosta(2.0)
        self.assertAlmostEqual(m, 1.0)

    def test_tulosta_varasto(self):
        s = str(self.varasto)
        self.assertEqual(s, "saldo = 0, vielä tilaa 10")
