# pingrs
Ping Runescape worlds using parallel processing.

Tested with Python 3.5.0.

<pre>
$ python pingrs.py -h
usage: pingrs.py [-h] [-p PINGS] [-b BATCHES] [-w WORKERS] [-v]
                 [-d DISTINGUISH [DISTINGUISH ...]]
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
  -v, --verbose         print verbose output
  -d DISTINGUISH [DISTINGUISH ...], --distinguish DISTINGUISH [DISTINGUISH ...]
                        distinguish worlds in output
</pre>

Example usage:
<pre>
$ python pingrs.py 104 -b 3 -p 2
    World 104: Min=  8, Max= 12, Avg= 10
1/3 batches
1.145s

    World 104: Min=  5, Max=  7, Avg=  6
2/3 batches
1.028s

    World 104: Min=  4, Max=  6, Avg=  5
3/3 batches
1.027s

----

Total time: 3.200s
</pre>

Ping values are in milliseconds.

All arguments are optional. By default, it will ping all worlds four times:

<pre>
$ python pingrs.py
    World  12: Ping=213
    World 134: Ping=114
    World 139: Ping=108
    World 137: Ping=104
    World 102: Ping= 98
    World  17: Ping= 97
    World  69: Ping= 96
    World 106: Ping= 96
    World  21: Ping= 95
    World   5: Ping= 94
    World  26: Ping= 93
    World 105: Ping= 93
    World  28: Ping= 92
    World  10: Ping= 92
    World  54: Ping= 92
    World 119: Ping= 92
    World 123: Ping= 92
    World  19: Ping= 91
    World  32: Ping= 91
    World  81: Ping= 88
    World 121: Ping= 88
    World 138: Ping= 84
    World 111: Ping= 84
    World  24: Ping= 83
    World 120: Ping= 83
    World 136: Ping= 83
    World 124: Ping= 82
    World 122: Ping= 82
    World  11: Ping= 81
    World  16: Ping= 81
    World  68: Ping= 81
    World  36: Ping= 80
    World 118: Ping= 80
    World  23: Ping= 79
    World  67: Ping= 79
    World  25: Ping= 78
    World  65: Ping= 78
    World  53: Ping= 78
    World  83: Ping= 78
    World  84: Ping= 77
    World  82: Ping= 76
    World 135: Ping= 76
    World   8: Ping= 75
    World  56: Ping= 75
    World   3: Ping= 74
    World  96: Ping= 73
    World  73: Ping= 72
    World  55: Ping= 71
    World  37: Ping= 70
    World  57: Ping= 70
    World  40: Ping= 68
    World  30: Ping= 67
    World  41: Ping= 67
    World  86: Ping= 67
    World  13: Ping= 66
    World  14: Ping= 66
    World  85: Ping= 65
    World  43: Ping= 64
    World  38: Ping= 64
    World   4: Ping= 63
    World  20: Ping= 63
    World  51: Ping= 63
    World 140: Ping= 35
    World  98: Ping= 33
    World  34: Ping= 32
    World  75: Ping= 32
    World  74: Ping= 31
    World  99: Ping= 31
    World  94: Ping= 31
    World  97: Ping= 31
    World  47: Ping= 30
    World 100: Ping= 28
    World 101: Ping= 28
    World  35: Ping= 27
    World  78: Ping= 27
    World 114: Ping= 27
    World 115: Ping= 27
    World  52: Ping= 24
    World  66: Ping= 18
    World  76: Ping= 12
    World  60: Ping= 11
    World  70: Ping= 11
    World  42: Ping= 10
    World  22: Ping=  9
    World   6: Ping=  9
    World  27: Ping=  9
    World   1: Ping=  9
    World  33: Ping=  9
    World  59: Ping=  9
    World  45: Ping=  8
    World  48: Ping=  8
    World 117: Ping=  8
    World   7: Ping=  7
    World   2: Ping=  7
    World  18: Ping=  7
    World  31: Ping=  7
    World  61: Ping=  7
    World  77: Ping=  7
    World  58: Ping=  7
    World 103: Ping=  7
    World  62: Ping=  6
    World 104: Ping=  6
    World  29: Ping=  5
    World  39: Ping=  5
    World   9: Ping=  4
    World  44: Ping=  4
    World 116: Ping=  4
    World  46: Ping=  3

1/4 batches
1.640s
...
</pre>