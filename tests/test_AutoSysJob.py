import unittest

from jilutil.AutoSysJob import AutoSysJob

jil_box_job = """/* ----------------- SAMPLE_BOX_JOB ----------------- */

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

        job = AutoSysJob.from_str(jil_box_job)

        self.assertIsInstance(job, AutoSysJob)

        self.assertEqual(job.attributes['insert_job'], 'SAMPLE_BOX_JOB')
        self.assertEqual(job.attributes['job_type'], 'BOX')
        self.assertEqual(job.attributes['alarm_if_fail'], '1')
        self.assertEqual(job.attributes['date_conditions'], '1')
        self.assertEqual(job.attributes['days_of_week'], 'su,mo,tu,we,th,fr,sa')
        self.assertEqual(job.attributes['description'], '"Sample box job"')
        self.assertEqual(job.attributes['group'], 'SOME_GROUP')
        self.assertEqual(job.attributes['owner'], 'root@domain')
        self.assertEqual(job.attributes['permission'], 'gx,ge,wx,we,mx,me')
        self.assertEqual(job.attributes['start_times'], '"20:00"')
    
    def test_to_str(self):

        job = AutoSysJob('SAMPLE_BOX_JOB')
        job.attributes['job_type'] = 'BOX'
        job.attributes['alarm_if_fail'] = '1'
        job.attributes['date_conditions'] = '1'
        job.attributes['days_of_week'] = 'su,mo,tu,we,th,fr,sa'
        job.attributes['description'] = '"Sample box job"'
        job.attributes['group'] = 'SOME_GROUP'
        job.attributes['owner'] = 'root@domain'
        job.attributes['permission'] = 'gx,ge,wx,we,mx,me'
        job.attributes['start_times'] = '"20:00"'

        self.assertEqual(str(job), jil_box_job)

if __name__ == '__main__':
    unittest.main()