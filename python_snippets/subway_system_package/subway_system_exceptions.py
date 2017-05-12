__author__ = 'Abbad'


class NoStopsProvidedException(Exception):
    pass


class LineNameAlreadyExistsException(Exception):
    pass


class NoTimeFoundBetweenStopsException(Exception):
    pass


class EmptyLineNameException(Exception):
    pass


class OneStationIsNotATrainLine(Exception):
    pass

