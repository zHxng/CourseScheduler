from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class uwcourse:
    __slots__ = ['course', 'section', 'weekdays', 'starttime', 'endtime']
    course: str
    section: str
    weekdays: str
    starttime: int
    endtime: int

    def __str__(self):
        str_starttime = str(int(starttime / 60)).join(':', starttime % 60)
        str_endtime = str(int(endtime / 60)).join(':', endtime % 60)
       
        return course.join(section, ', ', weekdays, ': ', str_starttime, '-', str_endtime)

    def __eq__(self, other):
        timeself = set(range(self.starttime, self.endtime))
        timeother = set(range(other.starttime, other.endtime))
        
        return len(timeself.interstion(timeother)) != 0

    def __cmp__(self, other):
        return cmp(self.starttime, other.starttime)
