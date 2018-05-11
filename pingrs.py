import re, subprocess, time

# TODO
# world metadata (members/non at the very least)

def ping(args):
    world = args['world']
    results = args['results']
    numPings = args['numPings']
    verbosity = args['verbosity']
    if verbosity is 2:
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
        results.append({
            'world': world,
            'fullResult': fullResult,
            'minTime': int(minTime),
            'maxTime': int(maxTime),
            'avgTime': int(avgTime)
        })
    if verbosity is 2:
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
    # 108 worlds listed here
    allWorlds = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,52,53,54,55,56,57,58,59,60,61,62,65,66,67,68,69,70,73,74,75,76,77,78,81,82,83,84,85,86,94,96,97,98,99,100,101,102,103,104,105,106,111,114,115,116,117,118,119,120,121,122,123,124,134,135,136,137,138,139,140]
    
    parser = argparse.ArgumentParser(description='Ping Runescape worlds.')
    parser.add_argument('-p', '--pings', type=int, default=1,
                       help='number of pings for each batch (default: 1)')
    parser.add_argument('-b', '--batches', type=int, default=4,
                       help='number of batches (default: 4)')
    parser.add_argument('-w', '--workers', type=int, default=None,
                       help='number of worker processes to spawn (default: os.cpu_count())')
    parser.add_argument('-v', '--verbosity', type=int, default=0,
                       help='set verbosity level')
    parser.add_argument('-d', '--distinguish', type=str, nargs='+', default=[],
                       help='distinguish worlds in output')
    parser.add_argument('worlds', type=int, nargs='*', default=allWorlds,
                       help='worlds to ping')
    args = parser.parse_args()
    
    worlds = args.worlds
    distinguishedWorlds = args.distinguish
    numPings = args.pings
    batches = args.batches
    numWorkers = args.workers
    verbosity = args.verbosity

    manager = Manager()
    p = Pool(numWorkers)
    totalTime = 0
    for i in range(batches):
        start = time.time()
        results = manager.list()
        # https://stackoverflow.com/questions/1408356/keyboard-interrupts-with-pythons-multiprocessing-pool
        # KeyboardInterrupt is finnicky... if all else fails:
        # taskkill /F /IM python.exe
        # kills all python processes on Windows
        p.map_async(ping, [{'results': results, 'world': world, 'numPings': numPings, 'verbosity': verbosity} for world in worlds]).get(999999)
        sortedresults = sorted(results, key=itemgetter('avgTime'), reverse=True)
        resultTable = ''
        for j, item in enumerate(sortedresults):
            rowBuilder = ''
            if item['world'] in distinguishedWorlds:
                rowBuilder += '--->'
            else:
                rowBuilder += '    '
            rowBuilder += 'World ' + (str(item['world'])).rjust(3) + ': '
            if numPings is 1:
                rowBuilder += 'Ping=' + (str(item['avgTime'])).rjust(3)
            else:
                rowBuilder += 'Min=' + (str(item['minTime'])).rjust(3) + ', '
                rowBuilder += 'Max=' + (str(item['maxTime'])).rjust(3) + ', '
                rowBuilder += 'Avg=' + (str(item['avgTime'])).rjust(3)
            if item['avgTime'] is -1:
                rowBuilder += ', Error=' + (str(item['fullResult'])).rjust(3)
            if j < len(sortedresults) - 1:
                rowBuilder += '\n'
            resultTable += rowBuilder
        print(resultTable)
        if verbosity >= 1:
            if batches > 1:
                print('{}/{} batches'.format(i+1, batches))
            batchTime = time.time() - start;
            if batches > 1:
                print('{:.3f}s'.format(batchTime))
            totalTime += batchTime
        print()
    if verbosity >= 1:
        print('----\n')
        print('Total time: {:.3f}s'.format(totalTime))
