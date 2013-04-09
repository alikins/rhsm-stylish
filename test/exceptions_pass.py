
try:
    int('sdfasdf')
except Exception:
    pass

try:
    int('sdfasdfasdf')
except ValueError:
    pass

try:
    int('sdfsdf')
except ValueError, e:
    print e
