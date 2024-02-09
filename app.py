# import streamlit as st 
# import pickle
# import pandas as pd

# teams=['Kolkata Knight Riders', 'Rajasthan Royals', 'Mumbai Indians',
#        'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings',
#        'Punjab Kings', 'Royal Challengers Bangalore', 'Gujarat Lions',
#        'Lucknow Super Giants']

# cities=['Kolkata', 'Mumbai', 'Ahmedabad', 'Abu Dhabi', 'Hyderabad',
#        'Bangalore', 'Chandigarh', 'Chennai', 'Rajkot', 'Delhi', 'Nagpur',
#        'Ranchi', 'Pune', '_Other', 'Bengaluru', 'Jaipur', 'Sharjah ',
#        'Visakhapatnam', 'Dubai ', 'Dharamsala', 'Indore', 'Sharjah',
#        'Kanpur', 'Raipur', 'Mohali', 'Cuttack']


# pipe=pickle.load(open('pipe.pkl','rb'))
# pipe_rf=pickle.load(open('pipe_rf.pkl','rb'))

# st.title('Match Prediction')

# col1,col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Batting team',sorted(teams))

# with col2:
#     bowling_team = st.selectbox('Bowling team',sorted(teams))
    
# selected_city = st.selectbox("Host city",sorted(cities))

 
# toss_winner = st.selectbox("Toss winner",[batting_team,bowling_team])




# col4, col5,col6,col7 = st.columns(4)

# with col4:
#     target =st.number_input("Target",step=1)

# with col5:
#     score = st.number_input("Current Score",step=1)

# with col6:
#     overs = st.number_input("Overs",step=1,max_value=20)

# with col7:
#     wickets = st.number_input("Wickets",step=1,max_value=10)
    
# if st.button("predict Probability"):
#     runs_left = target-score
#     balls_left=120-(overs*6)
#     wickets_left=(10-wickets)
#     crr=score/overs
#     rrr=(runs_left)/(balls_left/6)
    
#     input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'toss_winner':[toss_winner],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target':[target],'crr':[crr],'rrr':[rrr]})
    
#     # st.table(input_df)
    
#     prediction = pipe.predict_proba(input_df)
    
#     loss=prediction[0][0]
#     win=prediction[0][1]
    
#     st.header(batting_team + "- " + str(round(win*100))+ "%")
#     st.header(bowling_team + "- " + str(round(loss*100))+ "%")
    
#     prediction_rf=pipe_rf.predict(input_df)
#     if prediction_rf==1:
#         winner=batting_team
#     else:
#         winner=bowling_team
        
#     st.write("rf_Win"+": " + winner)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# import streamlit as st 
# import pickle
# import pandas as pd

# teams=['Kolkata Knight Riders', 'Rajasthan Royals', 'Mumbai Indians',
#        'Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings',
#        'Punjab Kings', 'Royal Challengers Bangalore', 'Gujarat Lions',
#        'Lucknow Super Giants']

# cities=['Kolkata', 'Mumbai', 'Ahmedabad', 'Abu Dhabi', 'Hyderabad',
#        'Bangalore', 'Chandigarh', 'Chennai', 'Rajkot', 'Delhi', 'Nagpur',
#        'Ranchi', 'Pune', '_Other', 'Jaipur', 'Sharjah ',
#        'Visakhapatnam', 'Dubai ', 'Dharamsala', 'Indore', 'Sharjah',
#        'Kanpur', 'Raipur', 'Mohali', 'Cuttack']


# pipe=pickle.load(open('pipe.pkl','rb'))
# pipe_rf=pickle.load(open('pipe_rf.pkl','rb'))

# st.title('Match Prediction')

# col1,col2 = st.columns(2)

# with col1:
#     batting_team = st.selectbox('Batting team',sorted(teams),index=8)

# with col2:
#     bowling_team = st.selectbox('Bowling team',sorted(teams),index=5)
    
# selected_city = st.selectbox("Host city",sorted(cities),index=2)

 
# toss_winner = st.radio("Toss winner",[batting_team,bowling_team],index=0)


# col8, col9,col10,col11 = st.columns(4)

# with col8:
#     target =st.number_input("Target",step=1,value=200)

# with col9:
#     score = st.number_input("Current Score",step=5,value=170,max_value=target)

# with col10:
#     overs = st.number_input("Overs",step=1,max_value=20,value=16,min_value=1)

# with col11:
#     wickets = st.number_input("Wickets",step=1,max_value=10,value=3,min_value=0)
    
# if st.button("predict Probability"):
#     runs_left = target-score
#     balls_left=120-(overs*6)
#     wickets_left=(10-wickets)
#     crr=score/overs
#     rrr=(runs_left)/(balls_left/6)
#     # batting_wl_ratio=bat_wins/bat_losses
#     # bowling_wl_ratio=bowl_wins/bowl_losses
    
#     # return row['batting_wins'] if row['batting_losses']==0 else (row['batting_wins']/row['batting_losses'])
    
#     input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'toss_winner':[toss_winner],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target':[target],'crr':[crr],'rrr':[rrr]})
 
    
#     # st.table(input_df)
    
#     prediction = pipe.predict_proba(input_df)
    
#     loss=prediction[0][0]
#     win=prediction[0][1]
    
#     st.header(batting_team + "- " + str(round(win*100))+ "%")
#     st.header(bowling_team + "- " + str(round(loss*100))+ "%")
    
#     prediction_rf=pipe_rf.predict(input_df)
#     prediction_rf_proba = pipe_rf.predict_proba(input_df) 
#     if prediction_rf==1:
#         winner=batting_team
#         chance=prediction_rf_proba[0][1]
#     else:
#         winner=bowling_team
#         chance=prediction_rf_proba[0][0]

      
#     st.write("rf_Win"+": " + winner + " " + str(round(chance*100)) +"%")
    
    
#----------------------------------------------------------------------------------------------------------------------------- 

import streamlit as st 
import pickle
import pandas as pd

teams=['Kolkata Knight Riders', 'Rajasthan Royals', 'Mumbai Indians','Sunrisers Hyderabad', 'Delhi Capitals', 'Chennai Super Kings','Punjab Kings', 'Royal Challengers Bangalore', 'Gujarat Titans','Lucknow Super Giants']

cities=['Kolkata', 'Mumbai', 'Ahmedabad', 'Abu Dhabi', 'Hyderabad','Bangalore', 'Chandigarh', 'Chennai', 'Rajkot', 'Delhi', 'Nagpur','Ranchi', 'Pune', '_Other', 'Jaipur', 'Sharjah ','Visakhapatnam', 'Dubai ', 'Dharamsala', 'Indore', 'Sharjah','Kanpur', 'Raipur', 'Mohali', 'Cuttack']


# pipe=pickle.load(open('pipe.pkl','rb'))
pipe_rf=pickle.load('pipe_rf.pkl')

st.title('Match Prediction')

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Batting team',sorted(teams),index=8)

with col2:
    bowling_team = st.selectbox('Bowling team',sorted(teams),index=1)
    
selected_city = st.selectbox("Host city",sorted(cities),index=2)

toss_winner = st.radio("Toss winner",[batting_team,bowling_team],index=0)


col8, col9,col10,col11 = st.columns(4)

with col8:
    target =st.number_input("Target",step=5,value=185)

with col9:
    score = st.number_input("Current Score",step=5,value=160,max_value=target)

with col10:
    overs = st.number_input("Overs",step=1,max_value=19,value=16,min_value=1)

with col11:
    wickets = st.number_input("Wickets",step=1,max_value=9,value=3,min_value=0)
    
if st.button("predict Probability"):
    runs_left = target-score
    balls_left=120-(overs*6)
    wickets_left=(10-wickets)
    crr=score/overs
    rrr=(runs_left)/(balls_left/6)
    # batting_wl_ratio=bat_wins/bat_losses
    # bowling_wl_ratio=bowl_wins/bowl_losses
    
    # return row['batting_wins'] if row['batting_losses']==0 else (row['batting_wins']/row['batting_losses'])
    
    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'toss_winner':[toss_winner],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'target':[target],'crr':[crr],'rrr':[rrr]})
    
    # st.table(input_df)
    
    prediction = pipe_rf.predict_proba(input_df)
    
    loss=prediction[0][0]
    win=prediction[0][1]
    
    st.header(batting_team + "- " + str(round(win*100))+ "%")
    st.header(bowling_team + "- " + str(round(loss*100))+ "%")
    

    
    # prediction_rf=pipe_rf.predict(input_df)
    # prediction_rf_proba = pipe_rf.predict_proba(input_df) 
    # if prediction_rf==1:
    #     winner=batting_team
    #     chance=prediction_rf_proba[0][1]
    # else:
    #     winner=bowling_team
    #     chance=prediction_rf_proba[0][0]  
    # st.write("rf_Win"+": " + winner)
    
