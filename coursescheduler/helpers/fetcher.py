import json
from .util.structures import uwcourse
import os
from uwaterlooapi import UWaterlooAPI


UW_API_KEY = os.environ.get('UW_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if UW_API_KEY is None:
    raise APIKeyMissingError(
        'Missing: UW_API_KEY '
        'Fetching data requires an API Key. '
        'Refer to https://uwaterloo.ca/api/ '
        'For how to register for an API key.'
    )

fetcher = UWaterlooAPI(api_key=UW_API_KEY)

def time_to_int(strtime):
    time = strtime.split(':')
    return time[0] * 60 + time[1]

def get_schedule(*courses):
    schedule = []
    for cur_course in courses:
        course_id = cur_course.split(" ")
        course_sections = json.loads(fetcher.course_schedule(course_str[0], course_str[1]))['data']

        for section in course_sections:
            if section['enrollment_capacity']-section['enrollment_total'] > 0 and 'LEC' in section['section']:
                starttime = time_to_int(section['classes']['date']['start_time'])
                endtime = time_to_int(section['classes']['date']['start_time'])
                course = uwcourse(cur_course, section['section'], section['classes']['date']['weekdays'], starttime, endtime, set())

                schedule.append(course)

    return schedule
