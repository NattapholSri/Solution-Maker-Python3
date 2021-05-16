import pygame,sys
import pygame_gui
import runpy

a = 0

pygame.init()

pygame.display.set_caption('Numerical')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((800, 600))

font = pygame.font.SysFont(None, 30)
img = font.render('NUMERICAL', True,pygame.Color('#000000'))



Taylor_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 225), (160, 50)),
                                             text='Taylor’s series',
                                             manager=manager)
Horner_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 275), (160, 50)),
                                             text='Hornor’s schema',
                                             manager=manager)
Lagrange_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((320, 325), (160, 50)),
                                             text='Lagrange Polynomial',
                                             manager=manager)
Exit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 550), (100, 50)),
                                             text='Exit',
                                             manager=manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60)/1000.0


    background.blit(img, (350, 175))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == Taylor_button:
                    print('Taylor Start')
                    pygame.quit()
                    runpy.run_path("Gui_Tayloy_series.py")
                if event.ui_element == Horner_button:
                    print('Horner Start')
                    pygame.quit()
                    runpy.run_path("GuiHorner.py")
                if event.ui_element == Lagrange_button:
                    print('Lagrange Start')
                    pygame.quit()
                    runpy.run_path("Gui_Lagrange.py")




                if event.ui_element == Exit_button:
                    print('Hello World!')
                    is_running = False

        manager.process_events(event)



    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()


