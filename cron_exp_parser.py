#!/usr/bin/env python3

def field_parse(field_name, field_str):
    out_value = []
    if field_name == 'command':
        return field_str

    if '/' in field_str:
        d = int(field_str.split('/')[-1])
        for i in range(int(60/d)):
            out_value.append(str(i * d))
    elif ',' in field_str:
        out_value = field_str.replace(',', ' ')
    elif '-' in field_str:
        a, b = field_str.split('-')
        out_value = [str(n) for n in range(int(a), int(b)+1)]
    elif field_str == '*':
        out_value = f'every {field_name}'
    else:
        out_value = field_str

    return out_value

def cron_exp_parse(exp):
    field_names = ['minute', 'hour', 'day of month', 'month', 'day of week', 'command']
    out_dict = {}
    parts = exp.split()


    for p in parts:
        fn = field_names[parts.index(p)]
        v = field_parse(fn, p)
        out_dict[fn] = v

    return out_dict

def print_table(d, w):
    for k, v in d.items():
        print(f"{k:<{w}} {' '.join(v) if isinstance(v, list) else v}")

if __name__ == '__main__':
    print_table(cron_exp_parse('*/15 0 1,15 * 1-5 /usr/bin/find'), 14)
