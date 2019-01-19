from . import getschedule
from util import uwcourse


restrictions = {'mintime':0, 'maxtime':1439}

def prunecourses(courses: list, mintime, maxtime):
    pruned = []
    for cur_course in courses:
        if cur_course.starttime is not None and cur_course.starttime > mintime and cur_course.endtime < maxtime:
            pruned.append(cur_course)

    return pruned

def makeschedule(courses: list, res: list):
    for r in res:
        rparse = r.split("=")
        if rparse[0] in restrictions:
            restrictions[rparse[0]] = rparse[1]

    allcourses = getschedule(courses)
    allcourses.sort()

    prunedcourses = prunecourses(allcourses, int(restrictions['mintime']), int(restrictions['maxtime']))

    schedule = []
    for cur_course in prunedcourses:
        if cur_course.name in courses and cur_course not in schedule:
            schedule.append(cur_course)
            courses.remove(cur_course.name)

    return schedule
