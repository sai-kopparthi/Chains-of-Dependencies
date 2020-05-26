import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import json
import pickle

###################################
# EDIT THESE CONSTANTS
###################################

GROUP = "ecs260-31"
DB_PASSWORD = "phrasing-litany-guttural-invest"
ANALYZER_NAME = "ecs260-31/hw3_4"
ANALYZER_VERSION = "0.0.1"
CORPUS_NAME = "r2c-1000"

###################################
# END EDIT SECTION
###################################

# Canonical SQL query to get job-specific results back.
JOB_QUERY = """
SELECT commit_corpus.repo_url,result.extra
FROM   result, 
       commit_corpus 
WHERE  result.commit_hash = commit_corpus.commit_hash 
       AND analyzer_name = %(analyzer_name)s 
       AND analyzer_version = %(analyzer_version)s
       AND corpus_name = %(corpus_name)s
"""

QUERY_PARAMS = {
    "corpus_name": CORPUS_NAME,
    "analyzer_name": ANALYZER_NAME,
    "analyzer_version": ANALYZER_VERSION
}

# Connect to PostgreSQL host and query for job-specific results
engine = create_engine(f'postgresql://notebook_user:{DB_PASSWORD}@{GROUP}-db.massive.ret2.co/postgres')
job_df = pd.read_sql(JOB_QUERY, engine, params=QUERY_PARAMS)

a={}
for i in range(job_df.size):
	try:
		a[job_df.repo_url[i]]=job_df.extra[i]['result']
	except:
		continue	

with open('result2.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)


