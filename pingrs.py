import re, subprocess, time

# TODO
# world metadata (members/non at the very least)

def ping(args):
    world = args['world']
    times = args['times']
    numPings = args['numPings']
    verbose = args['verbose']
    if verbose:
        print('Begin ping for World {}'.format(world))
    try:
        response = str(subprocess.check_output("ping -n {} world{}.runescape.com".format(numPings, world), shell=False))
        parsed = re.search('Minimum = (\d+)ms, Maximum = (\d+)ms, Average = (\d+)ms', response)
        fullResult = parsed.group(0)
        minTime = parsed.group(1)
        maxTime = parsed.group(2)
        avgTime = parsed.group(3)
    except subprocess.CalledProcessError as e:
        fullResult = handleNonZeroExit(e)
        minTime = maxTime = avgTime = -1
    finally:
        times.append({
            'world': world,
            'fullResult': fullResult,
            'minTime': int(minTime),
            'maxTime': int(maxTime),
            'avgTime': int(avgTime)
        })
    if verbose:
        print('World {} Average: {}ms'.format(world, avgTime))

def handleNonZeroExit(e):
    output = str(e.output)
    loss = re.search('\d+% loss', output)
    if loss is not None:
        msg = loss.group(0)
    else:
        noHost = re.search('could not find host', output)
        if noHost is not None:
            msg = "no host"
        else:
            msg = "unknown error: " + output
    return msg
    
if __name__ == '__main__':
    from multiprocessing import Pool, Lock, Manager
    from operator import itemgetter
    import argparse
    
    parser = argparse.ArgumentParser(description='Ping Runescape worlds.')
    parser.add_argument('-p', '--pings', type=int, default=1,
                       help='number of pings for each batch (default: 1)')
    parser.add_argument('-b', '--batches', type=int, default=10,
                       help='number of batches (default: 10)')
    parser.add_argument('-w', '--workers', type=int, default=None,
                       help='number of worker processes to spawn (default: os.cpu_count())')
    parser.add_argument('-v', '--verbose', action="store_true",
                       help='print verbose output')
    parser.add_argument('-d', '--distinguish', type=str, nargs='+',
                       help='distinguish worlds in output')
    args = parser.parse_args()
    # 108 worlds listed here
    worlds = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","51","52","53","54","55","56","57","58","59","60","61","62","65","66","67","68","69","70","73","74","75","76","77","78","81","82","83","84","85","86","94","96","97","98","99","100","101","102","103","104","105","106","111","114","115","116","117","118","119","120","121","122","123","124","134","135","136","137","138","139","140"]
    distinguishedWorlds = args.distinguish
    numPings = args.pings
    batches = args.batches
    numWorkers = args.workers
    verbose = args.verbose

    manager = Manager()
    p = Pool(numWorkers)
    for i in range(batches):
        start = time.time()
        times = manager.list()
        # https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
        # KeyboardInterrupt is finnicky... if all else fails:
        # taskkill /F /IM python.exe
        # kills all python processes
        p.map_async(ping, [{'times': times, 'world': world, 'numPings': numPings, 'verbose': verbose} for world in worlds]).get(999999)
        sortedTimes = sorted(times, key=itemgetter('avgTime'), reverse=True)
        resultTable = ''
        for item in sortedTimes:
            rowBuilder = ''
            if item['world'] in distinguishedWorlds:
                rowBuilder += '--->'
            else:
                rowBuilder += '    '
            rowBuilder += 'World ' + item['world'].rjust(3) + ': '
            if numPings is 1:
                rowBuilder += 'Ping=' + (str(item['avgTime'])).rjust(3)
            else:
                rowBuilder += 'Min=' + (str(item['minTime'])).rjust(3) + ', '
                rowBuilder += 'Max=' + (str(item['maxTime'])).rjust(3) + ', '
                rowBuilder += 'Avg=' + (str(item['avgTime'])).rjust(3)
            if item['avgTime'] is -1:
                rowBuilder += ', Error=' + (str(item['fullResult'])).rjust(3)
            resultTable += rowBuilder + '\n'
        print(resultTable)
        print('{}/{} batches'.format(i+1, batches))
        print('{:.3f}s'.format(time.time() - start))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        