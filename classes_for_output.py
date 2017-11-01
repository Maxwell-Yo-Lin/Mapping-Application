# Maxwell Lin 46268364
import API

class LATLONG:
    def __init__(self,json):
        self._description = API.print_latlong(json)
    def print(self):
        print(self._description)


class STEPS:

    def __init__(self,json):
        self._description = API.print_steps(json)

    def print(self):
        print(self._description)


class TOTALTIME:
    def __init__(self,json):
        self._description = API.get_total_time(json)
    def print(self):
        print(self._description+'\n')

class TOTALDISTANCE:
    def __init__(self,json):
        self._description = API.get_total_distance(json)
    def print(self):
        print(self._description+'\n')

class ELEVATION:
    def __init__(self,json):
        _latlong_pairs = API.get_latlong(json)
        _elevation_parameters = API.get_elevation_parameters(_latlong_pairs)
        _elevation_urls = API.get_elevation_urls(_elevation_parameters)
        _elevation_list = API.get_elevations(_elevation_urls)
        _result = "ELEVATIONS \n"
        for i in _elevation_list:
            _result += i+"\n"
        self._description = _result
    def print(self):
        print(self._description)

