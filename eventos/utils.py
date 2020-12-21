from datetime import datetime, timedelta, date
from calendar import HTMLCalendar
from .models import Event

import datetime as dt


class Calendar(HTMLCalendar):
    def __init__(self, events=None):
        super(Calendar, self).__init__()
        self.events = events
        #print(events)

    def formatday(self, day, weekday, events):

        events_from_day = events.filter(day__day=day)
        #print(events_from_day)
        events_html = "<ul>"
        for event in events_from_day:
            events_html += event.get_html_url + "<br>"
        events_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'  # day outside month
        else:
            return '<td class="%s">%d%s</td>' % (self.cssclasses[weekday], day, events_html)


    def formatweek(self, theweek, events):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd, events) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s


    def formatmonth(self, year, month, withyear=True):

        events = Event.objects.filter(day__month=month)

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month">')
        a('\n')
        a(self.formatmonthname(year, month, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(year, month):
            a(self.formatweek(week, events))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)