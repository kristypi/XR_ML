import pandas as pd
import plotly.graph_objs as go

data = pd.read_csv("/Users/jjaehui/USACO Problems/3.20/consulting_data_content_logic.csv")

print(data.info()) # 어떤 정보들이 있는지 나열해서 보여줌
print(data.head(10)) # 그 정보들을 10가지 랜덤으로 보여줌

data_male = data[data["gender"] == "Male"]
data_female = data[data["gender"] == "Female"]

print("Average Sentiment for Male: ", data_male["sentiment"].mean())
print("Average Sentiment for Female: ", data_female["sentiment"].mean())

print("Type of Consulting\n", data["type_of_consulting"].unique())
print("Type of Consulting\n", data["consulting_content"].unique()) # Contents들을 나열해줌
print("Type of Consulting\n", data["the_consultant"].unique())

consulting_counts = data["type_of_consulting"].value_counts()

print(consulting_counts)

consulting_df = consulting_counts.reset_index()
consulting_df.columns = ["Type of Consulting", "Count"]

colors = ["#FF9633", "#FFF033", "#99FF33", "#33FFA2", "#33E9FF", "#9933FF"]

#### Pie chart for the number of type of consulting ####

#fig = go.Figure(data=[go.Pie(labels = consulting_df["Type of Consulting"], values = consulting_df["Count"], marker = dict(colors=colors))])
#fig.update_layout(title = "Number of Each Type of COnsulting")
#
#fig.show()


#print(data["age"])
#age_histogram = go.Histogram(x = data["age"], nbinsx=10)
#age_layout = go.Layout(title = "Age Distribution")
#age_fig = go.Figure(data = [age_histogram], layout = age_layout)
#age_fig.show()


age_groups = pd.cut(data["age"], bins = [0, 20, 30, 40, 50, 60, 70], labels = ["0-20", "21-30", "31-40", "41-50", "51-60", "61-70"])
age_group_counts = age_groups.value_counts()
print(age_group_counts)
fig = go.Figure(data = [go.Pie(labels = age_group_counts.index, values = age_group_counts.values)])
fig.update_layout(title = "Age Group Distribution")

fig.show()




