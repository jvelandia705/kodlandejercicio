import pygame
import random
from pygame.locals import *
from time import time

# Inicializar Pygame
pygame.init()

# Inicializar pygame.mixer
pygame.mixer.init()

# Definir algunas constantes
ANCHO, ALTO = 800, 600
FPS = 60
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Nave")

# Cargar imágenes con transparencia
nave_img = pygame.image.load('assets/nave.png').convert_alpha()
enemigo_img = pygame.image.load('assets/enemigo.png').convert_alpha()
disparo_img = pygame.image.load('assets/disparo.png').convert_alpha()

# Redimensionar imágenes
nave_img = pygame.transform.scale(nave_img, (50, 50))
enemigo_img = pygame.transform.scale(enemigo_img, (30, 30))
disparo_img = pygame.transform.scale(disparo_img, (5, 20))

# Cargar música y sonidos
pygame.mixer.music.load('assets/musica.mp3')
pygame.mixer.music.set_volume(0.2)
sonido_disparo = pygame.mixer.Sound('assets/disparo.wav')
sonido_explosion = pygame.mixer.Sound('assets/explosion.wav')

# Fuente para texto
fuente = pygame.font.SysFont("Arial", 40)

# Funciones del juego
def crear_enemigos(cantidad, enemigos):
    for _ in range(cantidad):
        enemigo = pygame.Rect(random.randint(0, ANCHO - 30), random.randint(-150, -50), 30, 30)
        enemigos.append(enemigo)

def mover_enemigos(enemigos):
    for enemigo in enemigos:
        enemigo.y += 2
        if enemigo.y > ALTO:
            enemigo.x = random.randint(0, ANCHO - 30)
            enemigo.y = random.randint(-150, -50)

def dibujar_proyectiles(proyectiles, ventana):
    for proyectil in proyectiles:
        ventana.blit(disparo_img, (proyectil.x, proyectil.y))

def mover_proyectiles(proyectiles):
    for proyectil in proyectiles:
        proyectil.y -= 5
        if proyectil.y < 0:
            proyectiles.remove(proyectil)

def verificar_colisiones(proyectiles, enemigos, puntuacion):
    for proyectil in proyectiles:
        for enemigo in enemigos:
            if proyectil.colliderect(enemigo):
                enemigos.remove(enemigo)
                proyectiles.remove(proyectil)
                puntuacion += 10
                sonido_explosion.play()
                break
    return puntuacion

def juego():
    # Variables del jugador y el juego
    jugador_x = ANCHO // 2 - 25
    jugador_y = ALTO - 100
    jugador_vel = 5
    jugador_dx = 0
    vidas = 3
    puntuacion = 0
    proyectiles = []
    enemigos = []

    # Temporizador para generar enemigos
    ultimo_enemigo_tiempo = 0
    TIEMPO_ENTRE_ENEMIGOS = 4000  # 4 segundos

    # Iniciar música de fondo
    pygame.mixer.music.play(-1, 0.0)

    # Crear enemigos iniciales
    crear_enemigos(6, enemigos)

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jugador_dx = -jugador_vel
                elif evento.key == pygame.K_RIGHT:
                    jugador_dx = jugador_vel
                elif evento.key == pygame.K_SPACE:
                    proyectil = pygame.Rect(jugador_x + 22, jugador_y, 5, 20)
                    proyectiles.append(proyectil)
                    sonido_disparo.play()
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    jugador_dx = 0

        # Mover al jugador
        jugador_x += jugador_dx
        if jugador_x < 0:
            jugador_x = 0
        elif jugador_x > ANCHO - 50:
            jugador_x = ANCHO - 50

        # Generar nuevos enemigos cada 4 segundos
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultimo_enemigo_tiempo > TIEMPO_ENTRE_ENEMIGOS:
            crear_enemigos(4, enemigos)
            ultimo_enemigo_tiempo = tiempo_actual

        # Mover enemigos y proyectiles
        mover_enemigos(enemigos)
        mover_proyectiles(proyectiles)
        puntuacion = verificar_colisiones(proyectiles, enemigos, puntuacion)

        # Comprobar si el jugador ha sido alcanzado por un enemigo
        for enemigo in enemigos:
            if pygame.Rect(jugador_x, jugador_y, 50, 50).colliderect(enemigo):
                vidas -= 1
                enemigos.remove(enemigo)
                if vidas <= 0:
                    return False  # Fin del juego

        # Dibujar elementos en la pantalla
        ventana.fill(NEGRO)
        ventana.blit(nave_img, (jugador_x, jugador_y))  # Dibujar la nave
        dibujar_proyectiles(proyectiles, ventana)
        for enemigo in enemigos:
            ventana.blit(enemigo_img, (enemigo.x, enemigo.y))

        # Mostrar puntuación y vidas
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
        ventana.blit(texto_puntuacion, (10, 10))
        texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
        ventana.blit(texto_vidas, (ANCHO - 150, 10))

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

    return True  # Continuar el juego




