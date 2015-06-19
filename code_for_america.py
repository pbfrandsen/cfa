import pandas as pd
from collections import OrderedDict
from bokeh.charts import Bar, output_file, show, TimeSeries
from bokeh.io import vplot

# Load csv into Pandas data frame
df = pd.DataFrame.from_csv('cfa_challenge.csv')

# Rename the fields to something more manageable
new_column_names = {'violation_id':'violation_id',
                    'inspection_id':'inspection_id',
                    'violation_category':'violation_category',
                    'violation_date':'timestamp',
                    'violation_date_closed':'date_closed',
                    'violation_type':'violation_type'
}
df.rename(columns=new_column_names, inplace=True)
df.timestamp = pd.to_datetime(df.timestamp)

# Make a list of violations
violation_cats = []

for viol in df['violation_category']:
    if viol not in violation_cats:
        violation_cats.append(viol)


df.sort('timestamp')

garb_refuse = df['violation_category'].str.count('Garbage and Refuse')

sum_violation_cats = [df['violation_category'].str.count(cat).sum()\
                     for cat in violation_cats]


# Make an ordered dictionary with violation_cats
xyviolcats = OrderedDict()
xyviolcats['violation_cateogry'] = sum_violation_cats

# Make a bar plot for workshop usefulness
bar_viol_cat = Bar(xyviolcats, violation_cats, title="Violations by category", 
    xlabel="type of violation", ylabel="number of violations", legend="top_right",
    palette=["#3399FF"])

output_file("violations_bar_plot.html")

data = dict(viol_type=garb_refuse, Date=df['timestamp'])


show(bar_viol_cat)



