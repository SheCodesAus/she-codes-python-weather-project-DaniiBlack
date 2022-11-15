import csv
from datetime import datetime 

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return(date.strftime("%A %d %B %Y"))

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    num = float(temp_in_farenheit)

    conversion = (num - 32) / 1.8
    return round(conversion, 1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    result = 0
    for count in weather_data:
        result += float(count)
    return(result / len(weather_data))

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)[1:]
        result = []
        for row in data:
            if len(row) > 0:
                result.append([row[0], int(row[1]), int(row[2])])
        return(result)

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # if len(weather_data) == 0:
    #     return()
    # index = 1
    # result = [float(weather_data[0]), 0]
    # for item in weather_data[1:]:
    #     if float(item) <= result[0]:
    #         result = [float(item), index]
    #     index += 1
    # return(result[0], result[1])
    if len(weather_data) == 0:
        return()
    index = 1
    min = float(weather_data[0])
    min_index = 0
    for item in weather_data[1:]:
        if float(item) <= min:
            min = float(item)
            min_index = index
        index += 1
    return(min, min_index)

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    # if len(weather_data) == 0:
    #     return()
    # index = 1
    # result = [float(weather_data[0]), 0]
    # for item in weather_data[1:]:
    #     if float(item) >= result[0]:
    #         result = [float(item), index]
    #     index += 1
    # return(result[0], result[1])
    if len(weather_data) == 0:
        return()
    index = 1
    max = float(weather_data[0])
    max_index = 0
    for item in weather_data[1:]:
        if float(item) >= max:
            max = float(item)
            max_index = index
        index += 1
    return(max, max_index)




def format_min_summary(weather_data):
    def get_min(weather_line_item):
        return weather_line_item[1]
    min_val = list(map(get_min, weather_data))
    min_val_index = find_min(min_val)[1]
    min_weather_line_item = weather_data[min_val_index]
    min_c = format_temperature(convert_f_to_c(min_weather_line_item[1]))
    min_date = convert_date(min_weather_line_item[0])
    return(f"The lowest temperature will be {min_c}, and will occur on {min_date}.")

def format_max_summary(weather_data):
    def get_max(weather_line_item):
        return weather_line_item[2]
    max_val = list(map(get_max, weather_data))
    max_val_index = find_max(max_val)[1]
    max_weather_line_item = weather_data[max_val_index]
    max_c = format_temperature(convert_f_to_c(max_weather_line_item[2]))
    max_date = convert_date(max_weather_line_item[0])
    return(f"The highest temperature will be {max_c}, and will occur on {max_date}.")

def format_min_average(weather_data):
    def get_line_item(weather_line_item):
        return weather_line_item[1]
    min_values = list(map(get_line_item, weather_data))
    min_numbers = calculate_mean(min_values)
    min_celsius = format_temperature(convert_f_to_c((min_numbers)))
    return(f"The average low this week is {min_celsius}.")

def format_max_average(weather_data):
    def get_line_item(weather_line_item):
        return weather_line_item[2]
    max_values = list(map(get_line_item, weather_data))
    max_numbers = calculate_mean(max_values)
    max_celsius = format_temperature(convert_f_to_c((max_numbers)))
    return(f"The average high this week is {max_celsius}.")

def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    return(f"{len(weather_data)} Day Overview\n  {format_min_summary(weather_data)}\n  {format_max_summary(weather_data)}\n  {format_min_average(weather_data)}\n  {format_max_average(weather_data)}\n")

def format_day(line_item):
    return(f"---- {convert_date(line_item[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line_item[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line_item[2]))}\n\n")


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ''
    for line_item in weather_data:
        result += (format_day(line_item))
    return(result)