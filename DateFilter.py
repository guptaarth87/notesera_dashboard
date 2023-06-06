from datetime import datetime,timedelta
import DataExtraction

def date_sliced(df, start_date , end_date):
  # Filter the dataframe based on the date range
  filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
  return filtered_df

def date_filter_data(tag):
     # Get the current date
     current_date = datetime.now().date()
     
     # Format the current date as YYYY-MM-DD
     current_date_ = current_date.strftime('%Y-%m-%d')
     input_tag = tag
     if input_tag == 'today':
       start_date = current_date_
       end_date =  (current_date + timedelta(days=1)).strftime('%Y-%m-%d')
     elif input_tag == 'past week':
        start_date =  (current_date - timedelta(days=7)).strftime('%Y-%m-%d')
        end_date = current_date_
     elif input_tag == 'past month':
          start_date =  (current_date - timedelta(days=30)).strftime('%Y-%m-%d')
          end_date = current_date_
     elif input_tag == 'last 3 months':
          start_date =  (current_date - timedelta(days=90)).strftime('%Y-%m-%d')
          end_date = current_date_
     elif input_tag == 'last 6 months':
          start_date =  (current_date - timedelta(days=180)).strftime('%Y-%m-%d')
          end_date = current_date_
     elif input_tag == 'last 12 months':
          start_date =  (current_date - timedelta(days=365)).strftime('%Y-%m-%d')
          end_date = current_date_
    
     filtered_df_notes = date_sliced(DataExtraction.notes_requests_dataframe,start_date,end_date)
     filtered_df_papers = date_sliced(DataExtraction.papers_requests_dataframe,start_date,end_date)
     
     

     return filtered_df_notes , filtered_df_papers
