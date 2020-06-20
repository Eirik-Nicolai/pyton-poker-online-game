import socket
import pygame
import sys
import os

from networking import Helper
from game import Game
from player import Player
from consts import *

#
#       EVENT HANDLING
#
def event_handler(pygame, h, g):
    #pygame.event.pump()

    data = ""

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_RETURN]:
        print("ENTER presed")
    elif keys_pressed[pygame.K_ESCAPE]:
        print("Closing main")
        data = "break"
        print(h.send(data))
        h.close()
        return False
    elif keys_pressed[pygame.K_LEFT]:
        pass
    elif keys_pressed[pygame.K_RIGHT]:
        pass
    else:
        pressed = []
        for id, key in enumerate(keys_pressed):
            if key:
                pressed.append(id)

        for key in pressed:
            print(str(key) + " PRESSED")

    # gets the state of all mouse buttons
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)
        h.send(data)
    elif mouse_pressed[2]:
        mouse_pos = pygame.mouse.get_pos()
        print("Right mouse pressed.")
        h.send(data)
    elif mouse_pressed[1]:
        mouse_pos = pygame.mouse.get_pos()
        print("Middle mouse pressed.")
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
    # fill bg
    window.fill(COLOUR["black"])

    window.blit(g.BG, (0,0))

    g.blit_to_surface(g.BG)

    # update game

    # update chat ?


    pygame.display.update()


#
#       MAIN FUNCTION
#
if __name__ == "__main__":
    #
    #   INITIALIAZE GAME
    #
    print("starting up...")

    print("establishing connection")
    h = Helper()
    conn = h.connect()

    #if conn == "CONNECTED":
        #h._conn.settimeout(0)
    #else:
        #print("E : ERROR CONNECTING : " + str(conn))
        #sys.exit()

    print(" - connection established - ")


    pygame.init()
    window = pygame.display.set_mode((NUMBER["screen_width"], NUMBER["screen_height"]))
    pygame.display.set_caption("Client")
    clock = pygame.time.Clock()

    print(" - pygame initiated - ")

    print("loading game...")

    g = Game()

    # Load bg
    g.load_background(PATH["ABS"]+PATH["background"])
    print(" - BG loaded")

    # Load cards
    for filename in os.listdir(PATH["ABS"]+PATH["img_cards_png"]):
        g.add_card_to_deck(filename.split(".")[0],
                        PATH["ABS"]+PATH["img_cards_png"]+filename)

    print(" - IMAGES loaded")

    for i in range(5):
        g.load_player(i,
                      Player((0,0),
                             (POSITION  ["player_" + str(i) + "_card_left"],
                             SCALE      ["player_" + str(i)]),
                             (POSITION  ["player_" + str(i) + "_card_right"],
                             SCALE      ["player_" + str(i)]),
                             POSITION   ["player_" + str(i) + "_money"]
                             )
                      )
    g.init_values()

    g.load_table()

    print(" - loaded all game objects - ")

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

        #listen(h)

        frame_tick(g)

    pygame.quit()

#destroy things ?
