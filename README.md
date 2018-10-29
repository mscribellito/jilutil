# JIL Utility
AutoSys JIL command line utility

## What is JIL?
Job Information Language (JIL) is a scripting language that lets you define and modify assets such as jobs, global variables, machines, job types, external instances, and blobs.

## Basic Usage

Basic usage for formatting a JIL file.

### Positional Arguments
- path : path to JIL file

```python jilutil.py -f some_JIL_file.txt```

## Advanced Usage

Advanced usage for formatting a JIL file.

### Optional Arguments

- -f, --format : format the file
- -b, --backup : make a backup of the changed file
- -r, --reverse : sort jobs in descending order by name

- -c, --check : check for jobs matching attribute
- -a, --attribute : attribute to search for
