import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
descriptive_df = pd.read_csv(r"D:\Data Science Nit - July 2025\34 - 12th September\10th, 11th - Intro to Stats, Descriptive Stats\PROJECT\Inc_Exp_Data.csv")

st.title("Descriptive Statistics Dashboard Created By Akash")
st.write("Explore your dataset interactively using the options below.")

# Sidebar for user choice
option = st.sidebar.selectbox(
    "Choose an operation",
    [
        "Dataset Overview",
        "Mean of Monthly Expense",
        "Median of Monthly Expense",
        "Most Frequent Monthly Expense",
        "Bar Plot - Highest Qualified Member",
        "Scatter Plot - Income vs Expense",
        "Interquartile Range (IQR)",
        "Standard Deviation (First 5 Columns)",
        "Variance (First 4 Columns)",
        "Value Counts - Highest Qualified Member",
        "Bar Plot - No of Earning Members"
    ]
)

# Conditional rendering
if option == "Dataset Overview":
    st.subheader("Dataset Overview")
    st.dataframe(descriptive_df.describe().T)

elif option == "Mean of Monthly Expense":
    st.subheader("Mean of Monthly Expense")
    st.write(f"**Mean:** {descriptive_df['Mthly_HH_Expense'].mean():.2f}")

elif option == "Median of Monthly Expense":
    st.subheader("Median of Monthly Expense")
    st.write(f"**Median:** {descriptive_df['Mthly_HH_Expense'].median():.2f}")

elif option == "Most Frequent Monthly Expense":
    st.subheader("Most Frequent Monthly Expense")
    monthly_exp_temp = pd.crosstab(index=descriptive_df['Mthly_HH_Expense'], columns='count')
    monthly_exp_temp.reset_index(inplace=True)
    result = monthly_exp_temp[monthly_exp_temp['count'] == descriptive_df.Mthly_HH_Expense.value_counts().max()]
    st.dataframe(result)

elif option == "Bar Plot - Highest Qualified Member":
    st.subheader("Bar Plot - Highest Qualified Member")
    fig, ax = plt.subplots()
    descriptive_df['Highest_Qualified_Member'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)

elif option == "Scatter Plot - Income vs Expense":
    st.subheader("Scatter Plot - Income vs Expense")
    fig, ax = plt.subplots()
    descriptive_df.plot(x='Mthly_HH_Income', y='Mthly_HH_Expense', kind='scatter', ax=ax)
    st.pyplot(fig)

elif option == "Interquartile Range (IQR)":
    st.subheader("Interquartile Range (IQR)")
    IQR = descriptive_df['Mthly_HH_Expense'].quantile(0.75) - descriptive_df['Mthly_HH_Expense'].quantile(0.25)
    st.write(f"**IQR:** {IQR:.2f}")

elif option == "Standard Deviation (First 5 Columns)":
    st.subheader("Standard Deviation (First 5 Columns)")
    st.dataframe(pd.DataFrame(descriptive_df.iloc[:, 0:5].std().to_frame()).T)

elif option == "Variance (First 4 Columns)":
    st.subheader("Variance (First 4 Columns)")
    st.dataframe(pd.DataFrame(descriptive_df.iloc[:, 0:4].var().to_frame()).T)

elif option == "Value Counts - Highest Qualified Member":
    st.subheader("Value Counts - Highest Qualified Member")
    st.dataframe(descriptive_df['Highest_Qualified_Member'].value_counts().to_frame().T)

elif option == "Bar Plot - No of Earning Members":
    st.subheader("Bar Plot - No of Earning Members")
    fig, ax = plt.subplots()
    descriptive_df['No_of_Earning_Members'].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
