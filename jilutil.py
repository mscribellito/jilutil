from argparse import ArgumentParser
import csv
from datetime import datetime
import os
from autosys import AutoSysJob, JilParser

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

    print("exported to '{}'".format(file))

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

    print("formatted to '{}'".format(file))

def main(args):

    jil_parser = JilParser(args.path)

    jobs = jil_parser.parse_jobs()

    print('{} jobs parsed'.format(len(jobs)))

    if args.export:
        export_jil(jobs, args.path, args.reverse)
    
    if args.format:
        format_jil(jobs, args.path, args.new, args.reverse)

if __name__ == '__main__':

    parser = ArgumentParser(description='AutoSys JIL Utility')
    parser.add_argument('path', type=str, help='path to JIL source file')

    parser.add_argument('-e', '--export', action='store_true', help='export jobs to CSV file')

    parser.add_argument('-f', '--format', action='store_true', help='format the JIL source file')
    parser.add_argument('-n', '--new', action='store_true', help='format the JIL source file as a new file')

    parser.add_argument('-r', '--reverse', action='store_true', help='sort jobs in descending order by name')

    args = parser.parse_args()
    
    try:
        main(args)
    except Exception as e:
        print(e)

# EOF