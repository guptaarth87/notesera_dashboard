import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st 
import DataExtraction
import DateFilter
import FrequencyCounter
import AddNotes

def main():
  st.title("Deploying our data model")
  st.subheader("Notes data")
  notesDataFrame = DataExtraction.notes_requests_dataframe
  st.dataframe(notesDataFrame)
  st.subheader('Papers data')
  papersDataFrame= DataExtraction.papers_requests_dataframe
  st.dataframe(papersDataFrame)

  st.subheader('project Analytics using date range')
  
  input_tag = st.selectbox(
     'Select your time span from here',
     ('today', 'past week', 'past month','last 3 months','last 6 months','last 12 months'))

  st.write('You selected:', input_tag)
  notes_df, papers_df =DateFilter.date_filter_data(input_tag)
  if st.button("apply for papers"):
     st.write("papers section")
     st.dataframe(papers_df[0:5])
     x_axis1 , y_axis1 = FrequencyCounter.semester_frequency_filter(papers_df)
     #creatin a button
     display_graph(x_axis1 , y_axis1,input_tag,"semesters")
     x_axis2 , y_axis2 = FrequencyCounter.subject_frequency_filter(papers_df)
     display_graph(x_axis2 , y_axis2,input_tag,"subject")
 
  if st.button("apply for notes"):
     st.write("notes section")
     st.dataframe(notes_df[0:5])
     print(notes_df)
     x_axis3 , y_axis3 = FrequencyCounter.semester_frequency_filter(notes_df)
     display_graph(x_axis3 , y_axis3,input_tag,"semester")

     x_axis4 , y_axis4 = FrequencyCounter.subject_frequency_filter(notes_df)
     display_graph(x_axis4 , y_axis4,input_tag,"subject")

  # if st.button("apply1"):
  #      display_graph(x_axis , y_axis,input_tag)
  
  #data adding function
  if(st.button('Add Notes')):
     query = st.text_input("Enter subject,semester,program,link in same order without leaving spaces :")
     
     if(st.button('submit data')):
           st.write("updating data")
         #   AddNotes.AddNotes(query)

def display_graph(x_axis , y_axis,input_tag,item):
  st.subheader("Data for {}".format(input_tag))
  # st.write(temp_df)
  print(item,":")
  print(x_axis)
  print(y_axis)
  plt.bar(x_axis , y_axis )
  plt.xlabel(item)
  plt.ylabel('Frequency')
  fig = plt.gcf()
  fig.set_size_inches(15, 5.5)
  st.pyplot(fig)



if __name__=='__main__':
    main()