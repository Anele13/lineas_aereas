import unittest
from main import CompaniaAerea, Paquete, Ciudad

class TestCompaniaAerea(unittest.TestCase):
    def setUp(self):
        self.ciudad_origen = Ciudad('Trelew')
        self.ciudad_destino = Ciudad('Gaiman')
        self.compania = CompaniaAerea('Linea Aerea 1')

    def test_agregar_paquete(self):
        fecha = "2024-09-14"
        #Agrega paquete de cliente
        paquete1 = Paquete(self.ciudad_origen, self.ciudad_destino)
        self.compania.agregar_paquete(paquete1, fecha)
        self.assertEqual(len(self.compania.paquetes), 1)
        self.assertEqual(self.compania.paquetes.get(fecha)[0].id, paquete1.id)

        #Paquete no es de tipo cliente
        paquete2 = Paquete(self.ciudad_origen, self.ciudad_destino, Paquete.TIPO_DESCONOCIDO)
        self.compania.agregar_paquete(paquete2, fecha)
        self.assertEqual(len(self.compania.paquetes[fecha]), 1)
        self.assertNotEqual(self.compania.paquetes.get(fecha)[0].id, paquete2.id)

    def test_paquetes_en_fecha(self):
        fecha1 = '2025-01-01'
        paquete1 = Paquete(self.ciudad_origen, self.ciudad_destino)
        paquete2 = Paquete(self.ciudad_origen, self.ciudad_destino)
        paquete3 = Paquete(self.ciudad_origen, self.ciudad_destino)
        paquete4 = Paquete(self.ciudad_origen, self.ciudad_destino)
        
        #Agregar un paquete
        self.compania.agregar_paquete(paquete1, fecha1)
        paquetes_transportados, total_recaudado = self.compania.paquetes_en_fecha(fecha1)
        self.assertEqual(paquetes_transportados, 1)
        self.assertEqual(total_recaudado, 10)

        #Mas de un paquete
        self.compania.agregar_paquete(paquete2, fecha1)
        paquetes_transportados, total_recaudado = self.compania.paquetes_en_fecha(fecha1)
        self.assertEqual(paquetes_transportados, 2)
        self.assertEqual(total_recaudado, 20)

        #Sin paquetes en fecha
        fecha2 = '2024-09-16'
        paquetes_transportados, total_recaudado = self.compania.paquetes_en_fecha(fecha2)
        self.assertEqual(paquetes_transportados, 0)
        self.assertEqual(total_recaudado, 0)
    
        #Transportados en distintas fechas
        self.compania.agregar_paquete(paquete3, fecha2)
        paquetes_transportados, total_recaudado = self.compania.paquetes_en_fecha(fecha2)
        self.assertEqual(paquetes_transportados, 1)
        self.assertEqual(total_recaudado, 10)

        #La compañia actualiza su tarifas de envio a 150
        self.compania.TARIFA_POR_PAQUETE = 150

        #Agregar paquete con monto actualizado
        self.compania.agregar_paquete(paquete4, fecha1)
        paquetes_transportados, total_recaudado = self.compania.paquetes_en_fecha(fecha1)
        self.assertEqual(paquetes_transportados, 3)
        self.assertEqual(total_recaudado, 170)