###############################################
# Natural Language Processing to SQL
#
# Author: Lakshmanan Kuppan
#################################################

import sys
import pandas as pd
import sqlite3
from palm_api import send_query_to_ai

def start_inmemory_SQLite():
    conn = sqlite3.connect(':memory:')
    return conn

def load_csv_in_sql (csv, conn, table_name):

    # Load CSV data into a pandas DataFrame
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    csv = 'kea-dhcp4.csv'
    df = pd.read_csv(csv)

    # Use pandas to write the DataFrame to a table in the SQLite database
    df.to_sql(table_name, conn, index=False)
    return df

def sql_query(df, query):
    try:
        result_df = pd.read_sql_query(query, conn)
        return result_df
    except:
        return "Incorrect SQL Query. Try again"

def set_prompt(db, table_name, nlp) :

    if nlp.lower() in ["q", "quite", "exit", "stop", "thanks", "thank you"]:
        print("\nThanks You !")
        conn.close()
        sys.exit()

    prompt = ''' ### sqlite SQL Table with its properties given below\n
    # {}({})\nn
    # User Question to answer: {}\n
    ### Respond only with SQL SELECT Query\n
    ### do not include the character ```
    '''.format(table_name, db, nlp)
    return prompt

def display_prompt(nlp, message) :

    prompt = ''' User question is {} \n
    ### Reponse from SQL DB is {} \n
    # Format the response in a way that user understands well
    '''.format(nlp, message)
    return prompt

def main():

    table_name="Kea_DHCP_Server_assigned_IP"
    data_frame = load_csv_in_sql("kea-dhcp4.csv", conn, table_name)
    all_columns = ",".join([str(col) for col in data_frame.columns])
    nlp = input("(NLP -> SQL -> NLP) How can i help you ? ")

    while True:
        prompt = set_prompt(all_columns, table_name, nlp)
        sql_query_resp = send_query_to_ai(prompt)
        response = sql_query(data_frame, sql_query_resp)
        print("\n")
        if len(response) > 10 :
            print(response)
        else:
            print(send_query_to_ai(display_prompt(nlp, response)))

        print("\n\n\u2192 SQL Query for reference: {}".format(sql_query_resp))

        nlp = input("\n(NLP -> SQL -> NLP).. any more query ?  ")

    conn.close()

if '__main__' == __name__ :
    conn = start_inmemory_SQLite()
    main()
