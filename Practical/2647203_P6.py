# =======================================================================
# Domain: Clean Energy Systems & Grid Decarbonization
# Topic : Microgrid Telemetry Analytics Application
# =======================================================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="Clean Energy Microgrid Dashboard",
    layout="wide"
)

# -----------------------------------------------------------------------
# Load Dataset with Caching
# -----------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("microgrid_energy_dataset.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df

df = load_data()

# -----------------------------------------------------------------------
# 1. Application Layout & Navigation: Sidebar Controls
# -----------------------------------------------------------------------
st.sidebar.title("Telemetry Filter Controls")

# Widget 1: Multiselect for Energy Status
status_options = df["energy_status"].unique().tolist()
selected_status = st.sidebar.multiselect(
    "Filter by Energy Status:",
    options=status_options,
    default=status_options
)

# Widget 2: Slider for Battery SoC Range
min_soc, max_soc = float(df["battery_soc"].min()), float(df["battery_soc"].max())
selected_soc = st.sidebar.slider(
    "Filter by Battery SoC Range (%):",
    min_value=round(min_soc, 1),
    max_value=round(max_soc, 1),
    value=(round(min_soc, 1), round(max_soc, 1))
)

# Widget 3: Selectbox for Hour of Day
hour_options = ["All Hours"] + sorted(df["hour_of_day"].unique().tolist())
selected_hour = st.sidebar.selectbox("Filter by Hour of Day:", hour_options)

# Apply dynamic filters
filtered_df = df[
    (df["energy_status"].isin(selected_status)) &
    (df["battery_soc"] >= selected_soc[0]) &
    (df["battery_soc"] <= selected_soc[1])
]

if selected_hour != "All Hours":
    filtered_df = filtered_df[filtered_df["hour_of_day"] == selected_hour]

# -----------------------------------------------------------------------
# Main Dashboard Header & Dynamic KPIs
# -----------------------------------------------------------------------
st.title("Clean Energy Microgrid and BESS Dispatch Console")
st.write("Real-time telemetry analytics, energy balance monitoring, and storage dispatch diagnostics.")

# KPI Columns
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Records", f"{len(filtered_df):,}")

with col2:
    total_gen = filtered_df["total_power_generation"].sum() / 1000.0
    st.metric("Total Gen (MWh)", f"{total_gen:,.2f}")

with col3:
    avg_gen = filtered_df["total_power_generation"].mean() if not filtered_df.empty else 0.0
    st.metric("Avg Gen (kW)", f"{avg_gen:,.2f}")

with col4:
    avg_load = filtered_df["load_demand"].mean() if not filtered_df.empty else 0.0
    st.metric("Avg Load (kW)", f"{avg_load:,.2f}")

with col5:
    avg_soc = filtered_df["battery_soc"].mean() if not filtered_df.empty else 0.0
    st.metric("Avg Battery SoC", f"{avg_soc:.1f} %")

st.divider()

# -----------------------------------------------------------------------
# Navigation: Tabs Structure
# -----------------------------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Dataset Overview", "Data Analysis", "Visualizations", "Insights"])

# --- TAB 1: DATASET OVERVIEW ---
with tab1:
    st.subheader("Raw Microgrid Telemetry (Filtered View)")
    st.dataframe(filtered_df.head(100), use_container_width=True)

    with st.expander("Click to view Dataset Schema and Summary Statistics"):
        st.write("Summary Statistics:")
        st.dataframe(filtered_df[["solar_power_output", "wind_power_output", "battery_soc", "load_demand", "grid_import_power"]].describe())

# --- TAB 2: DATA ANALYSIS ---
with tab2:
    st.subheader("Category-Wise Power Breakdown and Energy Balance")
    
    col_a, col_b = st.columns(2)
    with col_a:
        with st.container():
            st.write("### Energy Status Record Count")
            status_counts = filtered_df["energy_status"].value_counts().reset_index()
            status_counts.columns = ["Energy Status", "Observations"]
            st.table(status_counts)

    with col_b:
        with st.container():
            st.write("### Average Metrics by Energy State")
            grouped_status = filtered_df.groupby("energy_status")[["total_power_generation", "load_demand", "battery_soc"]].mean()
            st.dataframe(grouped_status.round(2))

# --- TAB 3: VISUALIZATIONS ---
with tab3:
    st.subheader("Exploratory Data Visualizations")

    if filtered_df.empty:
        st.warning("No records match the selected filter combination.")
    else:
        viz_col1, viz_col2 = st.columns(2)

        # 2a. Bar Chart: Energy Status Distribution
        with viz_col1:
            st.write("### 1. Distribution of Operational Energy Status")
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            status_counts = filtered_df["energy_status"].value_counts()
            ax1.bar(status_counts.index, status_counts.values)
            ax1.set_title("Operational Status Counts")
            ax1.set_xlabel("Energy Status")
            ax1.set_ylabel("Number of Observations")
            ax1.grid(axis="y", linestyle="--", alpha=0.5)
            st.pyplot(fig1)
            st.caption("Interpretation: Compares the frequency of surplus generation against periods of energy deficit.")

        # 2b. Line Chart: Generation & Load Trends over Sample Chronology
        with viz_col2:
            st.write("### 2. Generation vs Load Demand Profile")
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sample_df = filtered_df.head(60)
            ax2.plot(sample_df.index, sample_df["total_power_generation"], label="Total Generation (kW)")
            ax2.plot(sample_df.index, sample_df["load_demand"], label="Grid Load Demand (kW)", linestyle="--")
            ax2.set_title("Renewable Generation vs Demand Sequence")
            ax2.set_xlabel("Observation Index")
            ax2.set_ylabel("Power (kW)")
            ax2.legend(loc="upper right")
            ax2.grid(True, linestyle="--", alpha=0.5)
            st.pyplot(fig2)
            st.caption("Interpretation: Displays power generation variations relative to load demand.")

        st.divider()
        
        # 2c. Scatter Plot: Solar Irradiance vs Solar Power Output
        st.write("### 3. Solar Irradiance vs Solar Power Output")
        fig3, ax3 = plt.subplots(figsize=(8, 4))
        ax3.scatter(
            filtered_df["solar_irradiance"],
            filtered_df["solar_power_output"],
            alpha=0.5
        )
        ax3.set_title("Solar Power Output as a Function of Irradiance")
        ax3.set_xlabel("Solar Irradiance (W/m2)")
        ax3.set_ylabel("Solar Power Output (kW)")
        ax3.grid(True, linestyle="--", alpha=0.5)
        st.pyplot(fig3)
        st.caption("Interpretation: Shows positive correlation between solar irradiance and solar generation.")

# --- TAB 4: INSIGHTS ---
with tab4:
    st.subheader("Key Findings and Operational Insights")
    st.write("1. Renewable Self-Sufficiency: Energy deficits occur during periods when load demand exceeds total renewable generation, requiring storage discharge or grid import.")
    st.write("2. Storage Utilization: Battery state of charge regulates whether the microgrid can support local load demand during generation shortfalls[cite: 14].")
    st.write("3. Grid Balance: Periods of energy surplus coincide with high solar irradiance and wind velocity, allowing battery charging or grid export[cite: 14].")