def cron_exp_parse(exp):
    parts = exp.split()
    od = {}
    ood = {
        'minute': [],
        'hour': [],
        'day of month': [],
        'month': [],
        'day of week': [],
        'command': ''
    }
    od['minute'] = parts[0]
    od['hour'] = parts[1]
    od['day of month'] = parts[2]
    od['month'] = parts[3]
    od['day of week'] = parts[4]
    od['command'] = parts[5]
    
    if '/' in od['minute']:
        d = int(od['minute'].split('/')[-1])
        for i in range(int(60/d)):
            ood['minute'].append(i * d)

    return ood


if __name__ == '__main__':
    print(cron_exp_parse('*/15 0 1,15 * 1-5 /usr/bin/find'))
