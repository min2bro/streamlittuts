import streamlit as st
import pandas as pd
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
fig = go.Figure()

csv_file_state = 'usa_covid_data_states.csv'
csv_file_total_cases = 'usa_total_cases.csv'

@st.cache
def load_data(file):
    # Read CSV Data
    df= pd.read_csv(file,parse_dates=['Date'])
    return df

# Upload total case files
dfstate = pd.read_csv(csv_file_state) 
df = load_data(csv_file_total_cases)	

# Dashboard Sidebar with State list
st.sidebar.title("State-Wise Data")
State_list = st.sidebar.selectbox(
    'state',
     dfstate.State[:8])

st.sidebar.markdown(

        """
    **Please note**:

    All line plots are interactive, you can zoom with scrolling and hover on data points for additional information.
    """

)

# Dashboard Title and paragraphs
st.title("Covid19 USA Data from Wikipedia")
st.markdown(

            """
        This app is for visualizing the Covid19 data for USA which is collected from the wikipedia site https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States.
         User can select the Metrics Type from the drop-down list to see the trend in last 15 days



        """

    )

# Dropdown for Trends
st.markdown("## " + 'TotalCases/Deaths/Recoveries Trend')	
st.markdown("#### " +"What Trends would you like to see?")

selected_metrics = st.selectbox(
    label="Choose...", options=['TotalCases','Deaths','Recoveries']
)


# Create Trends Graph
fig = go.Figure()
if selected_metrics == 'TotalCases':
	fig.add_trace(go.Scatter(x=df.Date, y=df.TotalCases,
                    mode='lines',
                    name='TotalCases'))
if selected_metrics == 'Deaths':
	fig.add_trace(go.Scatter(x=df.Date, y=df.Deaths,
	                    mode='markers', name='Deaths'))
if selected_metrics == 'Recoveries':
	fig.add_trace(go.Scatter(x=df.Date, y=df.Recoveries,
	                    mode='lines+markers',
	                    name='Recoveries'))
st.plotly_chart(fig, use_container_width=True)


# Create graph for total cases in last 15 days
st.markdown("## " + 'Jun-15 thru Jun-27')
st.markdown("""Displays the Group Bar Chart data for the time period Jun-15th thru Jun-27th. 
	Each day contains Total No of cases, Deaths and Recoveries""")
dates=df.Date

fig = go.Figure(data=[
    go.Bar(name='TotalCases', x=dates, y=df.TotalCases),
    go.Bar(name='Recoveries', x=dates, y=df.Recoveries),
    go.Bar(name='Deaths', x=dates, y=df.Deaths)
])
# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(fig, use_container_width=True)

# Create Graph for State data across all states
st.markdown("## " + 'State Data')
st.markdown("""This chart shows the trends for Total No of cases, Deaths, Recoveries and Hospitalized cases
	across all the states
	""")
fig = go.Figure()
fig.add_trace(go.Scatter(x=dfstate.index, y=dfstate.Cases,
                    mode='lines',
                    name='TotalCases'))
fig.add_trace(go.Scatter(x=dfstate.index, y=dfstate.Death,
	                    mode='lines', name='Deaths'))
fig.add_trace(go.Scatter(x=dfstate.index, y=dfstate.Recov,
	                    mode='lines',
	                    name='Recoveries'))
fig.add_trace(go.Scatter(x=dfstate.index, y=dfstate.Hosp,
	                    mode='lines',
	                    name='Hosp'))
st.plotly_chart(fig, use_container_width=True)


# Select a State from sidebar to update this chart
st.markdown("""This displays the data Total No of cases, Deaths, Recoveries and Hospitalized cases for the
	selected state in the side bar
	""")
Trends=['Cases', 'Death', 'Recov','Hosp']
newdf = dfstate[dfstate['State'] == State_list]
fig = go.Figure([go.Bar(x=Trends, y=[newdf['Cases'].values[0], 
	newdf['Death'].values[0], newdf['Recov'].values[0],
	newdf['Hosp'].values[0]])])
fig.update_layout(title=f'{State_list}')
st.plotly_chart(fig, use_container_width=True)
