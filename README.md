# CourseScheduler README
Schedule generator for courses at the University of Waterloo. This project is not affliated with the University of Waterloo.

## uWaterloo API
This program requries a University of Waterloo Open Data API key. You can register for one [here.](https://uwaterloo.ca/api/register) If you already have an API key, create a file called apikey.txt in the /coursescheduler directory and paste your API key in there.

## Usage
Basic Usage:
To select courses to include in the schedule enter the subject and catalog number with a ", " between each course.  <br>
> MATH 138, CS 136, MATH 136, SPCOM 100, ECON 101

To add restrictions to sections included in your schedule, specify in the format "restriction=value" with a ", " seperating each restriction.  <br>
> mintime=298, maxtime=1500

Current supported restrictions are as follows:  <br>

| Restriction | Description | Usage |
| --------------- | ----------| ---- |
| mintime | The earliest time a lecture can start. Time is measured in minutes from 00:00 AM | mintime=600 |
| maxtime | The latest time a lecture can start. Time is measured in minutes from 00:00 AM | maxtime=1080 |
