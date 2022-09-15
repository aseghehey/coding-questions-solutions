"""
Given an array of strings that represents the start time of servers
and a string shutDownTime representing the end time

Write a function that returns the total number of minutes spent from the start of every server until the
shutdowntime

"""

def shutDown(startTimes, shutDownTimes):
    shutdownHr, shutdownMin = shutDownTimes.split(':')
    res = 0
    for time in startTimes:
        hr, minute = time.split(':')
        res += (abs(int(hr) - int(shutdownHr)) * 60) + (int(shutdownMin) - int(minute))
    return res

print(shutDown(['12:01','00:00', '23:58', '23:59'], '23:59')) # must return 2158
print(shutDown(['12:30', '14:00', '19:55'], '20:00')) # must return 815
