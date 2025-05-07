from preswald import text, plotly, connect, get_df, table, button
import pandas as pd
import plotly.express as px

# Initialize connection
text("# Sleep Health and Lifestyle Dashboard")
text("Analyzing relationships between sleep patterns and lifestyle factors")

# Load the CSV
connect()
df = get_df('sleep_health_dataset')

# Create visualizations without filters
text("## Sleep Duration vs Quality of Sleep")
fig1 = px.scatter(
    df,
    x="Sleep Duration",
    y="Quality of Sleep",
    color="Gender",
    hover_data=["Age", "Occupation", "BMI Category"],
    title="Sleep Duration vs Quality of Sleep"
)
fig1.update_layout(template='plotly_white')
plotly(fig1)

text("## Physical Activity vs Sleep Quality")
fig2 = px.scatter(
    df,
    x="Physical Activity Level",
    y="Quality of Sleep",
    color="BMI Category",
    size="Stress Level",
    title="Physical Activity vs Sleep Quality"
)
fig2.update_layout(template='plotly_white')
plotly(fig2)

text("## Average Sleep Duration by Occupation")
avg_sleep = df.groupby("Occupation")["Sleep Duration"].mean().reset_index().sort_values("Sleep Duration")
fig3 = px.bar(
    avg_sleep,
    x="Occupation",
    y="Sleep Duration",
    title="Average Sleep Duration by Occupation",
    color="Sleep Duration"
)
fig3.update_layout(template='plotly_white')
plotly(fig3)

# Summary statistics
text("## Summary Statistics")
summary = pd.DataFrame({
    "Metric": ["Average Sleep Duration", "Average Quality of Sleep", "Average Physical Activity", 
               "Average Stress Level", "Average Heart Rate", "Average Daily Steps"],
    "Value": [
        f"{df['Sleep Duration'].mean():.2f} hours",
        f"{df['Quality of Sleep'].mean():.2f}/10",
        f"{df['Physical Activity Level'].mean():.2f} minutes",
        f"{df['Stress Level'].mean():.2f}/10",
        f"{df['Heart Rate'].mean():.2f} BPM",
        f"{df['Daily Steps'].mean():.0f} steps"
    ]
})
table(summary)

# Show the data
text("## Sleep Health Data")
table(df)
