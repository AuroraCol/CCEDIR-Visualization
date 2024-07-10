import pandas as pd
import datetime
import plotly.express as px
import csvtest as data

df = pd.DataFrame(dict({
    'beginTime': data.starttime,
    'endTime': data.endtime,
    'Observation': data.dateindex,
    'activity': data.obvCodeCSV,
    'label': data.descCSV,
    'elapsedtime': data.elapsedtime,
    'focusMode':data.instoStCSV
}
))
fig = px.timeline(df, x_start="beginTime", x_end="endTime", y="Observation", color='label')
fig2 = px.pie(df, values='elapsedtime', names='label', title='Time in Each Activity')
fig3 = px.pie(df, values='elapsedtime', names='focusMode', title='Time of Instructor vs Student Focus')
fig.show()
fig2.show()
fig3.show()