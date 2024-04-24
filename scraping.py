
# import in packages
import pandas as pd
import numpy as np
import camelot as cl

# function that scrapes the pdf and extracts the tables
def scrapePDF(file):
    tables = cl.read_pdf(file, pages='3,4,5', flavor='stream', table_areas=['0,650,500,0'])
    return tables

# concatenate the tables together into one big dataframe
def aggregateTables(tables):
    merged_df = tables[0].df
    for i in range(1, len(tables)):
        merged_df = pd.concat([merged_df, tables[i].df], ignore_index=True)

    # update the column headers
    merged_df.columns = [
        'Country', 'Rank', 'Overall Score', 
        'Electoral Process and Pluralism', 
        'Functioning of Government',
        'Political Participation',
        'Political Culture',
        'Civil Liberties'
    ]

    # return the final version
    return merged_df

# test / debug
tables = scrapePDF('EIU_Democracy-Index_2007_v3.pdf')
merged_df = aggregateTables(tables)
print(merged_df)