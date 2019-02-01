"""AutoSys JIL Utility (https://github.com/mscribellito/JIL-Utility)"""

from re import match

from .AutoSysJob import AutoSysJob

class JilParser:

    """Class that parses JIL into jobs"""

    job_comment = '/* -----------------'

    def __init__(self, path):
        """Instantiates a new instance"""

        self.path = path

    def read_jil(self):
        """Reads JIL from a file"""

        # list of trimmed & not empty lines in file
        lines = []

        with open(self.path, 'r') as f:
            for line in f:
                # remove leading & trailing whitespace
                line = line.strip()
                # check if line is empty
                if not line:
                    continue
                lines.append(line.strip())
        
        return lines

    def find_jobs(self, lines):
        """Finds jobs from lines"""

        jobs = []
        i = -1

        for line in lines:            
            # check if the line contents indicate a new job
            if line.startswith(self.job_comment):
                # find job start match
                matches = match(AutoSysJob.job_start_regex, line)
                # if match found, create new list for job lines & increment number of jobs
                if matches:
                    jobs.append([])
                    i += 1
            # is not a new job, add contents of line
            else:
                jobs[i].append(line)
        
        return jobs
    
    def parse_jobs(self):
        """Parses jobs from JIL"""

        lines = self.read_jil()
        raw_jobs = self.find_jobs(lines)
        parsed_jobs = []

        for definition in raw_jobs:
            # create new job from list of strings
            job = AutoSysJob.from_str('\n'.join(definition))
            parsed_jobs.append(job)
        
        return parsed_jobs
