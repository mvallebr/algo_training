#!/usr/bin/env python
import os
with open(os.path.join(os.path.dirname(__file__), "jobs1.txt")) as f:
    job_list = [(int(t[0]), int(t[1]))
                for t in (s.split() for s in f.readlines()[1:])]
    jobs = sorted(job_list, key=lambda x: x[0] - x[1], reverse=False)
print ("jobs = {}".format(jobs))
