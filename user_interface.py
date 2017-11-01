# Maxwell Lin 46268364
import API
import classes_for_output


def user_interface():

    print (""" The program will take input in the following format:
            - An integer whose value is at least 2, alone on a line, that specifies how many locations the trip will consist of.
            - If there are n locations, the next n lines of input will each describe one location. Each location can be a city such
                as Irvine, CA, an address such as 4545 Campus Dr, Irvine, CA, or anything that the Open MapQuest API will accept as a location. 
            - A positive integer whose value is at least 1, alone on a line, that specifies how many outputs will need to be generated.
            - If there are m outputs, the next m lines of input will each describe one output. Each output can be one of the following -> (STEPS,TOTALDISTANCE,TOTALTIME,LATLONG,ELEVATION)
            
            Sample input:
                3
                4533 Campus Dr, Irvine, CA
                1111 Figueroa St, Los Angeles, CA
                3799 S Las Vegas Blvd, Las Vegas, NV
                5
                LATLONG
                STEPS
                TOTALTIME
                TOTALDISTANCE
                ELEVATION
            """)

    locations_picked = get_user_input()
    results_picked = get_user_output()
    parameters = API.parameter_get(locations_picked)
    url = API.get_url(parameters)
    data = API.get_result(url)
    if data == {'route': {'routeError': {'message': '', 'errorCode': 0}}, 'info': {'copyright': {'text': '© 2016 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'imageAltText': '© 2016 MapQuest, Inc.'}, 'statuscode': 400, 'messages': ['We are unable to route with the given locations.']}}:
        print ("\nNO ROUTE FOUND ")
        return
    elif data == {'error': 'lol'}:
        print ("\nMAPQUEST ERROR ")
        return
    class_list = output_action(results_picked,data)
    for object in class_list:
        object.print()
    print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')


def get_user_input()->list:
    'This function returns a list of the inputted locations'
    number_of_locations = int(input())
    locations = []
    for i in range (number_of_locations):
        locations.append(input())

    return locations


def get_user_output()->list:
    'This function returns a list of the output they want'
    number_of_outputs = int(input())
    outputs = []
    for i in range (number_of_outputs):
        outputs.append((input().upper()))
    return outputs

def output_action(results_picked:list,data:dict)->list:
    'makes an action based on the output the person wants, using dictionary'
    class_list = []
    action = {
        'LATLONG': complete_latlong,
        'STEPS': complete_steps,
        'TOTALTIME': complete_total_time,
        'TOTALDISTANCE': complete_total_distance,
        'ELEVATION': complete_elevation,
    }

    for i in results_picked:
        class_list.append(action[i.strip()](data))
    return class_list


def complete_latlong(data:dict):
    'declares the ofject with a given class'
    latlong = classes_for_output.LATLONG(data)
    return latlong

def complete_steps(data:dict):
    'declares the ofject with a given class'
    steps = classes_for_output.STEPS(data)
    return steps

def complete_total_time(data:dict):
    'declares the ofject with a given class'
    total_time = classes_for_output.TOTALTIME(data)
    return total_time

def complete_total_distance(data:dict):
    'declares the ofject with a given class'
    total_distance = classes_for_output.TOTALDISTANCE(data)
    return total_distance

def complete_elevation(data:dict):
    'declares the ofject with a given class'
    elevation = classes_for_output.ELEVATION(data)
    return elevation


if __name__ == '__main__':
     user_interface()
