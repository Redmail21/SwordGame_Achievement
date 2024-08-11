import time
import psutil
import keyboard
import pygetwindow as gw
import pydirectinput

#made for a 1920x1080 pixels screen
if __name__ == "__main__":
                                                #The one who pulls out the sword will be crowned king.exe	49448
    print("starting...")
    app_found = "The one who pulls out the sword will be crowned king.exe" in (p.name() for p in psutil.process_iter())
    menu_coords1 = (191, 476) 
    menu_coords2 =  (604, 612)

    if app_found:

        game_window = gw.getWindowsWithTitle('The one who pulls out the sword will be crowned king')[0]
        game_window.activate()
        
        time.sleep(1)

        inc = -300
        pydirectinput.mouseDown()

        while True:
            pydirectinput.moveRel(None,inc)
            inc -=1000

            time.sleep(0.1)
            if keyboard.is_pressed('q'):
                print('lol')
                break

        time.sleep(10)
else:
    print("App not found")

