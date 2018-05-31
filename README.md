# pingrs
Ping Runescape worlds using parallel processing.

Tested with Python 3.5.0.

<pre>
$ python pingrs.py -h
usage: pingrs.py [-h] [-p PINGS] [-w WORKERS] [-v VERBOSITY]
                 [-d DISTINGUISH [DISTINGUISH ...]] [--all-worlds]
                 [worlds [worlds ...]]

Ping Runescape worlds.

positional arguments:
  worlds                worlds to ping

optional arguments:
  -h, --help            show this help message and exit
  -p PINGS, --pings PINGS
                        number of pings for each batch (default: 1)
  -w WORKERS, --workers WORKERS
                        number of worker processes to spawn (default:
                        os.cpu_count())
  -v VERBOSITY, --verbosity VERBOSITY
                        set verbosity level
  -d DISTINGUISH [DISTINGUISH ...], --distinguish DISTINGUISH [DISTINGUISH ...]
                        distinguish worlds in output
  --all-worlds          ping all worlds (include non-members)
</pre>

Example usage:
<pre>
$ python pingrs.py 104 -p 2
    World 104: Min=  7, Max=  8, Avg=7.5

</pre>

Ping values are in milliseconds.

All arguments are optional. By default, it will ping all members worlds once:

<pre>
$ python pingrs.py
    World  12: Ping=221.0
    World 102: Ping=99.0
    World  54: Ping=97.0
    World  69: Ping=97.0
    World 106: Ping=95.0
    World   5: Ping=94.0
    World  26: Ping=93.0
    World  21: Ping=93.0
    World 123: Ping=92.0
    World  10: Ping=91.0
    World  16: Ping=91.0
    World  28: Ping=91.0
    World 105: Ping=91.0
    World 137: Ping=91.0
    World  24: Ping=90.0
    World 119: Ping=89.0
    World 121: Ping=89.0
    World 124: Ping=89.0
    World  32: Ping=88.0
    World  84: Ping=87.0
    World 138: Ping=87.0
    World  67: Ping=86.0
    World  71: Ping=86.0
    World 139: Ping=86.0
    World  23: Ping=85.0
    World  63: Ping=85.0
    World  56: Ping=85.0
    World  36: Ping=84.0
    World  25: Ping=84.0
    World  53: Ping=84.0
    World  83: Ping=84.0
    World  82: Ping=84.0
    World  68: Ping=84.0
    World  92: Ping=84.0
    World 118: Ping=84.0
    World 134: Ping=84.0
    World  88: Ping=83.0
    World  96: Ping=82.0
    World  86: Ping=81.0
    World  14: Ping=80.0
    World  85: Ping=78.0
    World  40: Ping=77.0
    World  30: Ping=76.0
    World  37: Ping=75.0
    World   4: Ping=72.0
    World  51: Ping=72.0
    World  65: Ping=71.0
    World  73: Ping=71.0
    World  72: Ping=71.0
    World  97: Ping=32.0
    World 115: Ping=31.0
    World 114: Ping=31.0
    World  35: Ping=30.0
    World  74: Ping=29.0
    World  91: Ping=29.0
    World  78: Ping=27.0
    World 100: Ping=26.0
    World  75: Ping=25.0
    World  87: Ping=25.0
    World  98: Ping=25.0
    World 140: Ping=25.0
    World  47: Ping=24.0
    World  99: Ping=23.0
    World  60: Ping=12.0
    World 116: Ping=11.0
    World  27: Ping=10.0
    World  58: Ping=10.0
    World  52: Ping=8.0
    World  64: Ping=8.0
    World  70: Ping=8.0
    World  89: Ping=8.0
    World 103: Ping=8.0
    World   6: Ping=7.0
    World   1: Ping=7.0
    World  45: Ping=7.0
    World 117: Ping=7.0
    World  22: Ping=6.0
    World  18: Ping=6.0
    World  46: Ping=6.0
    World  66: Ping=6.0
    World  62: Ping=5.0
    World  79: Ping=5.0
    World  44: Ping=4.0
    World  48: Ping=4.0
    World  77: Ping=4.0
    World  59: Ping=4.0
    World  76: Ping=4.0
    World  31: Ping=3.0
    World   2: Ping=3.0
    World   9: Ping=3.0
    World  39: Ping=3.0
    World  42: Ping=3.0
    World 104: Ping=3.0
</pre>
