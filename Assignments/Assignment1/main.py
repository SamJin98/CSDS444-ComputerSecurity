import argparse
import pygame
from enum import Enum, auto


class LightState(Enum):
    GREEN = auto()
    YELLOW = auto()
    RED = auto()


class TrafficLight:
    def __init__(self, initial_state: LightState):
        self.state = initial_state

    def set_state(self, new_state: LightState):
        self.state = new_state

    def is_green(self):
        return self.state == LightState.GREEN

    def is_yellow(self):
        return self.state == LightState.YELLOW

    def is_red(self):
        return self.state == LightState.RED


class PedestrianLight:
    def __init__(self, walk: bool, stop: bool):
        self.walk = walk
        self.stop = stop

    def set_walk(self):
        self.walk = True
        self.stop = False

    def set_stop(self):
        self.walk = False
        self.stop = True

    def get_walk(self):
        return self.walk


class Pedestrian:
    def __init__(self, x, y, direction):
        self.start_x = x
        self.start_y = y
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 1
        self.crossing = False

    def update_position(self, traffic_system):
        if self.direction == "vertical":
            signal = traffic_system.north_cross.get_walk() or traffic_system.south_cross.get_walk()
        else:  # "horizontal"
            signal = traffic_system.east_cross.get_walk() or traffic_system.west_cross.get_walk()

        if signal and not self.crossing:  # Move towards the opposite side
            if self.direction == "vertical":
                self.y += -self.speed if self.start_y > 300 else self.speed
            else:
                self.x += self.speed if self.start_x < 300 else -self.speed

            # Check if pedestrian has crossed halfway to flip the crossing flag
            if self.direction == "vertical" and (self.y < 250 or self.y > 350):
                self.crossing = True
            elif self.direction == "horizontal" and (self.x < 250 or self.x > 350):
                self.crossing = True

        elif self.crossing:  # Return to start side
            if self.direction == "vertical":
                self.y += self.speed if self.y < 300 else -self.speed
            else:
                self.x += -self.speed if self.x > 300 else self.speed

            # Reset position and crossing flag near original position
            if (self.direction == "vertical" and abs(self.y - self.start_y) < 5) or \
                (self.direction == "horizontal" and abs(self.x - self.start_x) < 5):
                self.x, self.y = self.start_x, self.start_y
                self.crossing = False


class TrafficSystem:
    def __init__(self, north_light, south_light, east_light, west_light, north_cross, south_cross, east_cross,
                 west_cross, red_time, green_time, yellow_time, pedestrians):
        self.north_light = north_light
        self.south_light = south_light
        self.east_light = east_light
        self.west_light = west_light
        self.north_cross = north_cross
        self.south_cross = south_cross
        self.east_cross = east_cross
        self.west_cross = west_cross
        self.red_time = red_time
        self.green_time = green_time
        self.yellow_time = yellow_time
        self.pedestrians = pedestrians


def initialize_traffic_system(red_time, green_time, yellow_time):
    # Initialize traffic and pedestrian lights
    north_light = TrafficLight(LightState.RED)
    south_light = TrafficLight(LightState.RED)
    east_light = TrafficLight(LightState.GREEN)
    west_light = TrafficLight(LightState.GREEN)
    north_cross = PedestrianLight(False, True)
    south_cross = PedestrianLight(False, True)
    east_cross = PedestrianLight(True, False)
    west_cross = PedestrianLight(True, False)

    # Initialize pedestrians
    pedestrians = []
    # North to South and South to North
    for i in range(4):
        pedestrians.append(Pedestrian(280, 10 + i * 40, "vertical"))
        pedestrians.append(Pedestrian(320, 590 - i * 40, "vertical"))
    # East to West and West to East
    for i in range(4):
        pedestrians.append(Pedestrian(10 + i * 40, 280, "horizontal"))
        pedestrians.append(Pedestrian(590 - i * 40, 320, "horizontal"))

    traffic_system = TrafficSystem(north_light, south_light, east_light, west_light, north_cross, south_cross,
                                   east_cross, west_cross, red_time, green_time, yellow_time, pedestrians)
    return traffic_system


def update_traffic_lights(cycle_time, traffic_system):
    if cycle_time < traffic_system.red_time:
        traffic_system.east_light.set_state(LightState.GREEN)
        traffic_system.west_light.set_state(LightState.GREEN)
        traffic_system.north_light.set_state(LightState.RED)
        traffic_system.south_light.set_state(LightState.RED)
        traffic_system.east_cross.set_walk()
        traffic_system.west_cross.set_walk()
        traffic_system.north_cross.set_stop()
        traffic_system.south_cross.set_stop()
    elif cycle_time < traffic_system.red_time + traffic_system.yellow_time:
        traffic_system.east_light.set_state(LightState.YELLOW)
        traffic_system.west_light.set_state(LightState.YELLOW)
    elif cycle_time < traffic_system.red_time + traffic_system.yellow_time + traffic_system.green_time:
        traffic_system.north_light.set_state(LightState.GREEN)
        traffic_system.south_light.set_state(LightState.GREEN)
        traffic_system.east_light.set_state(LightState.RED)
        traffic_system.west_light.set_state(LightState.RED)
        traffic_system.north_cross.set_walk()
        traffic_system.south_cross.set_walk()
        traffic_system.east_cross.set_stop()
        traffic_system.west_cross.set_stop()
    elif cycle_time < traffic_system.red_time + traffic_system.yellow_time + traffic_system.green_time + traffic_system.yellow_time:
        traffic_system.north_light.set_state(LightState.YELLOW)
        traffic_system.south_light.set_state(LightState.YELLOW)


def draw_traffic_lights(screen, traffic_system):
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    GRAY = (192, 192, 192)  # Inactive light color
    light_positions = {'north': (300, 100), 'south': (300, 500), 'east': (100, 300), 'west': (500, 300)}

    # Distance between lights
    offset = 30

    for direction, light in [('north', traffic_system.north_light), ('south', traffic_system.south_light),
                             ('east', traffic_system.east_light), ('west', traffic_system.west_light)]:
        # Position adjustments for each circle to be drawn vertically aligned
        red_pos = (light_positions[direction][0], light_positions[direction][1] - offset)
        yellow_pos = light_positions[direction]
        green_pos = (light_positions[direction][0], light_positions[direction][1] + offset)

        # Determine the active light color
        red_color = RED if light.is_red() else GRAY
        yellow_color = YELLOW if light.is_yellow() else GRAY
        green_color = GREEN if light.is_green() else GRAY

        # Draw the traffic light circles
        pygame.draw.circle(screen, red_color, red_pos, 10)
        pygame.draw.circle(screen, yellow_color, yellow_pos, 10)
        pygame.draw.circle(screen, green_color, green_pos, 10)


def draw_pedastrian_traffic_lights(screen, traffic_system):
    RED = (255, 0, 0)
    # YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    GRAY = (192, 192, 192)  # Inactive light color
    light_positions = {'north': [(190, 150), (410, 150)], 'south': [(190, 450), (410, 450)],
                       'east': [(450, 190), (450, 410)], 'west': [(150, 190), (150, 410)]}

    # Distance between pd traffic lights
    distance = 5

    for direction, light in [('north', traffic_system.north_light), ('south', traffic_system.south_light),
                             ('west', traffic_system.west_light), ('east', traffic_system.east_light)]:

        # Determine the active light color
        red_color = GREEN if light.is_red() else GRAY
        green_color = RED if light.is_green() else GRAY

        if direction == 'north' or 'south':

            red_pos = (light_positions[direction][0][0], light_positions[direction][0][1] - distance)
            green_pos = (light_positions[direction][0][0], light_positions[direction][0][1] + distance)

            red_pos2 = (light_positions[direction][1][0], light_positions[direction][1][1] - distance)
            green_pos2 = (light_positions[direction][1][0], light_positions[direction][1][1] + distance)

            # Draw the traffic light circles (Both 2 sides)
            pygame.draw.circle(screen, red_color, red_pos, 5)
            pygame.draw.circle(screen, green_color, green_pos, 5)

            pygame.draw.circle(screen, red_color, red_pos2, 5)
            pygame.draw.circle(screen, green_color, green_pos2, 5)

        elif direction == 'west' or 'east':

            red_pos_we = (light_positions[direction][0][0] - distance, light_positions[direction][0][1])
            green_pos_we = (light_positions[direction][0][0] + distance, light_positions[direction][0][1])

            red_pos2_we = (light_positions[direction][1][0] - distance, light_positions[direction][1][1])
            green_pos2_we = (light_positions[direction][1][0] + distance, light_positions[direction][1][1])

            # Draw the traffic light circles (Both 2 sides)
            pygame.draw.circle(screen, red_color, red_pos_we, 5)
            pygame.draw.circle(screen, green_color, green_pos_we, 5)

            pygame.draw.circle(screen, red_color, red_pos2_we, 5)
            pygame.draw.circle(screen, green_color, green_pos2_we, 5)


def draw_roads(screen):
    road_color = (50, 50, 50)  # Dark gray color for roads
    pygame.draw.rect(screen, road_color, (50, 200, 500, 200))  # Wider Horizontal road
    pygame.draw.rect(screen, road_color, (200, 50, 200, 500))  # Wider Vertical road

    # Draw road markings
    marking_color = (124, 252, 0)  # White color for road markings
    pygame.draw.line(screen, marking_color, (50, 300), (550, 300), 5)  # Horizontal marking
    pygame.draw.line(screen, marking_color, (300, 50), (300, 550), 5)  # Vertical marking

    # Draw crosswalks
    crosswalk_color = (245, 245, 245)  # Grey color for crosswalk marking

    # Part 1 (Left)
    pygame.draw.rect(screen, crosswalk_color, (150, 210, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 230, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 250, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 270, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 290, 50, 10))

    pygame.draw.rect(screen, crosswalk_color, (150, 310, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 330, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 350, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 370, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (150, 390, 50, 8))

    # Part 2 (Up)
    pygame.draw.rect(screen, crosswalk_color, (210, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (230, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (250, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (270, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (290, 150, 10, 50))

    pygame.draw.rect(screen, crosswalk_color, (310, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (330, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (350, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (370, 150, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (390, 150, 8, 50))

    # Part 3 (Right)
    pygame.draw.rect(screen, crosswalk_color, (400, 210, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 230, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 250, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 270, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 290, 50, 10))

    pygame.draw.rect(screen, crosswalk_color, (400, 310, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 330, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 350, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 370, 50, 10))
    pygame.draw.rect(screen, crosswalk_color, (400, 390, 50, 8))

    # Part 4 (Down)
    pygame.draw.rect(screen, crosswalk_color, (210, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (230, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (250, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (270, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (290, 400, 10, 50))

    pygame.draw.rect(screen, crosswalk_color, (310, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (330, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (350, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (370, 400, 10, 50))
    pygame.draw.rect(screen, crosswalk_color, (390, 400, 8, 50))


def draw_pedestrian_states(screen, traffic_system):
    font = pygame.font.Font(None, 24)
    action_texts = {
        "north": "GO" if traffic_system.north_cross.get_walk() else "WAIT" if traffic_system.north_light.is_yellow() else "STOP",
        "south": "GO" if traffic_system.south_cross.get_walk() else "WAIT" if traffic_system.south_light.is_yellow() else "STOP",
        "east": "GO" if traffic_system.east_cross.get_walk() else "WAIT" if traffic_system.east_light.is_yellow() else "STOP",
        "west": "GO" if traffic_system.west_cross.get_walk() else "WAIT" if traffic_system.west_light.is_yellow() else "STOP"
    }
    positions = {"north": (320, 80), "south": (320, 520), "east": (120, 280), "west": (440, 280)}

    for direction, text in action_texts.items():
        text_surf = font.render(text, True, (255, 255, 255))
        screen.blit(text_surf, positions[direction])


def main(red_time, green_time, yellow_time):
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Traffic System Simulation")
    clock = pygame.time.Clock()

    traffic_system = initialize_traffic_system(red_time, green_time, yellow_time)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Clear the screen

        current_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds
        cycle_time = current_time % (red_time + green_time + yellow_time + yellow_time)

        update_traffic_lights(cycle_time, traffic_system)

        draw_roads(screen)
        draw_traffic_lights(screen, traffic_system)
        draw_pedestrian_states(screen, traffic_system)  # Replace draw_pedestrians call

        draw_pedastrian_traffic_lights(screen, traffic_system)

        pygame.display.flip()
        clock.tick(60)  # FPS

    pygame.quit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate a traffic light system with pedestrian movement.")
    parser.add_argument("--red-time", type=float, default=3, help="Time the red light is on")
    parser.add_argument("--green-time", type=float, default=3, help="Time the green light is on")
    parser.add_argument("--yellow-time", type=float, default=1, help="Time the yellow light is on")

    args = parser.parse_args()
    main(args.red_time, args.green_time, args.yellow_time)
