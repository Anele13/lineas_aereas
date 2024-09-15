from collections import defaultdict
import uuid

class Ciudad:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'{self.name}'

class Paquete:
    TIPO_CLIENTE = 1
    TIPO_DESCONOCIDO = 2

    def __init__(self, ciudad_origen, ciudad_destino, tipo=TIPO_CLIENTE):
        self.id = uuid.uuid1()
        self.origen = ciudad_origen
        self.destino = ciudad_destino
        self.tipo = tipo
        self.costo_traslado = 0

    def __str__(self):
        return (f'PAQUETE: {self.id} - DESDE: {self.origen} -'
                f'HASTA: {self.destino} - COSTO: {self.costo_traslado}')

class CompaniaAerea:
    TARIFA_POR_PAQUETE = 10
    
    def __init__(self, name):
        self.nombre = name
        self.paquetes = defaultdict(list)

    def __str__(self):
        return f'{self.nombre}'
    
    def agregar_paquete(self, paquete, fecha):
        """
        Agrega paquetes solo del 
        tipo cliente
        """
        if paquete.tipo == Paquete.TIPO_CLIENTE:
            paquete.costo_traslado = self.TARIFA_POR_PAQUETE
            self.paquetes[fecha].append(paquete)

    def paquetes_en_fecha(self, fecha):
        """
        Devuelve tupla indicando
        (cantidad_paquetes, tarifa_total)
        en una fecha determinada
        En caso de no haber paquetes devuelve
        (0,0)
        """
        respuesta = (0,0)
        paquetes_en_fecha = self.paquetes.get(fecha)
        if paquetes_en_fecha:
            respuesta = (
                len(paquetes_en_fecha),
                sum([paquete.costo_traslado for paquete in paquetes_en_fecha])
            )
        return respuesta

    def reporte(self, fecha):
        """
        Genera un reporte de cantidad
        de paquetes y costos en una 
        fecha especifica
        """
        cantidad_paquetes, costo_total = self.paquetes_en_fecha(fecha)
        if cantidad_paquetes:
            print(f'fecha: {fecha} | cantidad de paquetes: {cantidad_paquetes} | costo total: {costo_total}')

if __name__ == '__main__':
    ciudad_origen = Ciudad('Trelew')
    ciudad_destino = Ciudad('Gaiman')
    compania = CompaniaAerea('Linea del sol')

    #Sin paquetes transportados
    fecha1 = '2024-09-14'
    print(f'Reporte para {fecha1} (Sin paquetes cargados)')
    compania.reporte(fecha1)

    #Sin paquetes en fecha
    fecha2 = '2024-09-16'
    print(f'Reporte para {fecha2} (Sin paquetes en esa fecha)') 
    compania.reporte(fecha2)
    
    #Un solo paquete transportado
    print(f'Reporte para {fecha2} (despues de agregar un paquete)') 
    paquete1 = Paquete(ciudad_origen, ciudad_destino)
    print(paquete1)
    compania.agregar_paquete(paquete1, fecha1)
    compania.reporte(fecha1)

    #Muchos paquetes para la misma fecha
    print(f'Reporte para {fecha1} (después de agregar más paquetes para la misma fecha)')
    paquete2 = Paquete(ciudad_origen, ciudad_destino)
    paquete3 = Paquete(ciudad_origen, ciudad_destino)
    compania.agregar_paquete(paquete2, fecha1)
    compania.agregar_paquete(paquete3, fecha1)
    compania.reporte(fecha1)

    #Transportados en distintas fechas
    fecha3 = '2024-09-15'
    print(f'Reporte para {fecha3} (con paquetes en distintas fechas)')
    paquete4 = Paquete(ciudad_origen, ciudad_destino)
    compania.agregar_paquete(paquete4, fecha3)
    compania.reporte(fecha3)