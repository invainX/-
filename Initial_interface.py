def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects('Welcome', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO", 150, 450, 100, 50, green, bright_green, game_loop1)
        button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
        button("record", 350, 450, 100, 50, gray, bright_red, record)
        pygame.display.update()
        clock.tick(15)