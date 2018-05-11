# pingrs
Ping Runescape worlds using parallel processing

$ python pingrs.py -h
usage: pingrs.py [-h] [-p PINGS] [-b BATCHES] [-w WORKERS] [-v]
                 [-d DISTINGUISH [DISTINGUISH ...]]

Ping Runescape worlds.

optional arguments:
  -h, --help            show this help message and exit
  -p PINGS, --pings PINGS
                        number of pings for each batch (default: 1)
  -b BATCHES, --batches BATCHES
                        number of batches (default: 10)
  -w WORKERS, --workers WORKERS
                        number of worker processes to spawn (default:
                        os.cpu_count())
  -v, --verbose         print verbose output
  -d DISTINGUISH [DISTINGUISH ...], --distinguish DISTINGUISH [DISTINGUISH ...]
                        distinguish worlds in output
