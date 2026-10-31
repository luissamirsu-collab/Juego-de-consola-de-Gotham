import random

from clases.enemigos import Enemigos
from clases.jugador import Jugador


def main():
    nombre_jugador = input(
        "Bienvenido a Ghotam, Dime quien eres: "
        )
    jugador = Jugador(nombre_jugador)
    enemigos = [
        Enemigos("Guason", 50, 10),
        Enemigos("Gatubela", 30, 5),
        Enemigos("Bane", 70, 15),
    ]
    enemigos_derrotados= []
    print("Comienza la noche")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue
        print(
            f"Te encontraste en la noche fria de Gotham a {enemigo_actual.nombre} en tu camino "
        )

        while enemigo_actual.salud > 0:
            accion = input(
                "Que accion deseas hacer? (atacar / huir) "
                ).lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"Haz atacado a {enemigo_actual.nombre} y le haz causado {dano_jugador} puntos de daño"
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"{enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de daño"
                    )
                    jugador.recibir_dano(dano_enemigo)

            elif accion == "huir":
                print(
                    "Haz decidido huir del combate por la lucha de la justicia en Gotham. COBARDE"
                )
                break

        if jugador.salud == 0:
            print("Haz perdido la partida")
            break
        if enemigo_actual.salud <=0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)

        jugador.ganar_experiencia(20)
        continuar = input(
            "Quieres seguir batallano por Gotham? (s/n): "
            ).lower()
        
        if continuar != "s":
            print("Gracias por Tratar de defender a Gotham")
    
            break
    if not enemigos:
        print("Felicidades haz derrotado a todos los enemigos")    
if __name__ == "__main__": # Nos asegura q solo podamos ejecutar este scrit desde el programa principal
    main()  
    
