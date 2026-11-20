import math 

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

def aplicar_fricciones(vx, vy, dt):
    
    mu = 0.08
    g = 981 #error aca
    
    velocidad = math.sqrt(vx**2 + vy**2)
    if velocidad == 0:
        return 0, 0
    
    desacelaricion = mu * g
    nueva_velocidad = max(0, velocidad - desacelaricion * dt)
    
    factor = nueva_velocidad/ velocidad
    
    vx = vx*factor
    vy = vy*factor
    
    return vx, vy
    