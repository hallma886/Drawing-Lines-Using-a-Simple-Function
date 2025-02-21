# Draw Lines Using a Function

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption("Draw Lines Using a Function")
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_line(screen, color, start_point, end_point, width):
    pygame.draw.line(screen, color, start_point, end_point, width) 


def main():

    screen = init_game()
    clock = pygame.time.Clock()

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  # Use color from config

        # Arguments for first line 
        start_pos1 = [150, 150]
        end_pos1 =  [350, 500]
        line_color1 = config.PURPLE
        line_thickness1 = 10  # Set line width (thickness) in pixels

        # Arguments for second line 
        start_pos2 = [400, 350]
        end_pos2 =  [225, 425]
        line_color2 = config.ORANGE
        line_thickness2 = 6  # Set line width (thickness) in pixels

        # Arguments for third line 
        start_pos3 = [250, 250]
        end_pos3 =  [450, 550]
        line_color3 = config.BLUE
        line_thickness3 = 14  # Set line width (thickness) in pixels

        # Arguments for fourth line 
        start_pos4 = [450, 250]
        end_pos4 =  [100, 425]
        line_color4 = config.BLACK
        line_thickness4 = 16  # Set line width (thickness) in pixels

        # Arguments for fifth line 
        start_pos5 = [50, 250]
        end_pos5 =  [150, 450]
        line_color5 = config.GREEN
        line_thickness5 = 12  # Set line width (thickness) in pixels

        # Arguments for sixth line 
        start_pos6 = [425, 150]
        end_pos6 =  [215, 425]
        line_color6 = config.RED
        line_thickness6 = 8  # Set line width (thickness) in pixels


        draw_line(screen, line_color1, start_pos1, end_pos1, line_thickness1)
        draw_line(screen, line_color2, start_pos2, end_pos2, line_thickness2)
        draw_line(screen, line_color3, start_pos3, end_pos3, line_thickness3)
        draw_line(screen, line_color4, start_pos4, end_pos4, line_thickness4)
        draw_line(screen, line_color5, start_pos5, end_pos5, line_thickness5)
        draw_line(screen, line_color6, start_pos6, end_pos6, line_thickness6)
        pygame.display.flip()

        # Limit frame rate to specified number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()































