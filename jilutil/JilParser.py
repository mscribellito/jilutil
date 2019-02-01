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

        lines = []

        with open(self.path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue # skip if line is empty
                lines.append(line.strip())
        
        return lines

    def find_jobs(self, lines):
        """Finds jobs from lines"""

        jobs = []
        i = -1

        for line in lines:
            
            if line.startswith(self.job_comment):
                matches = match(AutoSysJob.job_start_regex, line)
                if matches:
                    jobs.append([])
                    i += 1
            else:
                jobs[i].append(line)
        
        return jobs
    
    def parse_jobs(self):
        """Parses jobs from JIL"""

        lines = self.read_jil()
        raw_jobs = self.find_jobs(lines)
        parsed_jobs = []

        for definition in raw_jobs:
            job = AutoSysJob.from_str('\n'.join(definition))
            parsed_jobs.append(job)
        
        return parsed_jobs
