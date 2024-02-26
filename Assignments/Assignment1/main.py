import pygame

from utils import (LightStates,
                   TrafficLight,
                   TrafficSystem)
from draw import (draw_vehicle_straight_and_right_turning_traffic_lights,
                  draw_vehicle_left_turning_traffic_lights,
                  draw_pedestrian_traffic_lights,
                  draw_backgrounds,
                  draw_turning_lights_text,
                  draw_description_text)


def initialize_traffic_system(_red_time, _green_time, _yellow_time):
    north_straight_light = TrafficLight(LightStates.RED)
    south_straight_light = TrafficLight(LightStates.RED)
    west_straight_light = TrafficLight(LightStates.GREEN)
    east_straight_light = TrafficLight(LightStates.GREEN)

    north_left_turning_light = TrafficLight(LightStates.RED)
    south_left_turning_light = TrafficLight(LightStates.RED)
    west_left_turning_light = TrafficLight(LightStates.RED)
    east_left_turning_light = TrafficLight(LightStates.RED)

    north_pedestrian_light = TrafficLight(LightStates.GREEN)
    south_pedestrian_light = TrafficLight(LightStates.GREEN)
    west_pedestrian_light = TrafficLight(LightStates.RED)
    east_pedestrian_light = TrafficLight(LightStates.RED)

    return TrafficSystem(
        north_straight_light, south_straight_light, west_straight_light, east_straight_light,
        north_left_turning_light, south_left_turning_light, west_left_turning_light, east_left_turning_light,
        north_pedestrian_light, south_pedestrian_light, west_pedestrian_light, east_pedestrian_light,
        _red_time, _green_time, _yellow_time
    )


def update_traffic_lights(_cycle_time, _traffic_system):
    if _cycle_time < _traffic_system.green_time:
        _traffic_system.east_straight_light.set_state(LightStates.GREEN)
        _traffic_system.west_straight_light.set_state(LightStates.GREEN)
        _traffic_system.north_straight_light.set_state(LightStates.RED)
        _traffic_system.south_straight_light.set_state(LightStates.RED)

        _traffic_system.east_left_turning_light.set_state(LightStates.RED)
        _traffic_system.west_left_turning_light.set_state(LightStates.RED)
        _traffic_system.north_left_turning_light.set_state(LightStates.RED)
        _traffic_system.south_left_turning_light.set_state(LightStates.RED)

        _traffic_system.north_pedestrian_light.set_state(LightStates.GREEN)
        _traffic_system.south_pedestrian_light.set_state(LightStates.GREEN)
        _traffic_system.west_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.east_pedestrian_light.set_state(LightStates.RED)
    elif _cycle_time < _traffic_system.green_time + _traffic_system.yellow_time:
        _traffic_system.east_straight_light.set_state(LightStates.YELLOW)
        _traffic_system.west_straight_light.set_state(LightStates.YELLOW)
        _traffic_system.north_straight_light.set_state(LightStates.RED)
        _traffic_system.south_straight_light.set_state(LightStates.RED)

        _traffic_system.east_left_turning_light.set_state(LightStates.RED)
        _traffic_system.west_left_turning_light.set_state(LightStates.RED)
        _traffic_system.north_left_turning_light.set_state(LightStates.RED)
        _traffic_system.south_left_turning_light.set_state(LightStates.RED)

        _traffic_system.north_pedestrian_light.set_state(LightStates.GREEN)
        _traffic_system.south_pedestrian_light.set_state(LightStates.GREEN)
        _traffic_system.west_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.east_pedestrian_light.set_state(LightStates.RED)
    elif _cycle_time < _traffic_system.green_time + _traffic_system.yellow_time + _traffic_system.green_time:
        _traffic_system.east_straight_light.set_state(LightStates.RED)
        _traffic_system.west_straight_light.set_state(LightStates.RED)
        _traffic_system.north_straight_light.set_state(LightStates.RED)
        _traffic_system.south_straight_light.set_state(LightStates.RED)

        _traffic_system.east_left_turning_light.set_state(LightStates.GREEN)
        _traffic_system.west_left_turning_light.set_state(LightStates.GREEN)
        _traffic_system.north_left_turning_light.set_state(LightStates.RED)
        _traffic_system.south_left_turning_light.set_state(LightStates.RED)

        _traffic_system.north_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.south_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.west_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.east_pedestrian_light.set_state(LightStates.RED)
    elif (_cycle_time < _traffic_system.green_time + _traffic_system.yellow_time + _traffic_system.green_time +
          _traffic_system.yellow_time):
        _traffic_system.east_straight_light.set_state(LightStates.RED)
        _traffic_system.west_straight_light.set_state(LightStates.RED)
        _traffic_system.north_straight_light.set_state(LightStates.RED)
        _traffic_system.south_straight_light.set_state(LightStates.RED)

        _traffic_system.east_left_turning_light.set_state(LightStates.YELLOW)
        _traffic_system.west_left_turning_light.set_state(LightStates.YELLOW)
        _traffic_system.north_left_turning_light.set_state(LightStates.RED)
        _traffic_system.south_left_turning_light.set_state(LightStates.RED)

        _traffic_system.north_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.south_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.west_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.east_pedestrian_light.set_state(LightStates.RED)
    elif (_cycle_time < _traffic_system.green_time + _traffic_system.yellow_time + _traffic_system.green_time +
          _traffic_system.yellow_time + _traffic_system.green_time):
        _traffic_system.east_straight_light.set_state(LightStates.RED)
        _traffic_system.west_straight_light.set_state(LightStates.RED)
        _traffic_system.north_straight_light.set_state(LightStates.GREEN)
        _traffic_system.south_straight_light.set_state(LightStates.GREEN)

        _traffic_system.east_left_turning_light.set_state(LightStates.RED)
        _traffic_system.west_left_turning_light.set_state(LightStates.RED)
        _traffic_system.north_left_turning_light.set_state(LightStates.RED)
        _traffic_system.south_left_turning_light.set_state(LightStates.RED)

        _traffic_system.north_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.south_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.west_pedestrian_light.set_state(LightStates.GREEN)
        _traffic_system.east_pedestrian_light.set_state(LightStates.GREEN)
    elif (_cycle_time < _traffic_system.green_time + _traffic_system.yellow_time + _traffic_system.green_time +
          _traffic_system.yellow_time + _traffic_system.green_time + _traffic_system.yellow_time):
        _traffic_system.east_straight_light.set_state(LightStates.RED)
        _traffic_system.west_straight_light.set_state(LightStates.RED)
        _traffic_system.north_straight_light.set_state(LightStates.YELLOW)
        _traffic_system.south_straight_light.set_state(LightStates.YELLOW)

        _traffic_system.east_left_turning_light.set_state(LightStates.RED)
        _traffic_system.west_left_turning_light.set_state(LightStates.RED)
        _traffic_system.north_left_turning_light.set_state(LightStates.RED)
        _traffic_system.south_left_turning_light.set_state(LightStates.RED)

        _traffic_system.north_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.south_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.west_pedestrian_light.set_state(LightStates.GREEN)
        _traffic_system.east_pedestrian_light.set_state(LightStates.GREEN)
    elif (_cycle_time < _traffic_system.green_time + _traffic_system.yellow_time + _traffic_system.green_time +
          _traffic_system.yellow_time + _traffic_system.green_time + _traffic_system.yellow_time +
          _traffic_system.green_time):
        _traffic_system.east_straight_light.set_state(LightStates.RED)
        _traffic_system.west_straight_light.set_state(LightStates.RED)
        _traffic_system.north_straight_light.set_state(LightStates.RED)
        _traffic_system.south_straight_light.set_state(LightStates.RED)

        _traffic_system.east_left_turning_light.set_state(LightStates.RED)
        _traffic_system.west_left_turning_light.set_state(LightStates.RED)
        _traffic_system.north_left_turning_light.set_state(LightStates.GREEN)
        _traffic_system.south_left_turning_light.set_state(LightStates.GREEN)

        _traffic_system.north_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.south_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.west_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.east_pedestrian_light.set_state(LightStates.RED)
    elif (_cycle_time < _traffic_system.green_time + _traffic_system.yellow_time + _traffic_system.green_time +
          _traffic_system.yellow_time + _traffic_system.green_time + _traffic_system.yellow_time +
          _traffic_system.green_time + _traffic_system.yellow_time):
        _traffic_system.east_straight_light.set_state(LightStates.RED)
        _traffic_system.west_straight_light.set_state(LightStates.RED)
        _traffic_system.north_straight_light.set_state(LightStates.RED)
        _traffic_system.south_straight_light.set_state(LightStates.RED)

        _traffic_system.east_left_turning_light.set_state(LightStates.RED)
        _traffic_system.west_left_turning_light.set_state(LightStates.RED)
        _traffic_system.north_left_turning_light.set_state(LightStates.YELLOW)
        _traffic_system.south_left_turning_light.set_state(LightStates.YELLOW)

        _traffic_system.north_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.south_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.west_pedestrian_light.set_state(LightStates.RED)
        _traffic_system.east_pedestrian_light.set_state(LightStates.RED)


if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption("Traffic System Simulation")
    clock = pygame.time.Clock()

    red_time, green_time, yellow_time = 5, 5, 2
    traffic_system = initialize_traffic_system(red_time, green_time, yellow_time)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        current_time = pygame.time.get_ticks() / 1000  # Convert milliseconds to seconds

        cycle_time = current_time % (traffic_system.green_time + traffic_system.yellow_time +
                                     traffic_system.green_time + traffic_system.yellow_time +
                                     traffic_system.green_time + traffic_system.yellow_time +
                                     traffic_system.green_time + traffic_system.yellow_time)
        update_traffic_lights(cycle_time, traffic_system)

        draw_description_text(screen)
        draw_backgrounds(screen)
        draw_vehicle_straight_and_right_turning_traffic_lights(screen, traffic_system)
        draw_vehicle_left_turning_traffic_lights(screen, traffic_system)
        draw_pedestrian_traffic_lights(screen, traffic_system)
        draw_turning_lights_text(screen)

        pygame.display.flip()
        clock.tick(60)  # FPS

    pygame.quit()

