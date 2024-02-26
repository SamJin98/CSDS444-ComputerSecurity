import pygame


RED, YELLOW, GREEN, GRAY = ((255, 0, 0),
                            (255, 255, 0),
                            (0, 255, 0),
                            (192, 192, 192))

vehicle_traffic_light_pos_base = {'north': (300, 100),
                                  'south': (300, 500),
                                  'west': (500, 300),
                                  'east': (100, 300)}
vehicle_traffic_light_offset = 30

pedestrian_traffic_light_pos_base = {'north': [(190, 175), (410, 175)],
                                     'south': [(190, 425), (410, 425)],
                                     'west': [(175, 190), (175, 410)],
                                     'east': [(425, 190), (425, 410)]}
pedestrian_traffic_light_offset = 5


def draw_vehicle_straight_and_right_turning_traffic_lights(screen, traffic_system):
    for direction, straight_light in [('north', traffic_system.north_straight_light),
                                      ('south', traffic_system.south_straight_light),
                                      ('west', traffic_system.west_straight_light),
                                      ('east', traffic_system.east_straight_light)]:

        if direction == 'north' or direction == 'south':
            red_straight_pos = (vehicle_traffic_light_pos_base[direction][0] - vehicle_traffic_light_offset,
                                vehicle_traffic_light_pos_base[direction][1])
            yellow_straight_pos = vehicle_traffic_light_pos_base[direction]
            green_straight_pos = (vehicle_traffic_light_pos_base[direction][0] + vehicle_traffic_light_offset,
                                  vehicle_traffic_light_pos_base[direction][1])

            right_turning_pos = (vehicle_traffic_light_pos_base[direction][0] + vehicle_traffic_light_offset * 2,
                                 vehicle_traffic_light_pos_base[direction][1])
            # if direction == 'south':
            #     print(right_turning_pos)  # (360, 500)
            if direction == 'south':
                right_turning_pos = (240, 500)
        else:
            red_straight_pos = (vehicle_traffic_light_pos_base[direction][0],
                                vehicle_traffic_light_pos_base[direction][1] - vehicle_traffic_light_offset)
            yellow_straight_pos = vehicle_traffic_light_pos_base[direction]
            green_straight_pos = (vehicle_traffic_light_pos_base[direction][0],
                                  vehicle_traffic_light_pos_base[direction][1] + vehicle_traffic_light_offset)

            right_turning_pos = (vehicle_traffic_light_pos_base[direction][0],
                                 vehicle_traffic_light_pos_base[direction][1] + vehicle_traffic_light_offset * 2)
            # if direction == 'east':
            #     print(right_turning_pos)  # (100, 360)
            if direction == 'east':
                right_turning_pos = (100, 240)

        straight_red_color = RED if straight_light.is_red() else GRAY
        straight_yellow_color = YELLOW if straight_light.is_yellow() else GRAY
        straight_green_color = GREEN if straight_light.is_green() else GRAY

        if straight_red_color == RED:
            right_turning_color = RED
        elif straight_yellow_color == YELLOW:
            right_turning_color = YELLOW
        elif straight_green_color == GREEN:
            right_turning_color = GREEN
        else:
            right_turning_color = GRAY

        pygame.draw.circle(screen, straight_red_color, red_straight_pos, 10)
        pygame.draw.circle(screen, straight_yellow_color, yellow_straight_pos, 10)
        pygame.draw.circle(screen, straight_green_color, green_straight_pos, 10)

        pygame.draw.circle(screen, right_turning_color, right_turning_pos, 10)


def draw_vehicle_left_turning_traffic_lights(screen, traffic_system):
    for direction, left_turning_light in [('north', traffic_system.north_left_turning_light),
                                          ('south', traffic_system.south_left_turning_light),
                                          ('west', traffic_system.west_left_turning_light),
                                          ('east', traffic_system.east_left_turning_light)]:

        if direction == 'north' or direction == 'south':
            turning_light_pos = (vehicle_traffic_light_pos_base[direction][0] - vehicle_traffic_light_offset * 2,
                                 vehicle_traffic_light_pos_base[direction][1])
            # if direction == 'south':
            #     print(turning_light_pos)  # (240, 500)
            if direction == 'south':
                turning_light_pos = (360, 500)
        else:
            turning_light_pos = (vehicle_traffic_light_pos_base[direction][0],
                                 vehicle_traffic_light_pos_base[direction][1] - vehicle_traffic_light_offset * 2)
            # if direction == 'east':
            #     print(turning_light_pos)  # (100, 240)
            if direction == 'east':
                turning_light_pos = (100, 360)

        if left_turning_light.is_red():
            left_turning_light_color = RED
        elif left_turning_light.is_yellow():
            left_turning_light_color = YELLOW
        elif left_turning_light.is_green():
            left_turning_light_color = GREEN
        else:
            left_turning_light_color = GRAY

        pygame.draw.circle(screen, left_turning_light_color, turning_light_pos, 10)


def draw_pedestrian_traffic_lights(screen, traffic_system):
    for direction, pedestrian_light in [('north', traffic_system.north_pedestrian_light),
                                      ('south', traffic_system.south_pedestrian_light),
                                      ('west', traffic_system.west_pedestrian_light),
                                      ('east', traffic_system.east_pedestrian_light)]:

        if pedestrian_light.is_green():
            green_light_color = GREEN
            red_light_color = GRAY
        else:
            green_light_color = GRAY
            red_light_color = RED

        if direction == "north" or direction == "south":
            green_light_pos = (pedestrian_traffic_light_pos_base[direction][0][0],
                               pedestrian_traffic_light_pos_base[direction][0][1] - pedestrian_traffic_light_offset)
            red_light_pos = (pedestrian_traffic_light_pos_base[direction][0][0],
                             pedestrian_traffic_light_pos_base[direction][0][1] + pedestrian_traffic_light_offset)
            green_light_pos2 = (pedestrian_traffic_light_pos_base[direction][1][0],
                                pedestrian_traffic_light_pos_base[direction][1][1] - pedestrian_traffic_light_offset)
            red_light_pos2 = (pedestrian_traffic_light_pos_base[direction][1][0],
                              pedestrian_traffic_light_pos_base[direction][1][1] + pedestrian_traffic_light_offset)

            pygame.draw.circle(screen, green_light_color, green_light_pos, 5)
            pygame.draw.circle(screen, red_light_color, red_light_pos, 5)
            pygame.draw.circle(screen, green_light_color, green_light_pos2, 5)
            pygame.draw.circle(screen, red_light_color, red_light_pos2, 5)
        else:
            green_light_pos = (pedestrian_traffic_light_pos_base[direction][0][0] - pedestrian_traffic_light_offset,
                               pedestrian_traffic_light_pos_base[direction][0][1])
            red_light_pos = (pedestrian_traffic_light_pos_base[direction][0][0] + pedestrian_traffic_light_offset,
                             pedestrian_traffic_light_pos_base[direction][0][1])
            green_light_pos2 = (pedestrian_traffic_light_pos_base[direction][1][0] - pedestrian_traffic_light_offset,
                                pedestrian_traffic_light_pos_base[direction][1][1])
            red_light_pos2 = (pedestrian_traffic_light_pos_base[direction][1][0] + pedestrian_traffic_light_offset,
                              pedestrian_traffic_light_pos_base[direction][1][1])

            pygame.draw.circle(screen, green_light_color, green_light_pos, 5)
            pygame.draw.circle(screen, red_light_color, red_light_pos, 5)
            pygame.draw.circle(screen, green_light_color, green_light_pos2, 5)
            pygame.draw.circle(screen, red_light_color, red_light_pos2, 5)


def draw_backgrounds(screen):
    # Draw roads
    pygame.draw.rect(screen, (50, 50, 50), (50, 200, 500, 200))
    pygame.draw.rect(screen, (50, 50, 50), (200, 50, 200, 500))

    # Draw road dividers
    pygame.draw.line(screen, (175, 175, 175), (50, 300), (550, 300), 3)
    pygame.draw.line(screen, (175, 175, 175), (300, 50), (300, 550), 3)

    # Draw zebra markings
    pygame.draw.rect(screen, (245, 245, 245), (150, 205, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 225, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 245, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 265, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 285, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 305, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 325, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 345, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 365, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (150, 385, 50, 10))

    pygame.draw.rect(screen, (245, 245, 245), (205, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (225, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (245, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (265, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (285, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (305, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (325, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (345, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (365, 150, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (385, 150, 10, 50))

    pygame.draw.rect(screen, (245, 245, 245), (400, 205, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 225, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 245, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 265, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 285, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 305, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 325, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 345, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 365, 50, 10))
    pygame.draw.rect(screen, (245, 245, 245), (400, 385, 50, 10))

    pygame.draw.rect(screen, (245, 245, 245), (205, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (225, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (245, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (265, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (285, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (305, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (325, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (345, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (365, 400, 10, 50))
    pygame.draw.rect(screen, (245, 245, 245), (385, 400, 10, 50))


def draw_turning_lights_text(screen):
    font = pygame.font.Font(None, 24)
    north_right_turing_text = font.render('RTurn', True, (255, 255, 255))
    south_right_turing_text = font.render('LTurn', True, (255, 255, 255))
    east_right_turing_text = font.render('RTurn', True, (255, 255, 255))
    west_right_turing_text = font.render('LTurn', True, (255, 255, 255))
    screen.blit(north_right_turing_text, (335, 70))
    screen.blit(south_right_turing_text, (338, 515))
    screen.blit(east_right_turing_text, (478, 375))
    screen.blit(west_right_turing_text, (78, 375))

    north_left_turing_text = font.render('LTurn', True, (255, 255, 255))
    south_left_turing_text = font.render('RTurn', True, (255, 255, 255))
    east_left_turing_text = font.render('LTurn', True, (255, 255, 255))
    west_left_turing_text = font.render('RTurn', True, (255, 255, 255))
    screen.blit(north_left_turing_text, (219, 70))
    screen.blit(south_left_turing_text, (216, 515))
    screen.blit(east_left_turing_text, (480, 211))
    screen.blit(west_left_turing_text, (80, 211))


def draw_description_text(screen):
    font = pygame.font.Font(None, 20)
    description_text1 = font.render(
        'This traffic control system includes straight ahead light (red, green and yellow colors ',
        True, (0, 0, 0))
    description_text2 = font.render(
        'separated), left turn light (three colors in one), right turn light (three colors in one) ',
        True, (0, 0, 0))
    description_text3 = font.render(
        'and pedestrian light (red and green colors separated). The straight ahead light and the ',
        True, (0, 0, 0))
    description_text4 = font.render(
        'right turn light are tied together, which means that you can turn right when you can go ',
        True, (0, 0, 0))
    description_text5 = font.render(
        'straight ahead. The left turn light is separated, and a left turn can only be made when ',
        True, (0, 0, 0))
    description_text6 = font.render(
        'the straight ahead light (with the right turn light) has ended. When the above steps ',
        True, (0, 0, 0))
    description_text7 = font.render(
        'have been performed, yield the right-of-way to the other roadway at the intersection.',
        True, (0, 0, 0))
    description_text8 = font.render(
        'Yunlai Zhou,  Ruilin Jin,  Sixu Li',
        True, (0, 0, 0))
    screen.blit(description_text1, (5, 600))
    screen.blit(description_text2, (5, 620))
    screen.blit(description_text3, (5, 640))
    screen.blit(description_text4, (5, 660))
    screen.blit(description_text5, (5, 680))
    screen.blit(description_text6, (5, 700))
    screen.blit(description_text7, (5, 720))
    screen.blit(description_text8, (5, 760))

