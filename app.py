import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Corrected Sample Data: Ensure matching state and spending counts
state_spending = {
    "state": ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"],
    "spending": [3500, 4000, 4200, 3700, 6050, 5000, 5200, 4800, 4600, 4300, 4900, 4100, 4700, 4400, 4000, 3900, 3800, 3600, 4300, 5200, 5500, 3900, 4800, 3400, 4100, 5300, 3700, 4600, 4900, 5100, 3500, 5800, 4300, 5700, 4400, 4200, 5000, 5300, 4600, 4800, 4200, 5600, 3900, 4700, 5400, 5000, 3700, 4500, 5800, 5200]
}

df = pd.DataFrame(state_spending)

fig = px.choropleth(
    df,
    locations="state",
    locationmode="USA-states",
    color="spending",
    color_continuous_scale="YlOrRd",
    scope="usa",
    title="Monthly Consumer Spending per Capita",
    labels={'spending': 'Spending ($)'},
    height=800
)
fig.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'))

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("US Consumer Spending per Capita"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)