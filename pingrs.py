import re, subprocess, time

def ping(args):
    world = args['world']
    results = args['results']
    numPings = args['numPings']
    verbosity = args['verbosity']
    if verbosity is 2:
        print('Begin ping for World {}'.format(world))
    try:
        pings = []
        for i in range(numPings):
            cmd = "ping -n 1 world{}.runescape.com".format(world)
            response = str(subprocess.check_output(cmd, shell=False))
            parsed = re.search('Minimum = (\d+)ms', response)
            pingTime = parsed.group(1)
            pings.append(int(pingTime))
        minTime = min(pings)
        maxTime = max(pings)
        fullResult = pings
        avgTime = float(sum(pings))/len(pings)
    except subprocess.CalledProcessError as e:
        fullResult = handleNonZeroExit(e)
        minTime = maxTime = avgTime = -1
    finally:
        results.append({
            'world': world,
            'fullResult': fullResult,
            'minTime': minTime,
            'maxTime': maxTime,
            'avgTime': avgTime
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
    # 93 members
    memberWorlds = [1,2,4,5,6,9,10,12,14,16,18,21,22,23,24,25,26,27,28,30,31,32,35,36,37,39,40,42,44,45,46,47,48,51,52,53,54,56,58,59,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,82,83,84,85,86,87,88,89,91,92,96,97,98,99,100,102,103,104,105,106,114,115,116,117,118,119,121,123,124,134,137,138,139,140]
    # 25 non-members
    nonMemberWorlds = [3,7,8,11,17,19,20,29,33,34,38,41,43,55,57,61,80,81,94,101,120,122,135,136,141]
    
    parser = argparse.ArgumentParser(description='Ping Runescape worlds.')
    parser.add_argument('-p', '--pings', type=int, default=1,
                       help='number of pings for each batch (default: 1)')
    parser.add_argument('-w', '--workers', type=int, default=None,
                       help='number of worker processes to spawn (default: os.cpu_count())')
    parser.add_argument('-v', '--verbosity', type=int, default=0,
                       help='set verbosity level')
    parser.add_argument('-d', '--distinguish', type=int, action='append', default=[],
                       help='distinguish worlds in output')
    parser.add_argument('worlds', type=int, nargs='*', default=memberWorlds,
                       help='worlds to ping')
    parser.add_argument('--all-worlds', action="store_true",
                       help='ping all worlds (include non-members)')
    args = parser.parse_args()
    
    if args.all_worlds is True:
        worlds = memberWorlds + nonMemberWorlds
    else:
        worlds = args.worlds
    distinguishedWorlds = args.distinguish
    numPings = args.pings
    numWorkers = args.workers
    verbosity = args.verbosity

    manager = Manager()
    p = Pool(numWorkers)
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
            rowBuilder += 'Ping=' + (str(item['minTime'])).rjust(3)
        else:
            rowBuilder += 'Min=' + (str(item['minTime'])).rjust(3) + ', '
            rowBuilder += 'Max=' + (str(item['maxTime'])).rjust(3) + ', '
            rowBuilder += 'Avg=' + ('{:.2f}'.format(item['avgTime'])).rjust(3)
            if verbosity >= 1:
                rowBuilder += ', All=' + (str(item['fullResult'])).rjust(3)
        if item['avgTime'] is -1:
            rowBuilder += ', Error=' + (str(item['fullResult'])).rjust(3)
        if j < len(sortedresults) - 1:
            rowBuilder += '\n'
        resultTable += rowBuilder
    print(resultTable)
    if verbosity >= 1:
        totalTime = time.time() - start;
        print()
        print('----\n')
        print('Total time: {:.3f}s'.format(totalTime))
