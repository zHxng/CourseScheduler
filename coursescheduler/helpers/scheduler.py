from fetcher import get_schedule
from .util.structures import uwcourse


def prune_courses(*courses, mintime, maxtime):
    pruned = []
    for cur_course in courses:
        if cur_course.starttime > mintime and cur_course.endtime < maxtime:
            pruned.append(cur_course)

    return pruned

def make_schedule(*courses, mintime=0, maxtime=1439):
    allcourses = get_schedule(courses)
    allcourses.sort()

    prunedcourses = prune_courses(allcourses, mintime, maxtime)

    schedule = []
    for cur_course in prunedcourses:
        if cur_course.name in courses and cur_course not in schedule:
            schedule.append(cur_course)

    return schedule
