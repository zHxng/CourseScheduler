from . import getschedule
from util import uwcourse


class InvalidRestrictionError(Exception):
    pass

# f_maxtime expects two args: [course, condition]
def f_mintime(args):
    if args[1] is None:
        return False
    if args[0].starttime is None:
        return True

    return args[0].starttime < int(args[1])

# f_maxtime expects two args: [course, condition]
def f_maxtime(args):
    if args[1] is None:
        return False
    if args[0].endtime is None:
        return True
    
    return args[0].endtime > int(args[1])

dispatch = {'mintime':f_mintime, 'maxtime':f_maxtime}
restrictions = dispatch.keys()

def f_dispatch(command, args):
    if command in restrictions:
        return dispatch[command](args)

def makeschedule(courses, res):
    sections = getschedule(courses)
    sections.sort()
    
    for s in sections:
        for r in res:
            if '=' in r:
                r1 = r.split('=')
                if f_dispatch(r1[0], (s, r1[1])):
                    sections.remove(s)

    schedule = []
    for cur_course in sections:
        if cur_course.name in courses and cur_course not in schedule:
            schedule.append(cur_course)
            courses.remove(cur_course.name)

    return schedule
