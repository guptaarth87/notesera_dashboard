def subject_frequency_filter(date_filtered_dataframe):
     list_of_subject_frequency = []
     subjects_available = date_filtered_dataframe['subject'].unique()
     for subj in subjects_available:
        freq = len(date_filtered_dataframe[(date_filtered_dataframe["subject"]==subj) ])
        obj = {
           'subject':subj,
           'frequency':freq
        }
        list_of_subject_frequency.append(obj)
     list_of_subject_frequency = sorted(list_of_subject_frequency, key=lambda x: x['frequency'], reverse=True)
     print(list_of_subject_frequency)
     top_list_of_subject_frequency = list_of_subject_frequency[0:10]
     frequency = []
     subject = []
     for dicx in top_list_of_subject_frequency:
       # print()
          frequency.append(dicx['frequency'])
          subject.append(dicx['subject'])
    
     print(frequency)
     print(subject)
     return subject , frequency

def semester_frequency_filter(date_filtered_dataframe):
     list_of_semester_frequency = []
     semesters_available = date_filtered_dataframe['semester'].unique()
     for sem in semesters_available:
        freq = len(date_filtered_dataframe[(date_filtered_dataframe["semester"]==sem) ])
        obj = {
           'semester':sem,
           'frequency':freq
        }
        list_of_semester_frequency.append(obj)
     list_of_semester_frequency = sorted(list_of_semester_frequency, key=lambda x: x['frequency'], reverse=True)
     print(list_of_semester_frequency)
     top_list_of_semester_frequency = list_of_semester_frequency[0:10]
     frequency = []
     semester = []
     for dicx in top_list_of_semester_frequency:
       # print()
          frequency.append(dicx['frequency'])
          semester.append(dicx['semester'])
     
     print("freq",frequency)
     print("sem",semester)
     return semester , frequency