# Scripts

This folder consists to the two scripts used to convert given utterances and generate a `json` in the required format.

## Directory

- `json_maker.py`
- `validator.py`
- `multi-modal-emotion-schema.json`

## Run Instructions

`python json-maker.py <directory> <short movie name> <srt file> <language> <index_start>`

## Libraries Used

1. `os` - to interact with the operating system, for tasks like changing the working directory or creating directories.
2. `sys` - to use command line arguments.
3. `csv` - to read and write CSV files.
4. `json` - to encode and decode JSON data.
5. `bisect` - to perform binary search operations.
6. `datetime` - to work with dates and times. Specifically, `timedelta` is used to convert seconds to hh:mm:ss format.
