import streamlit as st
import httpx
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

def main():
    st.markdown("# eClipseBord - Lunar")

    # Separate the page 
    col1_f, col2_f = st.columns([3, 1])

    with col1_f:
        # Put default setting to slider values
        century_range = httpx.get(f"{BASE_URL}/lunar/century_range", timeout=10.0).json()
        min_cen = century_range["min"]
        max_cen = century_range["max"]

        # Take users input on slider values
        start, end = st.slider("Choose span of centuries (BCE to the left)", min_cen, max_cen, (min_cen, max_cen))
        # Help from AI to put start and end in httpx link
        century_between = httpx.get(f"{BASE_URL}/lunar/century_limit?start={start}&end={end}", timeout=30.0).json()

    with col2_f:
        # Create a checkbox
        show_type = st.checkbox("Click to see the different types of lunar eclipses")
        
    st.html("<div style='height: 20px;'></div")

    col1, col2 = st.columns([3, 6])

    with col1:
        # Create KPI for average of total time based on slider values
        average_eclipse_time = httpx.get(f"{BASE_URL}/lunar/century_avg?start={start}&end={end}", timeout=30.0).json()
        st.metric("Average of the total time (min)", average_eclipse_time)
    
    with col2:
        # Create KPI with amount of eclipses based on slider values
        amount_eclipses = httpx.get(f"{BASE_URL}/lunar/century_lunar_amount?start={start}&end={end}", timeout=30.0).json()
        st.metric("Amount of eclipses", amount_eclipses)

    st.html("<div style='height: 20px;'></div")

    # If checkbox is clicked -> show different eclipse types
    if show_type:
            type_eclipse = httpx.get(f"{BASE_URL}/lunar/century_types?start={start}&end={end}", timeout=30.0).json()
    # if not clicked -> show type groups
    else:
            type_eclipse = httpx.get(f"{BASE_URL}/lunar/century_group_types?start={start}&end={end}", timeout=30.0).json()

    # Bar chart to show amounts of different eclipse types, based on checkbox
    type_eclipse = pd.DataFrame(
        list(type_eclipse.items()), columns=["type", "number"])
    st.bar_chart(type_eclipse, x="type" , y="number", x_label="Type of Eclipse", y_label="Amount of Eclipses")


if __name__ == "__main__":
    main()