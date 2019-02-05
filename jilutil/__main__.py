"""AutoSys JIL Utility (https://github.com/mscribellito/JIL-Utility)"""

from argparse import ArgumentParser
from sys import exit

from jilutil.jilutil import main
from jilutil.__init__ import __version__

if __name__ == '__main__':

    parser = ArgumentParser(prog='jilutil', description='AutoSys JIL command line utility')

    parser.add_argument('path', type=str, help='path to JIL source file')

    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('-e', '--export', action='store_true', help='Exports jobs contained in the JIL source file in ascending order by name to a CSV file.')
    actions.add_argument('-f', '--format', action='store_true', help='Formats jobs contained in the JIL source file in ascending order by name.')
    actions.add_argument('-o', '--output', action='store_true', help='Outputs jobs contained in the JIL source file in ascending order by name to standard out.')

    parser.add_argument('-a', '--attributes', action='store', help='Attributes to list when outputting jobs (ex: job_type,box_name).')
    parser.add_argument('-n', '--new', action='store_true', help='Formats as new file.')
    parser.add_argument('-r', '--reverse', action='store_true', help='Sorts jobs in descending order by name.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increases output verbosity.')

    parser.add_argument('--version', action='version', version=__version__)
    
    exit(main(parser.parse_args()))
