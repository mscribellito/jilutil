"""AutoSys JIL Utility (https://github.com/mscribellito/JIL-Utility)"""

import csv
from datetime import datetime
import os

from .AutoSysJob import AutoSysJob
from .JilParser import JilParser

verbose = False

def print_v(str):
    """Verbose printer"""
    if verbose == True:
        print(str)

def export(jobs, path, reversed):
    """Exports jobs contained in the JIL source file in ascending order by name to a CSV file."""

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

def format(jobs, path, new, reversed):
    """Formats jobs contained in the JIL source file in ascending order by name."""

    if new == True:
        file = '{} - {}.jil'.format(os.path.splitext(path)[0], datetime.now().strftime("%Y%m%d_%H%M%S"))
    else:
        file = path

    jobs.sort(key=lambda x: x.job_name, reverse=reversed)

    with open(file, 'w') as f:

        for job in jobs:
            f.write(str(job) + '\n')

    print_v("formatted to '{}'".format(file))

def output(jobs, attributes, reversed):
    """Outputs jobs contained in the JIL source file in ascending order by name to standard out."""

    jobs.sort(key=lambda x: x.job_name, reverse=reversed)

    attributes = [attribute.strip() for attribute in attributes.split(',') if attribute.strip() != '' and attribute in AutoSysJob.default_attributes]
    
    for job in jobs:

        extra = []

        print(job.job_name, end='')

        for attribute in attributes:
            extra.append('{}: {}'.format(attribute, job.attributes[attribute]))
        
        if len(extra) > 0:
            print(' -> ', end='')
            print(' ; '.join(extra), end='')

        print('')

def main(args):

    global verbose
    verbose = args.verbose
    
    try:

        jil_parser = JilParser(args.path)
        jobs = jil_parser.parse_jobs()

        print_v('{} jobs parsed'.format(len(jobs)))

        if args.export:
            export(jobs, args.path, args.reverse)        
        elif args.format:
            format(jobs, args.path, args.new, args.reverse)        
        elif args.output:
            output(jobs, args.attributes, args.reverse)

    except Exception as e:
        print(e)
        return 1
    
    return 0
