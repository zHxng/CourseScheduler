import json
import os
from util import uwcourse
from uwaterlooapi import UWaterlooAPI

class APIKeyMissingError(Exception):
    pass

def timetoint(strtime):
    if strtime is None:
        return None
    time = strtime.split(':')
    return int(time[0]) * 60 + int(time[1])

def getschedule(courses: list):
    UW_API_KEY = os.environ.get('UW_API_KEY', None)
    
    if UW_API_KEY is None:
        raise APIKeyMissingError(
            "Missing: UW_API_KEY"
            "All methods require an API Key. "
            "Refer to https://uwaterloo.ca/api/ "
            "For how to register for an API key."
        )

    fetcher = UWaterlooAPI(api_key=UW_API_KEY)
    
    schedule = []
    for cur_course in courses:
        course_id = cur_course.split(' ')
        course_sections = fetcher.course_schedule(course_id[0], course_id[1])

        for section in course_sections:
            if int(section['enrollment_capacity'])-int(section['enrollment_total']) > 0 and 'LEC' in section['section']:
                starttime = timetoint(section['classes'][0]['date']['start_time'])
                endtime = timetoint(section['classes'][0]['date']['end_time'])
                course = uwcourse(cur_course, section['section'], section['classes'][0]['date']['weekdays'], starttime, endtime, {})

                schedule.append(course)

    return schedule
