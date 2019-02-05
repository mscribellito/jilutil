import unittest

from jilutil.AutoSysJob import AutoSysJob

jil_job = """/* ----------------- SAMPLE_BOX_JOB ----------------- */

insert_job: SAMPLE_BOX_JOB   job_type: BOX
alarm_if_fail: 1
date_conditions: 1
days_of_week: su,mo,tu,we,th,fr,sa
description: "Sample box job"
group: SOME_GROUP
owner: root@domain
permission: gx,ge,wx,we,mx,me
start_times: "20:00"
"""

class TestAutoSysJob(unittest.TestCase):

    maxDiff = None

    def test_from_str(self):
        job = AutoSysJob.from_str(jil_job)
        self.assertEqual(str(job), jil_job)

if __name__ == '__main__':
    unittest.main()