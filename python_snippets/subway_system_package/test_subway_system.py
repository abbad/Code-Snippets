from subway_system import SubwaySystem, TrainLine
from unittest import TestCase, main
from subway_system_exceptions import NoStopsProvidedException, EmptyLineNameException, \
    NoTimeFoundBetweenStopsException, LineNameAlreadyExistsException, OneStationIsNotATrainLine


class TestSubwaySystemClassExceptions(TestCase):
    """
        Tests to cover subway system class exceptions.
    """

    def setUp(self):
        self.subway_system = SubwaySystem()

    def test_no_stops(self):
        """
        Test when there is no stops provided.
        """
        with self.assertRaises(NoStopsProvidedException):
            self.subway_system.add_train_line([], 'A', ('B', 'C', '2'))

    def test_add_train_line_no_name(self):
        """
        Test when calling the add_train_line function with no name for the line.
        :return:
        """
        with self.assertRaises(EmptyLineNameException):
            self.subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="")

    def test_add_train_line_no_time_found_exception(self):
        """
        Test when add train line function with no train time found.
        """
        with self.assertRaises(NoTimeFoundBetweenStopsException):
            self.subway_system.add_train_line(["Canal", "Houston", "Christopher", "14th"],"adssad",
                                              [("adsdas", "blabla", 4)])

    def test_add_train_line_duplicate(self):
        """
        Test when add train line is called with a duplicate path name
        """

        with self.assertRaises(LineNameAlreadyExistsException):
            self.subway_system.add_train_line(["Canal", "Houston", "Christopher", "14th"], name="Duplicate")
            self.subway_system.add_train_line(["Canal", "Houston", "Christopher", "14th"], name="Duplicate")

    def test_add_train_station_with_one_station(self):
        """
            Test function when sending a train station with only one station.
        """
        with self.assertRaises(OneStationIsNotATrainLine):
            self.subway_system.add_train_line(["Canal"], name="alpha")

class TestAddTrainLineFunction(TestCase):
    """
        A couple of tests to cover add_train_line_function.
    """

    def setUp(self):
        self.subway_system = SubwaySystem()

    def test_add_train_line_with_one_line(self):
        """
        Test when sending one line.
        """
        expected_network = {'Canal': {'Houston': 3}, 'Houston': {'Canal': 3, 'Christopher': 7},
                            'Christopher': {'Houston': 7, '14th': 2}, '14th': {'Christopher': 2}}

        self.subway_system.add_train_line(stops=["Canal", "Houston", "Christopher", "14th"], name="1",
                                     time_between_stations=[("Canal", "Houston", 3),
                                                            ("Houston", "Christopher", 7),
                                                            ("Christopher", "14th", 2)])

        self.assertEqual(self.subway_system.network, expected_network)

    def test_add_train_line_with_two_lines(self):
        """
        Test when sending train station with two different lines.

        Y --- A --- X
              |
              B
              |
              C
        """

        expected_network = {'A': {'B': 3, 'X': 3, 'Y': 7}, 'B': {'A': 3, 'C': 7}, 'C': {'B': 7},
                            'X': {'A': 3}, 'Y': {'A': 7}}

        self.subway_system.add_train_line(stops=["A", "B", "C"], name="1",
                                          time_between_stations=[("A", "B", 3),
                                                                 ("B", "C", 7)])

        self.subway_system.add_train_line(stops=["X", "A", "Y"], name="5",
                                          time_between_stations=[("X", "A", 3),
                                                            ("A", "Y", 7)])

        self.assertEqual(expected_network, self.subway_system.network)

    def test_add_train_station_3_different_lines(self):
        """                     (Line 2)
                               4
                               / \
                             3     A1
                            /       \
            A -- B -- C -- D -- E -- F   (Line 1)
                          /           \
                          |            A2
                          2             |
                          |            A3
                          1              (Line 3)
        """
        expected_output = {'A': {'B': 0}, 'A1': {'4': 0, 'F': 0}, 'C': {'B': 0, 'D': 0}, 'B': {'A': 0, 'C': 0}, 'E':
            {'D': 0, 'F': 0}, 'D': {'C': 0, '2': 0, 'E': 0, '3': 0}, 'F': {'A1': 0, 'A2': 0, 'E': 0},
                           'A3': {'A2': 0}, '1': {'2': 0}, '3': {'D': 0, '4': 0}, '2': {'1': 0, 'D': 0},
                           '4': {'A1': 0, '3': 0}, 'A2': {'A3': 0, 'F': 0}}

        self.subway_system.add_train_line(['A', 'B', 'C', 'D', 'E', 'F'], 'Line 1')
        self.subway_system.add_train_line(['1', '2', 'D', '3', '4'], 'Line 2')
        self.subway_system.add_train_line(['A3', 'A2', 'F', 'A1', '4'], 'Line 3')

        self.assertEqual(self.subway_system.network, expected_output)

    def test_add_train_line_no_time_between(self):
        """
        Test add_train_line function when calling it with no time in between.
         (Line 2)
                               4
                               / \
                             3     A1
                            /       \
            A -- B -- C -- D -- E -- F   (Line 1)
                          /           \
                          |            A2
                          2             |
                          |            A3
                          1              (Line 3)
        """

        expected_output = {'A': {'B': 0}, 'A1': {'4': 0, 'F': 0}, 'C': {'B': 0, 'D': 0}, 'B': {'A': 0, 'C': 0},
                            'E': {'D': 0, 'F': 0}, 'D': {'C': 0, '2': 0, 'E': 0, '3': 0}, 'F':
                                {'A1': 0, 'A2': 0, 'E': 0}, 'A3': {'A2': 0}, '1': {'2': 0}, '3': {'D': 0, '4': 0},
                            '2': {'1': 0, 'D': 0}, '4': {'A1': 0, '3': 0}, 'A2': {'A3': 0, 'F': 0}}

        self.subway_system.add_train_line(['A', 'B', 'C', 'D', 'E', 'F'], 'Line 1')
        self.subway_system.add_train_line(['1', '2', 'D', '3', '4'], 'Line 2')
        self.subway_system.add_train_line(['A3', 'A2', 'F', 'A1', '4'], 'Line 3')

        self.assertEqual(expected_output, self.subway_system.network)


class TestTakeTrainFunctionWithTimeBetweenStations(TestCase):
    """
        Test to cover take train function.
    """

    def setUp(self):
        """                     (Line 2)
                                4
                               / \
                             3     A1
                            /       \
            A -- B -- C -- D -- E -- F   (Line 1)
                          /           \
                          |            A2
                          2             |
                          |            A3
                          1              (Line 3)
        """
        self.subway_system = SubwaySystem()
        self.subway_system.add_train_line(['A', 'B', 'C', 'D', 'E', 'F'], 'Line 1', [('A', 'B', 3),
                                                                                     ('B', 'C', 5),('C', 'D', 5),
                                                                                     ('D', 'E', 10),
                                                                                     ('E', 'F', 15)])

        self.subway_system.add_train_line(['1', '2', 'D', '3', '4'], 'Line 2', [('1', '2', 5), ('2', 'D', 5),
                                                                                ('D', '3', 1), ('3', '4', 10)])

        self.subway_system.add_train_line(['A3', 'A2', 'F', 'A1', '4'], 'Line 3', [('A3', 'A2', 2), ('A2', 'F', 5),
                                                                                   ('F', 'A1', 2),
                                                                                   ('A1', '4', 10)])

    def test_take_train_from_f_to_1(self):
        self.assertEqual(self.subway_system.take_train('F', '1'), (['F', 'A1', '4', '3', 'D', '2', '1'], 33))

    def test_take_train_from_A_To_A3(self):
        """
        Test take train function when going from A to A3
        :return:
        """

        self.assertEqual(self.subway_system.take_train('A', 'A3'),
                         (['A', 'B', 'C', 'D', '3', '4', 'A1', 'F', 'A2', 'A3'], 43))

    def test_take_train_from_A_To_A3_with_direct_connection(self):
        """
        Test take train function when going from A to A3 Directly
        :return:
        """
        self.subway_system.add_train_line(['A', 'A3'], "Subway to heaven", [('A', 'A3', 0.5)])

        self.assertEqual(self.subway_system.take_train('A', 'A3'), (['A', 'A3'], 0.5))

    def test_take_train_from_4_to_E(self):
        """
        Test take train from 4 to E
        """
        self.assertEqual(self.subway_system.take_train('4', 'E'), (['4', '3', 'D', 'E'], 21))


class TestTakeTrainFunctionWithNoTimeBetweenStations(TestCase):
    """
        Test function take_train with no time is provided between train stations.
    """

    def setUp(self):
        """                     (Line 2)
                                4
                               / \
                             3     A1
                            /       \
            A -- B -- C -- D -- E -- F   (Line 1)
                          /           \
                          |            A2
                          2             |
                          |            A3
                          1              (Line 3)
        """
        self.subway_system = SubwaySystem()
        self.subway_system.add_train_line(['A', 'B', 'C', 'D', 'E', 'F'], 'Line 1')

        self.subway_system.add_train_line(['1', '2', 'D', '3', '4'], 'Line 2')

        self.subway_system.add_train_line(['A3', 'A2', 'F', 'A1', '4'], 'Line 3')

    def test_take_train_function_when_sending_A_A3(self):
        """
        :return:
        """
        self.assertEqual(self.subway_system.take_train("A", "A3"), (['A', 'B', 'C', 'D', 'E', 'F', 'A2', 'A3'], None))

    def test_take_train_function_when_sending_A_A3_with_direct_route(self):
        """
        Test take train function when having a direct route from A to A3
        :return:
        """

        self.subway_system.add_train_line(["A", "A3"], "Subway To Heaven", None)
        self.assertEqual(self.subway_system.take_train("A", "A3"), (['A', 'A3'], None))

    def test_take_train_function_when_sending_A_A3_with_direct_route_backwards(self):
        """
        Test take train function when having a direct route from A to A3 and going backwards
        :return:
        """

        self.subway_system.add_train_line(["A", "A3"], "Subway To Heaven", None)
        self.assertEqual(self.subway_system.take_train("A3", "A"), (['A3', 'A'], None))


class TestTrainLineClass(TestCase):
    """
    Test TrainLine class
    """

    def setUp(self):
        pass

    def test_normal_input(self):
        """
        :return:
        """
        stops = ["STATION 1", "STATION 2"]
        name_of_the_station = "2 stations"
        time_between_stations = ("STATION 1", "STATION 2", 2)

        train_line = TrainLine(stops, name_of_the_station, time_between_stations)

        self.assertEqual(train_line.name, name_of_the_station)
        self.assertEqual(train_line.stops, stops)
        self.assertEqual(train_line.time_between_stations, time_between_stations)

if __name__ == '__main__':
    main()
