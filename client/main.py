import socket
import pygame
import sys
import os

from networking import *
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
        #h.send(Message().fold())
    elif mouse_pressed[2]:
        mouse_pos = pygame.mouse.get_pos()
        print("Right mouse pressed.")
    elif mouse_pressed[1]:
        mouse_pos = pygame.mouse.get_pos()
        print("Middle mouse pressed.")
        #h.send("hello")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data = "break"
            h.send(data)
            h.close()
            return False

    return True

def listen(h, g):
    data = h.recv()
    if data == "connected":
        print("connected")
        return
    if data == None: #listening
        #print("LISTENING : NONE DATA RECEIVED")
        return

    jsondata = None
    try:
        jsondata = json.loads(data)
    except json.JSONDecodeError as e:
        print("JSON Error : " + str(e))
        print("D: ", data)
        print()
        return
    print(jsondata)

    header = jsondata["header"]
    # do something
    type = jsondata["type"]
    body = jsondata["body"]

    if type == "player_connect":
        g.handle_connected_players(body)
    elif type == "player_action":
        pass


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

    g.init_values()

    g.load_table()

    print(" - loaded all game objects - ")

    print("establishing connection")
    h = Helper()
    h.connect()
    conn = h.check_connection()

    if conn is not None:
        h._conn.settimeout(0)
        h._id = conn
    else:
        print("E : ERROR CONNECTING")
        sys.exit()

    print(" - connection established - ")

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

        listen(h, g)

        frame_tick(g)

    pygame.quit()

#destroy things ?
