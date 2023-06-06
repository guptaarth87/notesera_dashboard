import _helpers
import DataExtraction
import streamlit as st

# subject , semester , program , link
def string_to_list(string):
    # Split the string by commas
    elements = string.split(',')

    # Remove leading and trailing whitespaces from each element
    elements = [element.strip() for element in elements]

    return elements

def AddNotes(query):
       
        result_list = string_to_list(query)   
        subject = result_list[0]
        semester =result_list[1]
        program = result_list[2]
        link =  result_list[3]

        My_collection = DataExtraction.notes_data
        notes_dic = {
             'subject': subject,
             'semester': semester,
             'program': program,
             'link': link
        }
        st.write(notes_dic)
        print(notes_dic.keys)
        My_collection.insert_one(notes_dic)
        st.write("added notes successfully")

