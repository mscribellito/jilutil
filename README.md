# JIL Utility
AutoSys JIL command line utility

## What is JIL?
Job Information Language (JIL) is a scripting language that lets you define and modify assets such as jobs, global variables, machines, job types, external instances, and blobs.

## Basic Usage

Basic usage for formatting a JIL file.

### Positional Arguments
- path : path to JIL source file

```python jilutil.py some_JIL_file.txt```

## Advanced Usage

Advanced usage for formatting a JIL file.

### Optional Arguments

- -e, --export : export jobs to CSV file

- -f, --format : format the JIL source file
- -n, --new : format the JIL source file as a new file
- -r, --reverse : sort jobs in descending order by name
