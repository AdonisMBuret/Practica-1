# Juego de Aventura Simple con IF
print("¡Bienvenido a la Aventura!")
print("Te encuentras en un bosque oscuro. Debes tomar decisiones...")

# Primera decision
print("\n1. Te encuentras con dos caminos:")
print("a) Camino izquierdo - parece oscuro y misterioso")
print("b) Camino derecho - parece mas iluminado")

opcion1 = input("¿Que camino eliges? (a/b): ").lower()

if opcion1 == "a":
    print("\nCaminas por el sendero oscuro...")
    print("Encuentras una cueva misteriosa.")
    
    # Segunda decision
    print("\n2. ¿Que haces con la cueva?")
    print("a) Entrar a explorar")
    print("b) Continuar por el camino")
    
    opcion2 = input("Elige (a/b): ").lower()
    
    if opcion2 == "a":
        print("\n¡Encontraste un tesoro oculto! 🏆")
        print("¡Felicidades, ganaste el juego!")
    else:
        print("\nContinuas caminando pero te pierdes en el bosque.")
        print("Game Over ❌")
        
elif opcion1 == "b":
    print("\nCaminas por el sendero iluminado...")
    print("Encuentras un rio caudaloso.")
    
    # Segunda decision
    print("\n2. ¿Como cruzas el rio?")
    print("a) Nadar a traves de el")
    print("b) Buscar un puente")
    
    opcion2 = input("Elige (a/b): ").lower()
    
    if opcion2 == "a":
        print("\nLa corriente era muy fuerte y te arrastro.")
        print("Game Over ❌")
    else:
        print("\nEncuentras un puente seguro y cruzas exitosamente.")
        print("¡Llegaste a la civilizacion! 🎉")
        print("¡Felicidades, ganaste el juego!")
        
else:
    print("\nNo elegiste una opcion valida.")
    print("Te quedas paralizado por la indecision.")
    print("Game Over ❌")

print("\n¡Gracias por jugar 🤞!")