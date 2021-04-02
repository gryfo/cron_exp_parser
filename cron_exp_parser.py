#!/usr/bin/env python3

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
    elif ',' in od['minute']:
        ood['minute'] = od['minute'].split(',')
    elif '-' in od['minute']:
        ood['minute'] = list(range(int(od['minute'].split('-')[0]), int(od['minute'].split('-')[-1])+1))
    elif od['minute'] == '*':
        ood['minute'] = 'every minute'

    return ood


if __name__ == '__main__':
    print(cron_exp_parse('0-15 0 1,15 * 1-5 /usr/bin/find'))
