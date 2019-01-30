"""AutoSys JIL Utility

This script allows the user to work with (format & export) JIL files.

This tool accepts any file type (.txt, .jil, etc) for JIL source file path.

https://github.com/mscribellito/JIL-Utility
"""

from argparse import ArgumentParser
import csv
from datetime import datetime
import os
from autosys import AutoSysJob, JilParser

verbose = False

def print_v(str):
    """Verbose printer"""
    if verbose == True:
        print(str)

def export_jil(jobs, path, reversed):
    """Exports jobs to a CSV file"""

    file = '{} - {}.csv'.format(os.path.splitext(path)[0], datetime.now().strftime("%Y%m%d_%H%M%S"))
    
    jobs.sort(key=lambda x: x.job_name, reverse=reversed)

    with open(file, 'w', newline='') as csv_file:

        writer = csv.writer(csv_file, delimiter=',', quotechar='"')
        writer.writerow(AutoSysJob.default_attributes.keys())

        for job in jobs:

            data = AutoSysJob.default_attributes.copy()

            for attribute, value in job.attributes.items():
                data[attribute] = value

            writer.writerow(data.values())

    print_v("exported to '{}'".format(file))

def format_jil(jobs, path, new, reversed):
    """Formats jobs to a JIL file"""

    if new == True:
        file = '{} - {}.jil'.format(os.path.splitext(path)[0], datetime.now().strftime("%Y%m%d_%H%M%S"))
    else:
        file = path

    jobs.sort(key=lambda x: x.job_name, reverse=reversed)

    with open(file, 'w') as f:

        for job in jobs:
            f.write(str(job) + '\n')

    print_v("formatted to '{}'".format(file))

def output(jobs, reversed):
    """Outputs jobs to stdout"""

    jobs.sort(key=lambda x: x.job_name, reverse=reversed)

    for job in jobs:
	    print(job.job_name)

def main(args):

    global verbose
    verbose = args.verbose

    jil_parser = JilParser(args.path)

    jobs = jil_parser.parse_jobs()

    print_v('{} jobs parsed'.format(len(jobs)))

    if args.export:
        export_jil(jobs, args.path, args.reverse)
    
    if args.format:
        format_jil(jobs, args.path, args.new, args.reverse)
    
    if args.output:
        output(jobs, args.reverse)

if __name__ == '__main__':

    parser = ArgumentParser(description='AutoSys JIL command line utility')
    parser.add_argument('path', type=str, help='path to JIL source file')

    parser.add_argument('-e', '--export',   action='store_true',    help='Exports jobs contained in the JIL source file in ascending order by name to a CSV file.')

    parser.add_argument('-f', '--format',   action='store_true',    help='Formats jobs contained in the JIL source file in ascending order by name.')
    parser.add_argument('-n', '--new',      action='store_true',    help='Formats as new file.')

    parser.add_argument('-o', '--output',   action='store_true',    help='Outputs jobs contained in the JIL source file in ascending order by name to standard out.')

    parser.add_argument('-r', '--reverse',  action='store_true',    help='Sorts jobs in descending order by name.')

    parser.add_argument('-v', '--verbose',  action='store_true',    help='Increases output verbosity.')

    args = parser.parse_args()
    
    try:
        main(args)
    except Exception as e:
        print(e)

# EOF