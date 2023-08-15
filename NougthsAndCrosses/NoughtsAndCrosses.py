from cmath import rect
import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

# Gameboard
background_surface = pygame.image.load('graphics/table.jpg')
rect_surf1 = pygame.Rect(330,500,200,200)
rect_surf2 = pygame.Rect(530,500,200,200)
rect_surf3 = pygame.Rect(730,500,200,200)
rect_surf4 = pygame.Rect(330,300,200,200)
rect_surf5 = pygame.Rect(530,300,200,200)
rect_surf6 = pygame.Rect(730,300,200,200)
rect_surf7 = pygame.Rect(330,100,200,200)
rect_surf8 = pygame.Rect(530,100,200,200)
rect_surf9 = pygame.Rect(730,100,200,200)

# Colors
color_white = (255,255,255)
color_black =(0,0,0)
light_up_color_white = (205,205,205)
light_up_color_black = (30,30,30)

# Keep track of clicked rectangles
clicked_rectangle1 = [(rect_surf1,False)]
clicked_rectangle2 = [(rect_surf2,False)]
clicked_rectangle3 = [(rect_surf3,False)]
clicked_rectangle4 = [(rect_surf4,False)]
clicked_rectangle5 = [(rect_surf5,False)]
clicked_rectangle6 = [(rect_surf6,False)]
clicked_rectangle7 = [(rect_surf7,False)]
clicked_rectangle8 = [(rect_surf8,False)]
clicked_rectangle9 = [(rect_surf9,False)]

# Keep track of clicked piece
clicked_x1 = [()]

game_state = [["", "", ""], ["", "", ""], ["", "", ""]]
game_board_positions = [(330,500),(530,500),(730,500),(330,300),(530,300),(730,300),(330,100),(530,100),(730,100)]
spacing = 40
x_pos = 1000

# Player pieces
x_piece = pygame.image.load('graphics/cross-normal.png')
x_piece_highlighted = pygame.image.load('graphics/cross-pressed.png')

# List of remaining pieces for each player
remaining_x_piece = [x_piece, x_piece, x_piece]

# List for tracking highlighted pieces
highlighted_states_x = [False,False,False]

# List for storing clickable areas of pieces
x_piece_rects = []

# Calculating positions and creating rectangles
for idx, x_piece in enumerate(remaining_x_piece):
    y_pos = 150 + idx * (150 + spacing)
    piece_rect = pygame.Rect(x_pos, y_pos, x_piece.get_width(),x_piece.get_height())
    x_piece_rects.append(piece_rect)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for rect_tuple in clicked_rectangle1:
                    rect, clicked = rect_tuple
                    if rect.collidepoint(event.pos):
                        clicked_rectangle1 = [(r, not c) if r == rect else (r, c) for r, c in clicked_rectangle1]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for rect_tuple in clicked_rectangle2:
                    rect, clicked = rect_tuple
                    if rect.collidepoint(event.pos):
                        clicked_rectangle2 = [(r, not c) if r == rect else (r, c) for r, c in clicked_rectangle2]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for idx, piece_rect in enumerate(x_piece_rects):
                    if piece_rect.collidepoint(event.pos):
                        for i in range(len(highlighted_states_x)):
                            highlighted_states_x[i] = False

                        highlighted_states_x[idx] = True

        
            

    screen.blit(background_surface,(0,0))
    pygame.draw.rect(background_surface,(255,255,255), rect_surf1)
    pygame.draw.rect(background_surface,(0,0,0), rect_surf2)
    pygame.draw.rect(background_surface,(255,255,255), rect_surf3)
    pygame.draw.rect(background_surface,(0,0,0), rect_surf4)
    pygame.draw.rect(background_surface,(255,255,255), rect_surf5)
    pygame.draw.rect(background_surface,(0,0,0), rect_surf6)
    pygame.draw.rect(background_surface,(255,255,255), rect_surf7)
    pygame.draw.rect(background_surface,(0,0,0), rect_surf8)
    pygame.draw.rect(background_surface,(255,255,255), rect_surf9)

    # for idx, piece in enumerate(remaining_x_piece):
    #     y_pos = 150 + idx * (x_piece.get_height() + spacing)
    #     screen.blit(x_piece, (1000, y_pos))

    for idx, x_piece in enumerate(remaining_x_piece):
        y_pos = 150 + idx * (x_piece.get_height() + spacing)
        if highlighted_states_x[idx]: 
            screen.blit(x_piece_highlighted, (1000, y_pos))
        else:
            screen.blit(x_piece, (1000, y_pos))


    # for rect_white, clicked in clicked_rectangle1:
    #     if clicked:
    #         pygame.draw.rect(background_surface, light_up_color_white, rect_surf1)
    #     else:
    #         pygame.draw.rect(background_surface, color_white,rect_surf1)

    # for rect_black, clicked in clicked_rectangle2:
    #     if clicked:
    #         pygame.draw.rect(background_surface, light_up_color_black, rect_surf2)
    #     else:
    #         pygame.draw.rect(background_surface, color_black, rect_surf2)




    pygame.display.update()
    clock.tick(60)

pygame.quit()
