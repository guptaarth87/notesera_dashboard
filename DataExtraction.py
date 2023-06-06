import pymongo
import _helpers
import pandas as pd
myclient = pymongo.MongoClient(_helpers.api_url)

mydb = myclient["Mu_study"]

papersData = mydb['PostReqPapersData']
notesData = mydb['PostReqNotesData']
notes_data = mydb['Notes']
papers_data = mydb['Papers']

notesData = notesData.find()
papersData = papersData.find()

l1=[]
for i in notesData:
  print(i)
  l1.append(i)
notes_requests_dataframe = pd.DataFrame.from_records(l1)


l1=[]
for i in papersData:
  l1.append(i)
papers_requests_dataframe = pd.DataFrame.from_records(l1)