# JIL Utility
AutoSys JIL command line utility

This utility provides functionality to:
* **Export to CSV** - makes jobs easier to read for non-technical people
* **Format JIL** - aids in comparison of jobs in different environments
* **Output to console** - allows quick inspection of jobs contained within

## What is JIL?
Job Information Language (JIL) is a scripting language that lets you define and modify assets such as jobs, global variables, machines, job types, external instances, and blobs.

## Basic Usage

Basic usage for working with a JIL file.

```usage: jilutil.py [-h] [-e] [-f] [-n] [-o] [-r] [-v] path```

### Positional Arguments
* path - path to JIL source file

### Optional Arguments
* -h, --help - show this help message and exit
* -e, --export - Exports jobs contained in the JIL source file in ascending order by name to a CSV file.
* -f, --format - Formats jobs contained in the JIL source file in ascending order by name.
* -n, --new - Formats as new file.
* -o, --output - Outputs jobs contained in the JIL source file in ascending order by name to standard out.
* -r, --reverse - Sorts jobs in descending order by name.
* -v, --verbose - Increases output verbosity.

## Functionality

### Export
Exports jobs contained in the JIL source file in ascending order by name to a CSV file.

Export jobs contained in JIL file:
```python jilutil.py -e sample.jil```

### Format
Formats jobs contained in the JIL source file in ascending order by name.

Format JIL file in place:
```python jilutil.py -f sample.jil```

Format JIL file as new file:
```python jilutil.py -f -n sample.jil```

### Output
Outputs jobs contained in the JIL source file in ascending order by name to standard out.

Output jobs contained in JIL file:
```python jilutil.py -o sample.jil```
