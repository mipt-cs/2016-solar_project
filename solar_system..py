import pygame

pygame.init()
pygame.font.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (87, 160, 211)
GREEN = (140, 207, 127)
ORANGE = (240, 136, 0)

SCREEN_SIZE = (800, 600)


class Sun():
    """
    Устанавливает параметры Солнца и рисует его
    """
    pass


class Planet():
    """
    Управляет движением планет, устанавливает их параметры и рисует их
    """
    def __init__(self, number):
        """
        Рассчитывает скорость планет, их координаты и ускорения
        Параметр number выбирает планету из файла
        """
        pass
    pass


class Button():
    """
    Содержит основные свойства любой кнопки.
    """
    def __init__(self, coord=[20, 20], color=BLUE, width=100, height=45, time = 0):
        self.coord = coord
        self.color = color
        self.width = width
        self.height = height
        self.time = time
        self.font = pygame.font.SysFont("dejavusansmono", 40)
        self.font_loc = [self.coord[0] + 10, self.coord[1] + 10]
        self.font_color = BLACK

    def draw(self, screen, font_color, phrase=""):
        pygame.draw.rect(screen, self.color, (self.coord[0], self.coord[1], self.width, self.height))
        screen.blit(self.font.render(phrase, True, self.font_color), self.font_loc)


    def react(self, mouse_pos, phrase=""):
        if ((mouse_pos[0] > self.coord[0]) and (mouse_pos[0] < (self.coord[0] + self.width)) and
            (mouse_pos[1] > self.coord[1]) and (mouse_pos[1] < (self.coord[1] + self.height))):
            screen.blit(self.font.render(phrase, True, RED), self.font_loc)



class StartButton(Button):
    """
    Рисует стартовую кнопку, проверяет, нажата ли она и начинает симуляцию
    """
    def __init__(self, coord=[20, 85], color=GREEN, width=100, height=45, time = 0):
        super().__init__(coord=[20, 85], color=GREEN, width=100, height=45, time = 0)

    def draw(self, screen, font_color, phrase="Start"):
        super().draw(screen, font_color, phrase="Start")
    
    def react(self, mouse_pos, phrase="Start"):
        super().react(mouse_pos, phrase = "Start")

    def start():
        pass


class PauseButton(Button):
    """
    Рисует кнопку паузы, проверяет, нажата ли она и останавливает симуляцию
    """
    def __init__(self, coord=[20, 150], color=ORANGE, width=100, height=45, time = 0):
        super().__init__(coord=[20, 150], color=ORANGE, width=100, height=45, time = 0)

    def draw(self, screen, font_color, phrase = "Pause"):
        super().draw(screen, font_color, phrase = "Pause")
    
    def react(self, mouse_pos, phrase=""):
        if ((mouse_pos[0] > self.coord[0]) and (mouse_pos[0] < (self.coord[0] + self.width)) and
            (mouse_pos[1] > self.coord[1]) and (mouse_pos[1] < (self.coord[1] + self.height))):
            screen.blit(self.font.render(phrase, True, RED), self.font_loc)
            if self.font_color==BLACK:
                self.font_color = RED
            else:
                self.font_color = BLACK

    def pause():
        pass



class ResetButton(Button):
    """
    Рисует кнопку перезагрузки, проверяет, нажата ли она и перезапускает симуляцию
    """
    def __init__(self, coord=[20, 20], color=BLUE, width=100, height=45, time = 0):
        super().__init__(coord=[20, 20], color=BLUE, width=100, height=45, time = 0)


    def draw(self, screen, font_color, phrase = "Reset"):
        super().draw(screen, font_color, phrase = "Reset")

    def react(self, mouse_pos, phrase="Reset"):
        super().react(mouse_pos, phrase = "Reset")
    
    def restart():
        pass


class Processing():
    """
    Обработка
    """
    def __init__(self):
        self.rb = ResetButton()
        self.sb = StartButton()
        self.pb = PauseButton()

    def process(self, events, screen):
        self.rb.draw(screen, BLACK)
        self.sb.draw(screen, BLACK)
        self.pb.draw(screen, BLACK)
        done = False
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.rb.react(pygame.mouse.get_pos())
                self.sb.react(pygame.mouse.get_pos())
                self.pb.react(pygame.mouse.get_pos())

        return done

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Solar system model")

done = False
clock = pygame.time.Clock()
pygame.mouse.get_pos()

prs = Processing()

while not done==True:
    clock.tick(15)
    screen.fill(BLACK)

    done = prs.process(pygame.event.get(), screen)

    pygame.display.flip()


pygame.quit()


