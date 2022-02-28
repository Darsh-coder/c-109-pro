from turtle import pd
import plotly.express as px
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go
import statistics as s
import pandas as pd

df = pd.read_csv("ds.csv")
height_series = df["math score"]
dice_list = height_series.tolist()
fig = ff.create_distplot([dice_list],["maths marks"],show_hist = False)
fig.show()


mean = s.mean(dice_list)
mode = s.mode(dice_list)
median = s.median(dice_list)
st_dev = s.stdev(dice_list)

#fig = px.scatter(x=dice_list,y=count)
fig = ff.create_distplot([dice_list],["result"])



first_st_dev_start,first_st_dev_end = mean-st_dev,mean + st_dev

second_st_dev_start,second_st_dev_end = mean-(2*st_dev),mean +(2*st_dev)

third_st_dev_start,third_st_dev_end = mean-(3*st_dev),mean + (3*st_dev)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.1],mode="lines",name ="mean"))


fig.add_trace(go.Scatter(x=[first_st_dev_start,first_st_dev_start],y=[0,0.1],mode="lines",name ="std_1"))

fig.add_trace(go.Scatter(x=[first_st_dev_end,first_st_dev_end],y=[0,0.1],mode="lines",name ="std_1"))



fig.add_trace(go.Scatter(x=[second_st_dev_start,second_st_dev_start],y=[0,0.1],mode="lines",name ="std_2"))

fig.add_trace(go.Scatter(x=[second_st_dev_end,second_st_dev_end],y=[0,0.1],mode="lines",name ="std_2"))



fig.add_trace(go.Scatter(x=[third_st_dev_start,third_st_dev_start],y=[0,0.1],mode="lines",name ="std_3"))

fig.add_trace(go.Scatter(x=[third_st_dev_end,third_st_dev_end],y=[0,0.1],mode="lines",name ="std_3"))


print("mean is",+ mean)
print("mode is",+ mode)
print("median is",+ median)
print("st_devi is",+ st_dev)

fig.show()


list_of_data_1_std_dev = [result for result in dice_list if result > first_st_dev_start and result< first_st_dev_end  ]

list_of_data_2_std_dev = [result for result in dice_list if result > second_st_dev_start and result< second_st_dev_end  ]

list_of_data_3_std_dev = [result for result in dice_list if result > third_st_dev_start and result< third_st_dev_end  ]


print("percentage data of within one std dev ",(len(list_of_data_1_std_dev)/len(dice_list)*100))

print("percentage data of within one std dev ",(len(list_of_data_2_std_dev)/len(dice_list)*100))

print("percentage data of within one std dev ",(len(list_of_data_3_std_dev)/len(dice_list)*100))