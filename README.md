# pingrs
Ping Runescape worlds using parallel processing.

Tested with Python 3.5.0.

<pre>
$ python pingrs.py -h
usage: pingrs.py [-h] [-p PINGS] [-b BATCHES] [-w WORKERS] [-v VERBOSITY]
                 [-d DISTINGUISH [DISTINGUISH ...]] [--all-worlds]
                 [worlds [worlds ...]]

Ping Runescape worlds.

positional arguments:
  worlds                worlds to ping

optional arguments:
  -h, --help            show this help message and exit
  -p PINGS, --pings PINGS
                        number of pings for each batch (default: 1)
  -b BATCHES, --batches BATCHES
                        number of batches (default: 4)
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
$ python pingrs.py 104 -b 3 -p 2
    World 104: Min= 26, Max= 36, Avg= 31

    World 104: Min= 19, Max= 20, Avg= 19

    World 104: Min=  6, Max=  9, Avg=  7
</pre>

Ping values are in milliseconds.

All arguments are optional. By default, it will ping all members worlds four times:

<pre>
$ python pingrs.py
    World  12: Ping=219
    World  54: Ping= 96
    World 119: Ping= 96
    World 106: Ping= 96
    World  21: Ping= 94
    World 105: Ping= 93
    World  26: Ping= 92
    World  10: Ping= 92
    World   5: Ping= 92
    World  28: Ping= 92
    World  69: Ping= 91
    World 102: Ping= 90
    World 137: Ping= 90
    World 123: Ping= 89
    World  32: Ping= 88
    World  23: Ping= 87
    World 124: Ping= 85
    World  68: Ping= 84
    World  84: Ping= 84
    World  24: Ping= 83
    World  67: Ping= 83
    World 134: Ping= 83
    World  63: Ping= 82
    World  56: Ping= 82
    World 121: Ping= 82
    World  88: Ping= 81
    World 118: Ping= 81
    World  53: Ping= 80
    World  71: Ping= 80
    World 138: Ping= 80
    World  92: Ping= 79
    World  16: Ping= 78
    World 139: Ping= 78
    World  25: Ping= 77
    World  36: Ping= 76
    World  83: Ping= 76
    World  82: Ping= 75
    World  85: Ping= 71
    World  37: Ping= 70
    World  30: Ping= 70
    World  72: Ping= 69
    World  65: Ping= 67
    World  86: Ping= 67
    World  14: Ping= 66
    World   4: Ping= 66
    World  40: Ping= 66
    World  73: Ping= 66
    World  51: Ping= 65
    World  96: Ping= 65
    World  35: Ping= 35
    World  91: Ping= 33
    World  78: Ping= 32
    World 114: Ping= 32
    World  99: Ping= 31
    World  74: Ping= 30
    World 100: Ping= 30
    World  75: Ping= 28
    World  87: Ping= 28
    World  97: Ping= 27
    World 140: Ping= 27
    World 115: Ping= 26
    World  98: Ping= 26
    World  47: Ping= 25
    World  64: Ping= 15
    World  27: Ping= 11
    World  39: Ping= 11
    World 104: Ping= 11
    World  48: Ping= 10
    World  70: Ping= 10
    World 103: Ping= 10
    World  76: Ping=  9
    World 117: Ping=  9
    World  45: Ping=  8
    World  46: Ping=  8
    World   1: Ping=  7
    World   6: Ping=  6
    World  22: Ping=  6
    World  62: Ping=  6
    World  52: Ping=  6
    World  42: Ping=  6
    World  58: Ping=  6
    World 116: Ping=  6
    World  31: Ping=  5
    World  66: Ping=  5
    World  59: Ping=  5
    World  60: Ping=  4
    World   9: Ping=  3
    World   2: Ping=  3
    World  18: Ping=  3
    World  44: Ping=  3
    World  77: Ping=  3
    World  79: Ping=  3
    World  89: Ping=  3

...
</pre>