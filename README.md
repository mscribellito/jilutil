# JIL Utility
AutoSys JIL command line utility

## What is JIL?
Job Information Language (JIL) is a scripting language that lets you define and modify assets such as jobs, global variables, machines, job types, external instances, and blobs.

## Basic Usage

Basic usage for working with a JIL file.

### Positional Arguments
- path (required) : path to JIL source file

```python jilutil.py some_JIL_file.txt```

## Advanced Usage

Advanced usage for working with a JIL file.

### Optional Arguments

#### Export
- -e, --export : export jobs to CSV file

#### Format
- -f, --format : format the JIL source file
- -n, --new : format the JIL source file as a new file

#### Shared
- -r, --reverse : sort jobs in descending order by name
