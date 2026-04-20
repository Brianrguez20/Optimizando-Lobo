class Jugador:
    
    def __init__(self, nombre, rol):
        self.nombre = nombre
        self.rol = rol
        self.vivo = True
    
    def accion_noche(self, objetivo=None):
        if not self.vivo:
            return f"{self.nombre} esta muerto"
        
        if self.rol == "lobo":
            if objetivo:
                objetivo.vivo = False
                return f"{self.nombre} a eliminado a {objetivo.nombre}"
                
        elif self.rol == "vidente":
            if objetivo:
                return f"{self.nombre} descubre que {objetivo.nombre} es {objetivo.rol}"
                
        elif self.rol == "aldeano":
            return f"{self.nombre} duerme"
        
        return "Rol no valido"


class Partida:
    
    def __init__(self):
        self.jugadores = []
    
    def agregar_jugador(self, nombre, rol):
        self.jugadores.append(Jugador(nombre, rol))
    
    def votacion(self, nombre_acusado):
        for j in self.jugadores:
            if j.nombre == nombre_acusado and j.vivo:
                j.vivo = False
                return f"Linchan a {nombre_acusado}"
        return "No ubo linchamiento"
    
    def verificar_ganador(self):
        lobos_vivos = 0
        no_lobos_vivos = 0
        
        for j in self.jugadores:
            if j.vivo:
                if j.rol == "lobo":
                    lobos_vivos += 1
                else:
                    no_lobos_vivos += 1
        
        if lobos_vivos == 0:
            return "GANAN ALDEANOS"
        elif lobos_vivos >= no_lobos_vivos:
            return "GANAN LOBOS"
        else:
            return "Sigue el juego"


def main():
    print("\n" + "="*40)
    print("JUEGO DEL LOBO")
    print("="*40 + "\n")
    
    partida = Partida()
    partida.agregar_jugador("Nacho", "lobo")
    partida.agregar_jugador("Elena", "vidente")
    partida.agregar_jugador("Carlos", "aldeano")
    partida.agregar_jugador("Lucia", "aldeano")
    
    print("JUGADORES:")
    for j in partida.jugadores:
        print(f"   - {j.nombre} ({j.rol})")
    
    print("\nNOCHE")
    print(partida.jugadores[0].accion_noche(partida.jugadores[2]))
    
    print("\nVIDENTE:")
    print(partida.jugadores[1].accion_noche(partida.jugadores[0]))
    
    print("\nVERIFICAR:")
    print(partida.verificar_ganador())
    
    print("\nDIA")
    print(partida.votacion("Nacho"))
    
    print("\nESTADO FINAL:")
    for j in partida.jugadores:
        estado = "VIVO" if j.vivo else "MUERTO"
        print(f"   - {j.nombre} ({j.rol}): {estado}")
    
    print("\n" + partida.verificar_ganador())
    print("\n" + "="*40)

if __name__ == "__main__":
    main()
