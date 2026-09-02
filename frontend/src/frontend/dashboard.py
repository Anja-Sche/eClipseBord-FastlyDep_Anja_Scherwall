import streamlit as st
import httpx
import pandas as pd
import os

BASE_URL = os.getenv("BACKEND_URL","http://127.0.0.1:8000")

def main():
    st.markdown("# eClipseBord - Lunar")

    st.info("As default you see the three group types of lunar eclipses and is able to filter on ceturies." \
    "The average duration of the eclipses and the amount for the period you have chosen is also shown.")

    st.html("<div style='height: 10px;'></div")

    # Separate the page 
    col1_f, col2_f = st.columns([5, 2])

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
        show_type = st.checkbox("All types of lunar eclipses")
        
    

    col1, col2 = st.columns([3, 6])

    with col1:
        # Create KPI for average of total time based on slider values
        average_eclipse_time = httpx.get(f"{BASE_URL}/lunar/century_avg?start={start}&end={end}", timeout=30.0).json()
        st.metric("Average of the total time (min)", average_eclipse_time)
    
    with col2:
        # Create KPI with amount of eclipses based on slider values
        amount_eclipses = httpx.get(f"{BASE_URL}/lunar/century_lunar_amount?start={start}&end={end}", timeout=30.0).json()
        st.metric("Amount of eclipses", amount_eclipses)

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

    with st.expander("Click for information about Lunar Eclipse"):
            st.write("Lunar eclipses occur at the full Moon phase. When Earth is positioned precisely between the Moon and Sun, " \
            "Earth’s shadow falls upon the surface of the Moon, dimming it and sometimes turning the lunar surface a striking red over the course of a few hours. " \
            "Each lunar eclipse is visible from half of Earth.")
            st.write("-NASA (https://science.nasa.gov/moon/eclipses/)")

if __name__ == "__main__":
    main()