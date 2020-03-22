# maintainer: matiamic@fel.cvut.cz

from ics import Calendar, Event
from datetime import timedelta
import arrow
from copy import deepcopy
import requests


def get_event(file, calendar, program='', endtoken='INPUTEND') -> int:
    e = Event()
    e.name = file.readline()[:-1]
    if e.name == '':
        return 0  # no more events in the input file
    if e.name == endtoken:
        return 0
    if e.name[-3:] == 'END' or e.name[-5:] == 'START':
        file.readline()
        return 1  # just skip it
    begin = arrow.get(file.readline()[:-1]).replace(tzinfo='Europe/Prague')
    end = arrow.get(file.readline()[:-1]).replace(tzinfo='Europe/Prague')
    e.begin = begin
    e.end = end
    e.description = file.readline()[:-1]
    e.url = file.readline()[:-1]
    e.location = file.readline()[:-1]
    lecturers = file.readline()[:-1]
    e.description += ' - ' + lecturers
    if program and program not in e.name[e.name.index('['):]:
        file.readline()
        return 1  # dont make an event, go to the next record
    if input('Chces do rozvrhu ' + e.name + ' ' + weekday_tranlate(e.begin.strftime('%A')) + ' od ' +
             e.begin.strftime('%H:%M') + ' s ' + lecturers + '? (y/n)') in ('y', 'yes'):
        calendar.events.add(e)
    file.readline()
    return 1


def make_weekly_recurrence(calendar, how_many_weeks):
    events_aux = deepcopy(calendar.events)
    for event in events_aux:
        for n in range(1, how_many_weeks):
            recurr_event = event.clone()
            recurr_event.uid += str(n)
            recurr_event.end = recurr_event.end + timedelta(days=n * 7)
            recurr_event.begin = recurr_event.begin + timedelta(days=n * 7)
            calendar.events.add(recurr_event)


def skip_after(file, tag):
    while file.readline() not in (tag + 'START\n', ''):
        pass
    return tag + 'END'


def weekday_tranlate(english):
    dictionary = {'Monday': 'v pondeli', 'Tuesday': 'v utery', 'Wednesday': 've stredu', 'Thursday': 've ctvrtek',
                  'Friday': 'v patek', 'Saturday': 'v sobotu', 'Sunday': 'v nedeli'}
    return dictionary[english]


def get_programs_str(programs_list):
    string = programs_list[0]
    for i in range(1, len(programs_list)):
        if i == len(programs_list) - 1:
            string += ' a ' + programs_list[i]
        else:
            string += ', ' + programs_list[i]
    return string

cal = Calendar()
net = input("Chces nacist rozvrh z Kyrcal.in (funguje vzdycky), nebo z Internetu, kde na tom delame spolecne (aktualni)? (k/i)")
next_program = 'y'
programs_written = list()
while next_program in ('y', 'yes'):
    if net in ('k', 'K'):
        inp = open('felcal.in', 'r')
    else:
        with open('input_url.txt', 'r') as urlf:
            url = urlf.readline()
            urlf.close()
        with open('felcal_collabedit.in', 'w') as download:
            download.write(requests.get(url).text)
            download.close()
        inp = open('felcal_collabedit.in', 'r')

    end_token = skip_after(inp, 'INPUT')
    program = input('Predmety z jakeho oboru chces v kalendari? (tag oboru napr. "OI", "KyR", ..., zadny vyber = vsechny obory)')
    inp.readline()

    while get_event(inp, cal, program, end_token):
        pass
    inp.close()
    next_program = 'n'
    if program:
        programs_written.append(program)
        next_program = input('Chces pridat predmety z jinych oboru nez z ' + get_programs_str(programs_written) + '? (y/n)')

weeks = int(input('Na kolik tydnu to vidis?'))
make_weekly_recurrence(cal, weeks)

with open('felcal.ics', 'w') as out:
    out.write(str(cal))
    out.close()
