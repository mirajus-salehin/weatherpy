from datetime import datetime
import math

dt = 1604857571
deg = 21

def FormateTime(UNIX_TIMESTAMP:str):
    '''
    convert UNIX timestamp to human readable formate
    '''

    ts = int(UNIX_TIMESTAMP)
    return datetime.fromtimestamp(ts).strftime('%I:%M %p')

def FormateCardinalDirection(angle:int):
    '''
    converts wind direction to cardinal direction
    '''
    direction = ["N","NE","E","SE","S","SW","W","NW"]
    return direction[math.floor(angle / 45) % 8]