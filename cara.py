import pygame
import time
import random

def dibuixar_cara():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    # Colors
    blau_clar = (135, 206, 250)
    groc = (255, 223, 0)
    negre = (0, 0, 0)
    blanc = (255, 255, 255)
    vermell = (200, 0, 0)
    rosa = (255, 182, 193)
    gris = (169, 169, 169)
    blanc_llamp = (255, 255, 255)

    running = True
    tancant_ulls = False

    # Coordenades de la cara (evitar rayos en esta zona)
    cara_rect = pygame.Rect(250, 150, 300, 300)  # (x, y, width, height)

    def dibuixar_pluja():
        for _ in range(50):  # Crear 50 línies de pluja
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            pygame.draw.line(screen, gris, (x, y), (x, y + random.randint(10, 30)), 2)

    def dibuixar_llamps():
        # Incrementar la probabilitat de llamps
        if random.random() < 0.1:  # 10% de probabilitat de llamps
            x_inici = random.randint(0, 800)
            x_final = random.randint(0, 800)

            # Asegurarse de que el rayo no pase por la cara
            while cara_rect.collidepoint(x_inici, 0) or cara_rect.collidepoint(x_final, 600):
                x_inici = random.randint(0, 800)
                x_final = random.randint(0, 800)

            # Dibujar rayo quebrado
            puntos_rayo = [(x_inici, 0)]
            for i in range(4):  # Crear segmentos en el rayo
                x_nuevo = puntos_rayo[-1][0] + random.randint(-30, 30)
                y_nuevo = puntos_rayo[-1][1] + random.randint(50, 150)
                if y_nuevo > 600:
                    y_nuevo = 600
                puntos_rayo.append((x_nuevo, y_nuevo))
            puntos_rayo.append((x_final, 600))

            # Dibujar el rayo
            pygame.draw.lines(screen, blanc_llamp, False, puntos_rayo, 5)

    while running:
        screen.fill(blau_clar)  # Fons blau cel

        # Dibuixar pluja
        dibuixar_pluja()

        # Dibuixar llamps aleatoris
        dibuixar_llamps()

        # Cara rodona
        pygame.draw.circle(screen, groc, (400, 300), 150)
        pygame.draw.circle(screen, negre, (400, 300), 150, 5)

        # Galtes rosades
        pygame.draw.circle(screen, rosa, (320, 340), 25)
        pygame.draw.circle(screen, rosa, (480, 340), 25)

        if not tancant_ulls:
            # Ulls oberts
            pygame.draw.ellipse(screen, blanc, (310, 230, 70, 100))
            pygame.draw.ellipse(screen, blanc, (420, 230, 70, 100))
            pygame.draw.circle(screen, negre, (345, 270), 20)
            pygame.draw.circle(screen, negre, (455, 270), 20)
            pygame.draw.circle(screen, blanc, (338, 260), 7)
            pygame.draw.circle(screen, blanc, (448, 260), 7)

            # Boca oberta
            pygame.draw.ellipse(screen, negre, (340, 370, 120, 70))
            pygame.draw.arc(screen, negre, (340, 370, 120, 70), 0, 3.14, 5)

            # Llengua vermella
            pygame.draw.ellipse(screen, vermell, (370, 400, 60, 30))

            # Dents blanques
            pygame.draw.rect(screen, blanc, (370, 370, 20, 15))
            pygame.draw.rect(screen, blanc, (390, 370, 20, 15))
            pygame.draw.rect(screen, blanc, (410, 370, 20, 15))
            pygame.draw.line(screen, negre, (390, 370), (390, 385), 2)
            pygame.draw.line(screen, negre, (410, 370), (410, 385), 2)

        else:
            # Ulls tancats
            pygame.draw.line(screen, negre, (310, 270), (380, 270), 5)
            pygame.draw.line(screen, negre, (420, 270), (490, 270), 5)

            # Boca tancada (simulada por una línea recta)
            pygame.draw.line(screen, negre, (340, 410), (460, 410), 5)

        # Celles aixecades
        pygame.draw.line(screen, negre, (300, 200), (360, 190), 5)
        pygame.draw.line(screen, negre, (440, 190), (500, 200), 5)

        pygame.display.flip()

        # Parpelleig cada cert temps
        time.sleep(1.5)
        tancant_ulls = not tancant_ulls

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


dibuixar_cara()
