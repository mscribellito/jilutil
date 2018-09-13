# JIL Formatter
AutoSys JIL formatter command line utility

## What is JIL?
Job Information Language (JIL) is a scripting language that lets you define and modify assets such as jobs, global variables, machines, job types, external instances, and blobs.

## Basic Usage

Basic usage for formatting a JIL file.

### Positional Arguments
- path : path to JIL file

```python jil_formatter.py some_JIL_file.txt```

## Advanced Usage

Advanced usage for formatting a JIL file.

### Optional Arguments

- -b, --backup : make a backup of the changed file
- -r, --reverse : sort jobs in descending order by name

```python jil_formatter.py some_JIL_file.txt -b -r```
