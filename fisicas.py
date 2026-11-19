def actualizar_posicion(x, y, vx, vy, dt):
    nueva_x = x + vx * dt
    nueva_y = y + vy * dt
    return nueva_x, nueva_y

def rebotar_paredes(x, y, vx, vy, radio, ancho, alto):

    e = 1.0  # Coeficiente de restitución

    # Pared derecha
    if x + radio >= ancho:
        x = ancho - radio
        vx = -abs(vx) * e

    # Pared izquierda
    elif x - radio <= 0:
        x = radio
        vx = abs(vx) * e

    # Pared inferior
    if y + radio >= alto:
        y = alto - radio
        vy = -abs(vy) * e

    # Pared superior
    elif y - radio <= 0:
        y = radio
        vy = abs(vy) * e

    return x, y, vx, vy