import pygame
import sys
from menu import mostrar_menu, mostrar_fin_juego
from game import juego

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crear la ventana
pygame.display.set_caption("Invasores del Espacio")

# Función principal
def main():
    corriendo = True
    while corriendo:
        mostrar_menu(ventana)  # Pasar ventana como argumento a mostrar_menu()

        # Detectar teclas para navegar en el menú
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:  # Empezar el juego
                    if not juego():  # Si el juego termina, mostrar fin de juego
                        mostrar_fin_juego(ventana)  # Pasar ventana como argumento a mostrar_fin_juego()
                        fin_juego = True
                        while fin_juego:
                            for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:
                                    fin_juego = False
                                    corriendo = False
                                if evento.type == pygame.KEYDOWN:
                                    if evento.key == pygame.K_r:  # Reiniciar el juego
                                        juego()
                                        fin_juego = False
                                    elif evento.key == pygame.K_ESCAPE:  # Salir del juego
                                        fin_juego = False
                                        corriendo = False

                elif evento.key == pygame.K_ESCAPE:  # Salir del juego
                    corriendo = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
