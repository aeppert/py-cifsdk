from cifsdk.format.plugin import Plugin
import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class Csv(Plugin):

    def __init__(self, *args, **kwargs):
        super(Csv, self).__init__(*args, **kwargs)

    def __repr__(self):
        si = StringIO()
        cw = csv.writer(si)
        for obs in self.data:
            r = []
            for c in self.cols:
                y = obs.get(c) or ''
                if type(y) is list:
                    y = ','.join(y)
                y = str(y)
                y = (y[:self.max_field_size] + '..') if len(y) > self.max_field_size else y
                r.append(y)
            cw.writerow(r)
        return si.getvalue().strip('\r\n')