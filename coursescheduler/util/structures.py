from dataclasses import dataclass
import re


@dataclass(order=True)
class uwcourse:
    __slots__ = ['name', 'section', 'weekdays', 'starttime', 'endtime', 'pweekdays']
    name: str
    section: str
    weekdays: str
    starttime: int
    endtime: int
    pweekdays: set

    def __post_init__(self):
        if self.weekdays is not None:
            self.pweekdays = set(re.findall('[A-Z][^A-Z]*', self.weekdays))

    def __str__(self):
        starttime = ''.join((str(int(self.starttime / 60)).zfill(2), ':', str(self.starttime % 60).zfill(2)))
        endtime = ''.join((str(int(self.endtime / 60)).zfill(2), ':', str(self.endtime % 60).zfill(2)))

        return ' '.join((self.name, self.section, self.weekdays,':' ,'-'.join((starttime, endtime))))

    def __eq__(self, other):
        timeself = set(range(self.starttime, self.endtime))
        timeother = set(range(other.starttime, other.endtime))

        return len(self.pweekdays.intersection(other.pweekdays)) != 0 and len(timeself.intersection(timeother)) != 0 

    def __cmp__(self, other):
        return cmp(self.starttime, other.starttime)
