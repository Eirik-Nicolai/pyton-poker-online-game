import socket
from networking import Helper
import pygame
import sys
from game import Game

#
#       EVENT HANDLING
#
def event_handler(pygame, h, g):
    #pygame.event.pump()

    data = ""

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RIGHT]:
        print("Right arrow pressed.")
    elif keys_pressed[pygame.K_ESCAPE]:
        print("Closing main")
        data = "break"
        print(h.send(data))
        h.close()
        return False

    # gets the state of all mouse buttons
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    if mouse_pressed[0]:
        data = "P:"+str(g.colour[0])+";"+str(g.colour[1])+";"+str(g.colour[2])
        h.send(data)
        #resp = h.recv()
        #clrstr = resp.split(";")
        #g.colour = [int(numeric_string) for numeric_string in clrstr]
    elif mouse_pressed[2]:
        data = "M:"+str(g.colour[0])+";"+str(g.colour[1])+";"+str(g.colour[2])
        h.send(data)
        #resp = h.recv()
        #clrstr = resp.split(";")
        #g.colour = [int(numeric_string) for numeric_string in clrstr]
    elif mouse_pressed[1]:
        h.send("hello")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data = "break"
            h.send(data)
            h.close()
            return False

    return True

def listen(h):
    data = h.recv()
    if data != "TIMEOUT":
        print("answr: " + data)

#
#       UPDATE SCREEN
#
def frame_tick(g):
    window.fill((g.colour[0],g.colour[1],g.colour[2]))

    pygame.display.update()


#
#       MAIN FUNCTION
#
if __name__ == "__main__":
    #
    #   INITIALIAZE GAME
    #
    game_width  = 500
    game_height = 500

    print("starting up...")

    pygame.init()

    window = pygame.display.set_mode((game_width, game_height))
    pygame.display.set_caption("Client")

    print("pygame initiated")
    clock = pygame.time.Clock()
    h = Helper()
    conn = h.connect()
    if conn == "CONNECTED":
        print("CONNECTED")
        h._conn.settimeout(0)
    else:
        print("ERROR CONNECTING : " + str(conn))
        sys.exit()

    g = Game()

    #
    #       MENU LOOP
    #
    menu = True
    #while menu:
        #break
    #
    #       MAIN LOOP
    #
    run = True
    while run:
        clock.tick(60)

        run = event_handler(pygame, h, g)

        listen(h)

        frame_tick(g)

    pygame.quit()

#destroy things ?
