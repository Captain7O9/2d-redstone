import pygame
pygame.init()


# Window information
display_width = 800
display_height = 600
window = pygame.display.set_mode((display_width, display_height))

# Clock
window_clock = pygame.time.Clock()


class Renderer:
    def __init__(self, width, height):
        """
        The __init__ function is called when the class is instantiated.
        It runs the window.

        :param self: Represent the instance of the class
        :param width: Set the width of the screen
        :param height: Set the height of the screen
        :return: The object itself
        """
        self.dw = width
        self.dh = height

        self.run()

    def run(self):
        """
        The run function is the main loop of the program. It handles all events,
        updates and drawing to the screen. The run function will be called by
        the main function in order to start the program.

        :param self: Represent the instance of the class
        :return: Nothing
        """
        running = True

        # Main loop
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    running = False

            # Update clock and display
            pygame.display.update()
            window_clock.tick(60)


if __name__ == "__main__":
    renderer = Renderer()
