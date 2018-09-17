"""
AutoSys JIL formatter command line utility
Author: Michael Scribellito
"""

from argparse import ArgumentParser
from re import match
from shutil import copyfile

job_indicator_regex = '\\/\\*\\s*\\-*\\s*([a-zA-Z0-9_-]*)\\s*\\-*\\s*\\*\\/'
job_indicator_start = '/*'
job_indicator = '/* ----------------- {} ----------------- */'

backup_suffix = '.bak'

def main(args):

    if args.backup:
        copyfile(args.path, args.path + backup_suffix)

    lines = read_jil(args.path)
    print('Jobs in source: {}'.format(sum(l.startswith(job_indicator_start) for l in lines)))

    jobs = parse_jil(lines)
    print('Jobs after parsing: {}'.format(len(jobs)))

    write_jil(args.path, jobs, args.reverse)

def read_jil(path):

    """reads JIL code from file and returns list of lines"""

    lines = []

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue # skip if line is empty
            lines.append(line.strip())

    return lines

def parse_jil(lines):

    """parses JIL code from lines and returns dictionary of jobs"""

    jobs = {}

    job = None

    for line in lines:
        
        if line.startswith(job_indicator_start):
            matches = match(job_indicator_regex, line)
            if matches:
                job = matches.group(1)
                jobs.update({ job : [] })
        else:
            jobs[job].append(line)
    
    return jobs

def write_jil(path, jobs, reversed=False):

    """writes JIL code to file"""

    job_names = sorted(jobs, reverse=reversed)

    with open(path, 'w') as f:
        for job in job_names:
            f.write(job_indicator.format(job) + '\n')           
            f.write('\n')
            for code in jobs[job]:
                f.write(code + '\n')          
            f.write('\n')

if __name__ == '__main__':

    parser = ArgumentParser(description='AutoSys JIL Formatter')
    parser.add_argument('path', type=str, help='path to JIL file')
    parser.add_argument('-b', '--backup', action='store_true', help='make a backup of the changed file')
    parser.add_argument('-r', '--reverse', action='store_true', help='sort jobs in descending order by name')

    args = parser.parse_args()
    
    try:
        main(args)
    except Exception as e:
        print(e)
