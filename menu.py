import pygame

# Función para mostrar el menú principal
def mostrar_menu(ventana):
    ventana.fill((0, 0, 0))
    fuente = pygame.font.SysFont("Arial", 40)
    texto = fuente.render("¡Bienvenido al Juego!", True, (255, 255, 255))
    ventana.blit(texto, (400 - texto.get_width() // 2, 150))
    texto_jugar = fuente.render("Presiona ENTER para JUGAR", True, (255, 255, 255))
    ventana.blit(texto_jugar, (400 - texto_jugar.get_width() // 2, 250))
    texto_salir = fuente.render("Presiona ESC para SALIR", True, (255, 255, 255))
    ventana.blit(texto_salir, (400 - texto_salir.get_width() // 2, 350))
    pygame.display.update()

# Función para mostrar la pantalla de fin de juego
def mostrar_fin_juego(ventana):
    ventana.fill((0, 0, 0))
    fuente = pygame.font.SysFont("Arial", 40)
    texto = fuente.render("¡FIN DEL JUEGO!", True, (255, 0, 0))
    ventana.blit(texto, (400 - texto.get_width() // 2, 150))
    texto_reiniciar = fuente.render("Presiona R para REINICIAR", True, (255, 255, 255))
    ventana.blit(texto_reiniciar, (400 - texto_reiniciar.get_width() // 2, 250))
    texto_salir = fuente.render("Presiona ESC para SALIR", True, (255, 255, 255))
    ventana.blit(texto_salir, (400 - texto_salir.get_width() // 2, 350))
    pygame.display.update()



