import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(file):
    # Load CSV file into a DataFrame
    data = pd.read_csv(file)
    return data

def main():
    st.set_page_config(page_title='Graphs by Streamlit', page_icon=':bar_chart:')
    st.subheader('_By:_ Zulfiqar :blue[Ahmed] :sunglasses:')
    # Add title and description
    st.title('Graphs by Streamlit')
    st.write("This page allows you to create graphs based on the selected chart type.")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Load data
        data = load_data(uploaded_file)

        # Sidebar with chart type options
        chart_type = st.sidebar.selectbox("Select Chart Type", ["Line Chart", "Bar Chart", "Scatter Plot"])

        # Create chart based on user selection
        if chart_type == "Line Chart":
            st.subheader("Line Chart")
            fig = px.line(data)
            st.plotly_chart(fig)

        elif chart_type == "Bar Chart":
            st.subheader("Bar Chart")
            fig = px.bar(data)
            st.plotly_chart(fig)

        elif chart_type == "Scatter Plot":
            st.subheader("Scatter Plot")
            fig = px.scatter(data)
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()
