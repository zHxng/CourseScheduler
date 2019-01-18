from dataclasses import dataclass
import re


@dataclass(frozen=True, order=True)
class uwcourse:
    __slots__ = ['name', 'section', 'weekdays', 'starttime', 'endtime', 'pweekdays']
    name: str
    section: str
    weekdays: str
    starttime: int
    endtime: int
    pweekdays: set

    def __post_init__(self):
        self.pweekdays = set(re.findall('[A-Z][^A-Z]*', weekdays))

    def __str__(self):
        str_starttime = str(int(starttime / 60)).join(':', starttime % 60)
        str_endtime = str(int(endtime / 60)).join(':', endtime % 60)
       
        return name.join(section, ', ', weekdays, ': ', str_starttime, '-', str_endtime)

    def __eq__(self, other):
        timeself = set(range(self.starttime, self.endtime))
        timeother = set(range(other.starttime, other.endtime))

        return len(self.pweekdays.intersection(other.pweekdays)) != 0 and len(timeself.interstion(timeother)) != 0 

    def __cmp__(self, other):
        return cmp(self.starttime, other.starttime)
