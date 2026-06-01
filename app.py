import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Real Estate Buyer Segmentation",
    page_icon="🏠",
    layout="wide"
)

df = pd.read_csv("client_segments.csv")

st.write(df.columns.tolist())
st.title("🏠 Real Estate Buyer Segmentation Dashboard")

st.write("""
Machine Learning Based Buyer Segmentation and Investment Profiling
for Real Estate Market Intelligence
""")

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Clients", len(df))

with col2:
    st.metric("Total Segments", df["cluster_name"].nunique())

with col3:
    st.metric("Average Investment",
              f"${df['total_investment'].mean():,.0f}")

st.header("Cluster Distribution")

cluster_counts = df["cluster_name"].value_counts()

st.bar_chart(cluster_counts)

st.header("Segment Summary")

summary = df.groupby("cluster_name").agg({
    "total_investment": "mean",
    "num_properties": "mean",
    "age": "mean"
}).round(2)

st.dataframe(summary)

st.header("Client Data")

st.dataframe(df)

st.success("Project Successfully Completed")