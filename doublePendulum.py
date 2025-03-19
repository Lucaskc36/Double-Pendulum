import pygame
# Initialize Pygame
pygame.init()

# Set up the display window with a width of 800 pixels and a height of 600 pixels
screen = pygame.display.set_mode((800, 600))
origin = (400, 0)
l = 300
r_1 = (0,l)
r_2 = (l,r_1[1])
m_1 = 1
m_2 = 1
g = 9.8
theta_1 = 0
theta_2 = 0
theta_1_dot = 0
theta_2_dot = 0

def in_range(pos: tuple, origin: tuple,l: int):
    return (pos[0] - origin[0])**2 + (pos[1] - origin[1])**2 <= l**2

# Set the window title
pygame.display.set_caption("Double Pendulum")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        # Quit the window if the user closes it
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
        ## Cursor position
            cursor_pos = pygame.mouse.get_pos()
            print("Mouse button down at", cursor_pos)
            if in_range(cursor_pos, origin, l):
                print("In range")
            else:
                print("Out of range")
        if event.type == pygame.MOUSEBUTTONUP:
            cursor_pos = pygame.mouse.get_pos()
            print("Mouse button up at", cursor_pos)
        if event.type == pygame.MOUSEMOTION:
            cursor_pos = pygame.mouse.get_pos()
            print("Mouse moved to", cursor_pos)


    pygame.draw.line(screen, (207, 184, 124), (400, 0), (400, 300), 5)
    pygame.draw.line(screen, (207, 184, 124), (400, 300), (400, 500), 5)
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), 10)
    pygame.draw.circle(screen, (255, 255, 255), (400, 500), 10)
    # Your game logic and drawing code would go here

    # Update the display
    pygame.display.flip()

# Clean up and close the window
pygame.quit()
