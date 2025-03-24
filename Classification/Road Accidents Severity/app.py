import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    with open('Label_encoder.pkl', 'rb') as file:
        le = pickle.load(file)
    return model, le

def preprocess_input(user_input, le, column_index):
    if user_input[4] == 'Male':
        user_input[4] = 0
    elif user_input[4] == 'Female':
        user_input[4] = 1
    else:
        user_input[4] = -1
    
    for i, index in enumerate(column_index):
        user_input[index] = le[i].transform([user_input[index]])[0]
    
    return np.array(user_input).reshape(1, -1)

st.set_page_config(layout="wide")

st.markdown(
    """
    <h1 style="text-align: center;">
        🚦 <span style="
            background: linear-gradient(to right, purple, pink); 
            -webkit-background-clip: text; 
            color: transparent;
        ">Accident Severity Prediction</span> 🚑
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e; /* Light black / Dark gray */
        color: white; /* Change text color to white for better contrast */
    }
    .stApp {
        background-color: #1e1e1e;
    }
    </style>
    """,
    unsafe_allow_html=True
)


columns = ['Hours', 'Minutes', 'Day_of_week', 'Age_band_of_driver',
           'Sex_of_driver', 'Educational_level', 'Vehicle_driver_relation',
           'Driving_experience', 'Type_of_vehicle', 'Owner_of_vehicle',
           'Area_accident_occured', 'Lanes_or_Medians', 'Types_of_Junction', 
           'Road_surface_type', 'Road_surface_conditions', 'Light_conditions', 
           'Weather_conditions', 'Type_of_collision',
           'Number_of_vehicles_involved', 'Number_of_casualties',
           'Vehicle_movement', 'Cause_of_accident']

column_index = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<h3 style='text-align: center;color: white;'>🕒 Enter Hours</h3>", unsafe_allow_html=True)
    user_input = [st.slider(" ", 0, 23, 12)]

    st.markdown("<h3 style='text-align: center;color: white;'>⏳ Enter Minutes</h3>", unsafe_allow_html=True)
    user_input.append(st.slider(" ", 0, 59, 30))

    st.markdown("<h3 style='text-align: center;color: white;'>📅 Enter Day of Week</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Friday', 'Monday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']))

    st.markdown("<h3 style='text-align: center;color: white;'>🧑‍🦱 Enter Age Band of Driver</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['18-30', '31-50', 'Over 51', 'Under 18', 'Unknown']))

    st.markdown("<h3 style='text-align: center;color: white;'>🚗 Enter Sex of Driver</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Female', 'Male', 'Unknown']))

with col2:
    st.markdown("<h3 style='text-align: center;color: white;'>📖 Educational Level</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Junior high school', 'Elementary school', 'High school', 'Above high school', 'Writing & reading', 'Unknown', 'Illiterate']))

    st.markdown("<h3 style='text-align: center;color: white;'>👥 Vehicle-Driver Relation</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Employee', 'Owner', 'Other']))

    st.markdown("<h3 style='text-align: center;color: white;'>🚘 Driving Experience</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['1-2yr', '2-5yr', '5-10yr', 'Above 10yr', 'Below 1yr', 'No Licence', 'unknown']))

    st.markdown("<h3 style='text-align: center;color: white;'>🚛 Type of Vehicle</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Animal-Drawn Vehicle', 'Heavy Lorry', 'Large Public Transport', 'Medium Lorry', 'Medium Public Transport', 'Other', 'Passenger Vehicle', 'Pickup Truck', 'Small Public Transport', 'Special Vehicle', 'Two-Wheeler']))

    st.markdown("<h3 style='text-align: center;color: white;'>🏠 Owner of Vehicle</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Governmental', 'Organization', 'Other', 'Owner']))

with col3:
    st.markdown("<h3 style='text-align: center;color: white;'>📍 Area Accident Occurred</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Other', 'Office areas', 'Residential areas', 'Church areas', 'Industrial areas', 'School areas', 'Recreational areas', 'Outside rural areas', 'Hospital areas', 'Rural village areas', 'Market areas']))

    st.markdown("<h3 style='text-align: center;color: white;'>🛣️ Lanes or Medians</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Two-way (divided with broken lines road marking)', 'Undivided Two way', 'other', 'Double carriageway (median)', 'One way', 'Two-way (divided with solid lines road marking)']))

    st.markdown("<h3 style='text-align: center;color: white;'>🔀 Types of Junction</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Crossing', 'No junction', 'O Shape', 'Other', 'T Shape', 'X Shape', 'Y Shape']))

    st.markdown("<h3 style='text-align: center;color: white;'>🛤️ Road Surface Type</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Asphalt roads', 'Asphalt roads with some distress', 'Earth roads', 'Gravel roads', 'Other']))

    st.markdown("<h3 style='text-align: center;color: white;'>🌧️ Road Surface Conditions</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Dry', 'Flood over 3cm. deep', 'Snow', 'Wet or damp']))

    st.markdown("<h3 style='text-align: center;color: white;'>💡 Light Conditions</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Darkness - lights lit', 'Darkness - lights unlit', 'Darkness - no lighting', 'Daylight']))

with col4:
    st.markdown("<h3 style='text-align: center;color: white;'>🌦️ Weather Conditions</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Cloudy', 'Fog or mist', 'Normal', 'Other', 'Raining', 'Raining and Windy', 'Snow', 'Windy']))

    st.markdown("<h3 style='text-align: center;color: white;'>💥 Type of Collision</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Collision with animals', 'Collision with pedestrians', 'Collision with roadside objects', 'Collision with roadside-parked vehicles', 'Fall from vehicles', 'Other', 'Rollover', 'Vehicle with vehicle collision', 'With Train']))

    st.markdown("<h3 style='text-align: center;color: white;'>🚗 Number of Vehicles Involved</h3>", unsafe_allow_html=True)
    user_input.append(st.number_input(" ", min_value=1, step=1))

    st.markdown("<h3 style='text-align: center;color: white;'>🚑 Number of Casualties</h3>", unsafe_allow_html=True)
    user_input.append(st.number_input(" ", min_value=0, step=1))

    st.markdown("<h3 style='text-align: center;color: white;'>🚦 Vehicle Movement</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Entering a junction', 'Getting off', 'Going straight', 'Moving Backward', 'Other', 'Overtaking', 'Parked', 'Reversing', 'Stopping', 'Turnover', 'U-Turn', 'Waiting to go']))

    st.markdown("<h3 style='text-align: center;color: white;'>⚠️ Cause of Accident</h3>", unsafe_allow_html=True)
    user_input.append(st.selectbox(" ", ['Changing lane to the left', 'Changing lane to the right',
       'Driving at high speed', 'Driving carelessly',
       'Driving to the left', 'Driving under the influence of drugs',
       'Drunk driving', 'Getting off the vehicle improperly',
       'Improper parking', 'Moving Backward', 'No distancing',
       'No priority to pedestrian', 'No priority to vehicle', 'Other',
       'Overloading', 'Overspeed', 'Overtaking', 'Overturning',
       'Turnover']))

st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 10px 30px;
        font-size: 90px; /* Adjust font size */
        border-radius: 20px;
        border: none;
        cursor: pointer;
        display: inline-block;
        margin-left: 0;
        font-weight: bold; /* Make text bold */
        transform: scale(1.5); /* Increase size of button & text */
    }
    div.stButton > button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Button on the left
col1, col2 = st.columns([1, 5])

with col1:
    predict_clicked = st.button("Predict")  # Store the button click state

# Process prediction after button click
if predict_clicked:
    model, le = load_model()
    processed_input = preprocess_input(user_input, le, column_index)
    prediction = model.predict(processed_input)[0]

    # Display result at center
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)

    if prediction == 0:
        st.markdown(
            "<div style='background-color: #EAF8ED; color: black; padding: 25px; border-radius: 10px; text-align: center; width: 50%; margin: auto;'>"
            "<h2 style='color: green;'>✅ Slight Injury</h2></div>",
            unsafe_allow_html=True
        )
    elif prediction == 1:
        st.markdown(
            "<div style='background-color: #FFF4E5; color: black; padding: 25px; border-radius: 10px; text-align: center; width: 50%; margin: auto;'>"
            "<h2 style='color: orange;'>⚠️ Serious Injury</h2></div>",
            unsafe_allow_html=True
        )
    elif prediction == 2:
        st.markdown(
            "<div style='background-color: #FCE8E6; color: black; padding: 25px; border-radius: 10px; text-align: center; width: 50%; margin: auto;'>"
            "<h2 style='color: red;'>🚨 Death Injury</h2></div>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)
