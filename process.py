import os
import datetime

import pandas as pd

TODAY = datetime.datetime.today().date().isoformat()

# grab a list of xlsx files
xlsx_files = [os.path.join('raw', x) for x
              in os.listdir('raw') if x.endswith('xlsx')]

# get headers from first file
headers = pd.read_excel(xlsx_files[0]).columns

# create empty data frame
df = pd.DataFrame(columns=headers)

# loop over the xlsx files
for xl_file in xlsx_files:

    # create a data frame
    new_df = pd.read_excel(xl_file, columns=headers)

    # append to main data frame
    df = df.append(new_df,
                   ignore_index=True,
                   sort=True)

# add today's date in a new column
df['download_date'] = TODAY

# coerce amount column to numbers (some prizes are not money)
df['Amount Won'] = pd.to_numeric(df['Amount Won'],
                                 errors='coerce')

# filter out the nulls
not_null = df[df['Amount Won'].notnull()]

# write out to CSV
not_null.to_csv(f'{TODAY}-lotto.csv',
                encoding='utf-8',
                index=False)