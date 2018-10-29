"""
AutoSys JIL command line utility
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

    print('-----')
	
    if args.format == True:
        write_jil(args.path, jobs, args.reverse)
    
    if args.check == True:
        check_jil(jobs)

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

def check_jil(jobs):

    """checks JIL for jobs matching attribute"""

    jobs_matching = []
    jobs_not_matching = []
    job_names = sorted(jobs)

    print("searching for attribute '{}'".format(args.attribute))

    for job in job_names:
        if any(args.attribute in s for s in jobs[job]):
            jobs_matching.append(job)
        else:
            jobs_not_matching.append(job)   

    print("Jobs matching:")
    print("\n".join(jobs_matching))
    print("-----")
    print("Jobs not matching:")
    print("\n".join(jobs_not_matching))

if __name__ == '__main__':

    parser = ArgumentParser(description='AutoSys JIL Formatter')
    parser.add_argument('path', type=str, help='path to JIL file')

    parser.add_argument('-f', '--format', action='store_true', help='format the file')
    parser.add_argument('-b', '--backup', action='store_true', help='make a backup of the changed file')
    parser.add_argument('-r', '--reverse', action='store_true', help='sort jobs in descending order by name')

    parser.add_argument('-c', '--check', action='store_true', help='check for jobs matching attribute')
    parser.add_argument('-a', '--attribute', action='store', help='attribute to search for')

    args = parser.parse_args()
    
    try:
        main(args)
    except Exception as e:
        print(e)
