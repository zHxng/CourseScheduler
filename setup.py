from setup import setup, find_packages


requires = ['uwaterlooapi']

setup(
    name='CourseScheduler',
    version='0.1.0',
    description='Schedule generator for courses at the University of Waterloo. ',
    author='Alan Zhang',
    author_email='ay5zhang@edu.uwaterloo.ca',
    install_requires=requires
    license='MIT'
    url='https://github.com/zHxng/CourseScheduler',
    packages=find_packages()
)
