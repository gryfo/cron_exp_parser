#!/usr/bin/env python3

field_ranges = {
    'minute': range(0, 60),
    'hour': range(0, 24),
    'day of month': range(1, 32),
    'month': range(1, 13),
    'day of week': range(1, 8)
}


def field_parse(field_name, field_str):
    out_value = []
    if field_name == 'command':
        return field_str

    if '/' in field_str:
        d = int(field_str.split('/')[-1])
        for i in range(field_ranges[field_name][0], int((field_ranges[field_name][-1]+1)/d)):
            out_value.append(str(i * d))
    elif ',' in field_str:
        out_value = field_str.replace(',', ' ')
    elif '-' in field_str:
        a, b = field_str.split('-')
        out_value = [str(n) for n in range(int(a), int(b)+1)]
    elif field_str == '*':
        out_value = [str(n) for n in field_ranges[field_name]]
    else:
        out_value = field_str

    return ' '.join(out_value) if isinstance(out_value, list) else out_value


def cron_exp_parse(exp):
    field_names = ['minute', 'hour', 'day of month', 'month', 'day of week', 'command']
    out_dict = {}
    parts = exp.split()
    for p in range(len(parts)):
        fn = field_names[p]
        v = field_parse(fn, parts[p])
        out_dict[fn] = v
    return out_dict


def generate_table_string(d, w):
    s = ''
    for k, v in d.items():
        s += f"{k:<{w}} {v}\n"
    return s


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('cron_expression', type=str, help='A valid cron expression to be parsed')
    args = parser.parse_args()

    print(generate_table_string(cron_exp_parse(args.cron_expression), 14))
    

if __name__ == '__main__':
    main()
