# cron_exp_parser
A Python script which parses a cron string and expands each field to show the time at which it will run.

## Requirements
The script requires `Python v3.7` or newer installed on the system to run.

## Usage
You can run the script in one of two ways: 
- using the Python interpreter explicitly

```
python3 cron_exp_parser.py '*/15 0 1,15 * 1-5 /usr/bin/find'
```

- running it as a standard script (you need to set execution rights on the file `chmod +x cron_exp_parser.py`)

```
./cron_exp_parser.py '*/15 0 1,15 * 1-5 /usr/bin/find'
```

## Unit tests

The `unit_tests.py` script contains a set of simple unit tests. It uses the standard `unittest` library. To run the tests you have to use the following command:

```
python3 -m unittest unit_tests.py
```
