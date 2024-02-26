from enum import Enum, auto


class LightStates(Enum):
    GREEN = auto()
    YELLOW = auto()
    RED = auto()


class TrafficLight:
    def __init__(self, initial_state: LightStates):
        self.state = initial_state

    def set_state(self, new_state: LightStates):
        self.state = new_state

    def is_green(self):
        return self.state == LightStates.GREEN

    def is_yellow(self):
        return self.state == LightStates.YELLOW

    def is_red(self):
        return self.state == LightStates.RED


class TrafficSystem:
    def __init__(self, north_straight_light, south_straight_light, west_straight_light, east_straight_light,
                 north_left_turning_light, south_left_turning_light, west_left_turning_light, east_left_turning_light,
                 north_pedestrian_light, south_pedestrian_light, west_pedestrian_light, east_pedestrian_light,
                 red_time, green_time, yellow_time):
        self.north_straight_light = north_straight_light
        self.south_straight_light = south_straight_light
        self.west_straight_light = west_straight_light
        self.east_straight_light = east_straight_light

        self.north_left_turning_light = north_left_turning_light
        self.south_left_turning_light = south_left_turning_light
        self.west_left_turning_light = west_left_turning_light
        self.east_left_turning_light = east_left_turning_light

        self.north_pedestrian_light = north_pedestrian_light
        self.south_pedestrian_light = south_pedestrian_light
        self.west_pedestrian_light = west_pedestrian_light
        self.east_pedestrian_light = east_pedestrian_light

        self.red_time = red_time
        self.green_time = green_time
        self.yellow_time = yellow_time

