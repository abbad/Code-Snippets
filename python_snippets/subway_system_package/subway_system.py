from subway_system_exceptions import NoStopsProvidedException, LineNameAlreadyExistsException, \
    NoTimeFoundBetweenStopsException, EmptyLineNameException, OneStationIsNotATrainLine
from dijkstra import dijkstra

__author__ = 'Abbad'

class TrainLine(object):

    def __init__(self, stops, name, time_between_stations):
        """
        :param stops: List of stops.
        :param name: String which the name of the stop.
        :param time_between_stations: tuple consisting of 2 stations and a the time between them in minutes.
        ("station_a", "station_b", 2)
        :return:
        """
        if name == "":
            raise EmptyLineNameException()

        if len(stops) == 0:
            raise NoStopsProvidedException()

        if len(stops) == 1:
            raise OneStationIsNotATrainLine()

        self.name = name
        self.stops = stops
        self.time_between_stations = time_between_stations


class SubwaySystem(object):

    def __init__(self):
        self.network = {}  # This is the network of trains.
        self.train_lines = {}
        self.with_time = None

    def add_train_line(self, stops, name, time_between_stations=None):
        """
        :param stops: list of each stop on the train line.
        :param name: name of the line.
        :param time_between_stations: time between each station and it is bidirectional.
        :return:
        """

        # Create a new object of TrainLine. This is only used for the records.
        train_line = TrainLine(stops, name, time_between_stations)

        if name in self.train_lines:
            raise LineNameAlreadyExistsException()

        self.train_lines[name] = train_line

        # Add stations to the network of trains which is a graph.
        self.add_stops_to_network(train_line)

    def add_stops_to_network(self, train_line):
        """
        :param train_line: train_line object that contains distances and stops.
        :return: None
        """
        # Loop over the stops and start adding them to the graph with their weights.
        for idx in range(1, len(train_line.stops)):
            stop_a = train_line.stops[idx - 1]
            stop_b = train_line.stops[idx]

            time_between_stop_a_stop_b = self.get_time_estimate(stop_a, stop_b, train_line.time_between_stations) \
                if train_line.time_between_stations else 0

            if stop_a in self.network:
                self.network[stop_a].update({stop_b: time_between_stop_a_stop_b})
            else:
                self.network[stop_a] = {stop_b: time_between_stop_a_stop_b}
            if stop_b in self.network:
                self.network[stop_b].update({stop_a: time_between_stop_a_stop_b})
            else:
                self.network[stop_b] = {stop_a: time_between_stop_a_stop_b}

    def take_train(self, origin, destination):
        """
        :param origin: Original train station from the location where the journey will begin.
        :param destination: Destination is where the passenger has already begun.
        :return: a tuple of list of stations and time if time_between stations was given.
        :Note: This function will behave fine with weighted and non wighted graphs.
        """
        return dijkstra(self.network, origin, destination)

    def get_time_estimate(self, station_a, station_b, time_between_stations):
        """
        This function will get you the time estimate between a and b or b and a
        :param station_a: Name of the first station.
        :param station_b: Name of the second station.
        :return: int presenting time between a and b in minutes.
        :exception if time is not found an exception would occur.
        """
        for time_between_two_stations in time_between_stations:
            if station_a in time_between_two_stations and station_b in time_between_two_stations:
                return time_between_two_stations[2]

        raise NoTimeFoundBetweenStopsException("Time is not found between the following train stations " +
                                               str(station_a) + " " + str(station_b))


if __name__ == "__main__":
    # This is a playground. It used for quick debugging.
    subway_system = SubwaySystem()

    subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1",
                                 time_between_stations=[("Canal", "Houston", 3),
                                                        ("Houston", "Christopher", 7),
                                                        ("Christopher", "14th", 2)])

    subway_system.add_train_line(stops=["8th", "14th", "6th", "Union Square"], name="L",
                                 time_between_stations=[("8th", "14th", 3),
                                                        ("14th", "6th", 7),
                                                        ("Union Square", "6th", 2)])