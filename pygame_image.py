import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #背景画像のSurface
    bg_img2 =pg.image.load("fig/pg_bg.jpg")
    kk_img =pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img,True,False)
    bg_img = pg.transform.flip(bg_img,True,False)
    kk_img = pg.transform.rotozoom(kk_img, 10, 1.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        dx = 0
        dy = 0
        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            dx = -1
        if key_list[pg.K_DOWN]:
            dx = 1
        if key_list[pg.K_LEFT]:
            dy = -1
        if key_list[pg.K_RIGHT]:
            dy = 1
        else:
            dy = -1

        kk_rct.move_ip(dy,dx)

        x = tmr%3200
        screen.blit(bg_img, [-x, 0]) #1枚目
        screen.blit(bg_img2, [-x+1600, 0]) #２枚目
        screen.blit(bg_img, [-x+3200, 0])
        #screen.blit(kk_img, [300, 200])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr +=  1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()