from pygame.locals import *
import pygame

# Constants
AMPLADA = 800
ALTURA = 600
BACKGROUND_IMAGE = 'assets/fons.png'
MUSICA_FONS = 'assets/musica.mp3'
MUSICA_MENU = 'assets/musica_menu.mp3'  # Música diferent per al menú principal
MUSICA_GAME_OVER = 'assets/game_over.mp3'  # Música de Game Over
IMPACTE_BALES = 'assets/impacte_bales.mp3'  # Afegim el camí de l'arxiu d'impacte de les bales
WHITE = (255, 255, 255)
MAGENTA = (255, 0, 255)

# pantalles del joc
pantalla_actual = 1  # Iniciar al menú

# Jugador 1:
player_image = pygame.image.load('assets/nau.png')
player_rect = player_image.get_rect(midbottom=(AMPLADA // 2, ALTURA - 10))
velocitat_nau = 15

# Jugador 2:
player_image2 = pygame.image.load('assets/enemic.png')
player_rect2 = player_image2.get_rect(midbottom=(AMPLADA // 2, ALTURA - 500))
velocitat_nau2 = 15

# vides:
vides_jugador1 = 3
vides_jugador2 = 3
vides_jugador1_image = pygame.image.load('assets/vida2.png')
vides_jugador2_image = pygame.image.load('assets/vida1.png')

# Bales:
bala_imatge1 = pygame.image.load('assets/bala1.png')  # Imatge bala jugador 1
bala_imatge2 = pygame.image.load('assets/bala2.png')  # Imatge bala jugador 2
bales_jugador1 = []  # llista on guardem les bales del jugador 1
bales_jugador2 = []  # llista on guardem les bales del jugador 2
velocitat_bales = 30
temps_entre_bales = 350  # 0.35 milisegons
temps_ultima_bala_jugador1 = 0  # per contar el temps que ha passat des que ha disparat el jugador 1
temps_ultima_bala_jugador2 = 0  # per contar el temps que ha passat des que ha disparat el jugador 2

pygame.init()
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arcade")

# Carregar la música de fons
pygame.mixer.music.load(MUSICA_MENU)  # Música per al menú principal
pygame.mixer.music.play(-1)  # Reproduir música de fons de manera continuada

# Carregar el so d'impacte
impacte_so = pygame.mixer.Sound(IMPACTE_BALES)

# Control de FPS
clock = pygame.time.Clock()
fps = 30

def imprimir_pantalla_fons(image):
    # Imprimeixo imatge de fons:
    background = pygame.image.load(image).convert()
    pantalla.blit(background, (0, 0))

def mostrar_vides():
    # Mostrar les vides a la pantalla
    for i in range(vides_jugador1):
        pantalla.blit(vides_jugador1_image, (10 + i * 40, 10))  # Vides jugador 1 a dalt a l'esquerra
    for i in range(vides_jugador2):
        pantalla.blit(vides_jugador2_image, (AMPLADA - (i + 1) * 40 - 10, ALTURA - 50))  # Vides jugador 2 a sota a la dreta


while True:
    # Contador
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if pantalla_actual == 4:  # Game Over
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # Reiniciar el joc
                    vides_jugador1 = 3
                    vides_jugador2 = 3
                    pantalla_actual = 3
                    for i in bales_jugador1:
                        bales_jugador1.remove(i)
                    for i in bales_jugador2:
                        bales_jugador2.remove(i)

                    # Aturar la música de Game Over i tornar a la música de fons
                    pygame.mixer.music.stop()  # Detener la música actual
                    pygame.mixer.music.load(MUSICA_FONS)  # Carregar música de fons
                    pygame.mixer.music.play(-1)  # Reproducir música de fons de manera continuada
                else:
                    event.key == K_ESCAPE
                    quit()

        if pantalla_actual == 3:  # Joc
            # controlar trets de les naus
            if event.type == KEYDOWN:
                # jugador 1
                if event.key == K_w and current_time - temps_ultima_bala_jugador1 >= temps_entre_bales:
                    bales_jugador1.append(pygame.Rect(player_rect.centerx - 2, player_rect.top, 4, 10))
                    temps_ultima_bala_jugador1 = current_time
                # jugador 2
                if event.key == K_i and current_time - temps_ultima_bala_jugador2 >= temps_entre_bales:
                    bales_jugador2.append(pygame.Rect(player_rect2.centerx - 2, player_rect2.bottom - 10, 4, 10))
                    temps_ultima_bala_jugador2 = current_time

        if pantalla_actual == 1:  # Menú principal
            # Mostrar fons del menú
            imprimir_pantalla_fons(BACKGROUND_IMAGE)

            # Afegir títol "Nebula Strike"
            font_title = pygame.font.SysFont(None, 100)  # Font més gran per al títol
            title_text = font_title.render("Nebula Strike", True, WHITE)
            pantalla.blit(title_text, (AMPLADA // 2 - title_text.get_width() // 2, ALTURA // 4 - title_text.get_height() // 2))

            # Afegir text al menú amb un tamany més gran
            font = pygame.font.SysFont(None, 60)  # Font més gran per a les opcions
            text = font.render("Prem 1 per jugar", True, WHITE)
            pantalla.blit(text, (AMPLADA // 2 - text.get_width() // 2, ALTURA // 2 - 50))

            text2 = font.render("Prem 2 per crèdits", True, WHITE)
            pantalla.blit(text2, (AMPLADA // 2 - text2.get_width() // 2, ALTURA // 2))

            text3 = font.render("Prem 3 per sortir", True, WHITE)
            pantalla.blit(text3, (AMPLADA // 2 - text3.get_width() // 2, ALTURA // 2 + 50))

            if event.type == KEYDOWN:
                if event.key == K_1:  # Iniciar joc
                    pantalla_actual = 3
                    pygame.mixer.music.stop()  # Aturar música del menú
                    pygame.mixer.music.load(MUSICA_FONS)  # Música de joc
                    pygame.mixer.music.play(-1)
                if event.key == K_2:  # Mostrar crèdits
                    pantalla_actual = 2
                if event.key == K_3:  # Sortir
                    pygame.quit()

        if pantalla_actual == 2:  # Pantalla de crèdits
            imprimir_pantalla_fons(BACKGROUND_IMAGE)

            font_title = pygame.font.SysFont(None, 50)
            text1 = font_title.render("Crèdits", True, WHITE)
            pantalla.blit(text1, (AMPLADA // 2 - text1.get_width() // 2, ALTURA // 4))

            font = pygame.font.SysFont(None, 40)
            text2 = font.render("Desenvolupador: Sergio Arguiñena", True, WHITE)
            pantalla.blit(text2, (AMPLADA // 2 - text2.get_width() // 2, ALTURA // 2 - 50))

            text3 = font.render("Música: Musica per a jocs", True, WHITE)
            pantalla.blit(text3, (AMPLADA // 2 - text3.get_width() // 2, ALTURA // 2))

            text4 = font.render("Gràfics: Sergio Arguiñena ", True, WHITE)
            pantalla.blit(text4, (AMPLADA // 2 - text4.get_width() // 2, ALTURA // 2 + 50))

            text5 = font.render("Prem 1 per tornar al menú", True, WHITE)
            pantalla.blit(text5, (AMPLADA // 2 - text5.get_width() // 2, ALTURA // 2 + 150))

            if event.type == KEYDOWN:
                if event.key == K_1:  # Tornar al menú
                    pantalla_actual = 1

    if pantalla_actual == 4:
        # Mostrar imatge Game Over
        imprimir_pantalla_fons('assets/game_over.png')
        text = "Player" + str(guanyador) + " Wins!"
        font = pygame.font.SysFont(None, 100)
        img = font.render(text, True, MAGENTA)
        pantalla.blit(img, (180, 520))



    if pantalla_actual == 3:
        # Moviment del jugador 1
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            player_rect.x -= velocitat_nau
        if keys[K_d]:
            player_rect.x += velocitat_nau
        # Moviment del jugador 2
        if keys[K_j]:
            player_rect2.x -= velocitat_nau2
        if keys[K_l]:
            player_rect2.x += velocitat_nau2

        # Mantenir al jugador dins de la pantalla:
        player_rect.clamp_ip(pantalla.get_rect())
        player_rect2.clamp_ip(pantalla.get_rect())

        # Dibuixar el fons:
        imprimir_pantalla_fons(BACKGROUND_IMAGE)

        # Dibuixar les naus
        pantalla.blit(player_image, player_rect)  # Nau del jugador 1
        pantalla.blit(player_image2, player_rect2)  # Nau del jugador 2

        # Mostrar les vides
        mostrar_vides()

        # Comprovar si un jugador ha quedat sense vides
        if vides_jugador1 <= 0 or vides_jugador2 <= 0:
            pygame.mixer.music.load(MUSICA_GAME_OVER)  # Música de joc
            pygame.mixer.music.play()
        if vides_jugador2 == 0:
            pantalla_actual = 4  # Pantalla de Game Over
            guanyador = 2  # El guanyador és el jugador 2
        if vides_jugador1 == 0:
            pantalla_actual = 4  # Pantalla de Game Over
            guanyador = 1  # El guanyador és el jugador 1

        # Actualitzar i dibuixar les bales del jugador 1:
        for bala in bales_jugador1:
            bala.y -= velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador1.remove(bala)
            else:
                pantalla.blit(bala_imatge1, bala)  # Dibuixar la bala del jugador 1
            # Detectar col·lisions amb jugador 2:
            if player_rect2.colliderect(bala):
                print("BOOM 1!")
                vides_jugador1 -= 1
                bales_jugador1.remove(bala)  # eliminar la bala
                impacte_so.play()  # Reproducir el so d'impacte

        # Actualitzar i dibuixar les bales del jugador 2:
        for bala in bales_jugador2:
            bala.y += velocitat_bales
            if bala.bottom < 0 or bala.top > ALTURA:
                bales_jugador2.remove(bala)
            else:
                pantalla.blit(bala_imatge2, bala)  # Dibuixar la bala del jugador 2
            # Detectar col·lisions amb jugador 1:
            if player_rect.colliderect(bala):
                print("BOOM 2!")
                vides_jugador2 -= 1
                bales_jugador2.remove(bala)  # eliminar la bala
                impacte_so.play()

    # Actualitzar la pantalla
    pygame.display.update()
    clock.tick(fps)
