import pygame
import numpy as np
# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()
# Set up the display window with a width of 800 pixels and a height of 600 pixels
screen = pygame.display.set_mode((800, 600))
origin = (400, 0)
l = 150
r_1 = (0,l)
r_2 = (r_1[0],r_1[1]+l)

m_1 = 1 #kg
m_2 = 1 #kg
g = 9.8 #m/s^2
phi_1 = 0 #radians
phi_2 = 0 #radians
phi_1_dot = 0 #radians/s
phi_2_dot = 0 #radians/s



def calculate_position(phi_1, phi_2):
    x_1 = l * np.sin(phi_1)
    y_1 = l * np.cos(phi_1)
    x_2 = x_1 + l * np.sin(phi_2)
    y_2 = y_1 + l * np.cos(phi_2)
    return (x_1,y_1), (x_2,y_2)
#in_range: checks if the position given is in range of the pendulum
def in_range(pos: tuple, origin: tuple,l: int):
    return (pos[0] - origin[0])**2 + (pos[1] - origin[1])**2 <= l**2

# Set the window title
pygame.display.set_caption("Double Pendulum")

# Main loop
running = True
while running:
    ## Calculates the delta time
    delta_time = clock.tick(60) / 1000  # pygame.tick() returns milliseconds, so divide by 1000 to get seconds
    for event in pygame.event.get():
        # Quit the window if the user closes it
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ## Cursor position
            cursor_pos = pygame.mouse.get_pos()
            print("Mouse button down at", cursor_pos)
            if in_range(cursor_pos, origin, 2*l):
                print("In range")
            else:
                print("Out of range")
        if event.type == pygame.MOUSEBUTTONUP:
            cursor_pos = pygame.mouse.get_pos()
            print("Mouse button up at", cursor_pos)
        if event.type == pygame.MOUSEMOTION:
            cursor_pos = pygame.mouse.get_pos()
            if in_range(cursor_pos, origin, 2*l):
                print("In range")
            else:
                print("Out of range")
            print("Mouse moved to", cursor_pos)

    #m_1 string
    pygame.draw.line(screen, (207, 184, 124), (origin[0], origin[1]), (r_1[0]+origin[0], r_1[1] + origin[1]), 5)
    #m_2 string
    pygame.draw.line(screen, (207, 184, 124), (r_1[0]+origin[0], r_1[1] + origin[1]),(r_2[0]+origin[0], r_2[1] + origin[1]), 5)
    #m_1 mass
    pygame.draw.circle(screen, (255, 255, 255), (r_1[0]+origin[0],r_1[1]+origin[1]), 10)
    #m_2 mass
    pygame.draw.circle(screen, (255, 255, 255), (r_2[0]+origin[0],r_2[1]+origin[1]), 10)

    # Update the display
    pygame.display.flip()

# Clean up and close the window
pygame.quit()
