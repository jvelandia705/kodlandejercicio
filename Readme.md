# Juego de Nave (Space Shooter)

Este es un juego clásico de **Space Shooter** en 2D, desarrollado con **Pygame**, donde controlas una nave espacial para disparar a los enemigos y evitar colisiones. El objetivo es sobrevivir el mayor tiempo posible y acumular puntuación destruyendo enemigos.

## Funcionalidad del Juego

### Características principales:
- **Nave jugable**: Controlas una nave que se mueve horizontalmente por la pantalla.
- **Disparos**: La nave puede disparar proyectiles hacia arriba para destruir a los enemigos.
- **Enemigos**: Los enemigos se generan en la parte superior de la pantalla y descienden hacia el jugador.
- **Colisiones**: Si un proyectil de la nave golpea a un enemigo, el enemigo es destruido y se suma puntos al jugador. Si el jugador choca con un enemigo, pierde una vida.
- **Puntuación**: Cada enemigo destruido suma puntos al jugador.
- **Vidas**: El jugador comienza con 3 vidas. Si se queda sin vidas, el juego termina.
- **Pantalla de Fin de Juego**: Cuando el jugador pierde todas sus vidas, se muestra una pantalla de fin de juego con opciones para reiniciar o salir.

### Controles:
- **Teclas de dirección izquierda y derecha**: Mueven la nave a la izquierda o derecha.
- **Espacio (Space)**: Dispara un proyectil desde la nave.
- **Enter**: Inicia el juego desde el menú principal.
- **R**: Reinicia el juego después de perder.
- **Esc (Escape)**: Sale del juego.

### Pantallas del juego:
1. **Menú principal**: Se muestra al iniciar el juego, donde puedes elegir comenzar a jugar o salir.
2. **Pantalla de juego**: Durante el juego, se muestra la nave, los enemigos, los proyectiles y la puntuación actual.
3. **Pantalla de fin de juego**: Si el jugador pierde, se muestra esta pantalla con la opción de reiniciar o salir.

### Lógica de juego:
- El jugador puede moverse de izquierda a derecha y disparar hacia arriba para destruir los enemigos.
