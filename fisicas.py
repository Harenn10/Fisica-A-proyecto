import math 

def actualizar_posicion(x, y, vx, vy, dt):
    nueva_x = x + vx * dt
    nueva_y = y + vy * dt
    return nueva_x, nueva_y

def rebotar_paredes( x, y, vx, vy, radio, ancho, alto, margen=0):
    e = 1.0
    # Pared derecha
    if x + radio >= ancho - margen:
        x = ancho - margen - radio
        vx = -abs(vx) * e

    # Pared izquierda
    elif x - radio <= margen:
        x = margen + radio
        vx = abs(vx) * e

    # Pared inferior
    if y + radio >= alto - margen:
        y = alto - margen - radio
        vy = -abs(vy) * e

    # Pared superior
    elif y - radio <= margen:
        y = margen + radio
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
    
    
def colision_bolas(bola1, bola2, restitucion = 1.0):
    dx = bola2.x - bola1.x
    dy = bola2.y - bola1.y
    
    distancia = (dx**2 + dy**2)**0.5 #####3
    radio_total =bola1.radio + bola2.radio
    
    if distancia > radio_total: #Estan chocando??
        return False 
    
    if distancia == 0:
        nx = 1.0
        ny = 0.0
    else:
        nx = dx/distancia
        ny = dy/distancia
        
    solapamiento = radio_total - distancia #Separarlas
    
    bola1.x -= nx *solapamiento/2
    bola1.y -= ny*solapamiento/2
    bola2.x -= nx *solapamiento/2
    bola2.y -= ny*solapamiento/2
    
    velocidad_relativa = (
        (bola2.vx-bola1.vx)*nx-(bola2.vy-bola1.vy)*ny #direccion
    )
    
    if velocidad_relativa>=0:
        return True #si se separan no se aplica el impulso
    
    impulso = -(1 + restitucion) * velocidad_relativa / 2

    bola1.vx -= impulso * nx
    bola1.vy -= impulso * ny
    bola2.vx += impulso * nx
    bola2.vy += impulso * ny

    return True