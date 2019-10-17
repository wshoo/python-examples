import pandas as pd
import csv

url = 'https://www.reebok.com/us/help-section-size_charts.html?tdsourcetag=s_pctim_aiomsg'
tb = pd.read_html(url)[1] #所需表格是网页中第4个table，故为[3]
tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
