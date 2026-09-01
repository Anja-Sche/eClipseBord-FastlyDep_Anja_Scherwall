import streamlit as st
import httpx
import pandas as pd

BASE_URL = "http://127.0.0.1:8000"

def main():
    st.markdown("# Lunar")

    col1_f, col2_f = st.columns([3, 1])

    with col1_f:
        century_range = httpx.get(f"{BASE_URL}/lunar/century_range", timeout=10.0).json()
        min_cen = century_range["min"]
        max_cen = century_range["max"]

        start, end = st.slider("Choose centuries", min_cen, max_cen, (min_cen, max_cen))
        # Help from AI to put start and end in httpx link
        century_between = httpx.get(f"{BASE_URL}/lunar/century_limit?start={start}&end={end}", timeout=30.0).json()

    with col2_f:
        show_type = st.checkbox("Click to see the different types of eclipses")
        
    st.html("<div style='height: 20xp;'></div")

    col1, col2 = st.columns([1, 1])

    with col1:
        averge_eclipse_time = httpx.get(f"{BASE_URL}/lunar/century_avg?start={start}&end={end}", timeout=30.0).json()

        st.metric("Average total time of eclipses (min)", averge_eclipse_time)
    
    with col2:
        amount_eclipses = httpx.get(f"{BASE_URL}/lunar/century_lunar_amount?start={start}&end={end}", timeout=30.0).json()
        st.metric("Amount of eclipses", amount_eclipses)

    st.html("<div style='height: 20xp;'></div")

    if show_type:
            type_eclipse = httpx.get(f"{BASE_URL}/lunar/century_types?start={start}&end={end}", timeout=30.0).json()
    else:
            type_eclipse = httpx.get(f"{BASE_URL}/lunar/century_group_types?start={start}&end={end}", timeout=30.0).json()

    type_eclipse = pd.DataFrame(
        list(type_eclipse.items()), columns=["type", "number"])
    st.bar_chart(type_eclipse, x="type" , y="number")


if __name__ == "__main__":
    main()