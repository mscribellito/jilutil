# JIL Utility
AutoSys JIL command line utility

## What is JIL?
Job Information Language (JIL) is a scripting language that lets you define and modify assets such as jobs, global variables, machines, job types, external instances, and blobs.

## Basic Usage

Basic usage for working with a JIL file.

```usage: jilutil.py [-h] [-e] [-f] [-n] [-i] [-r] path```

### Positional Arguments
- path - path to JIL source file

### Optional Arguments
- -h, --help - show this help message and exit
- -e, --export - export jobs to CSV file
- -f, --format - format the JIL source file
- -n, --new - format the JIL source file as a new file
- -i, --info - show job info
- -r, --reverse - sort jobs in descending order by name

## Functionality

### Export
Exports jobs contained in the JIL source file in ascending order by name to a CSV file.

### Format
Formats jobs contained in the JIL source file in ascending order by name, optionally as a new file.
