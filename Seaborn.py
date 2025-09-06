# Import necessary libraries
import streamlit as st          # Streamlit for creating interactive web apps
import seaborn as sns           # Seaborn for advanced data visualization
import matplotlib.pyplot as plt # Matplotlib for controlling plots

# Set Seaborn style for consistent look
sns.set(style="whitegrid")

# Load the built-in 'tips' dataset from Seaborn (restaurant bills & tips data)
tips = sns.load_dataset('tips')

# Streamlit app title and description
st.title("Comprehensive Tips Dataset Visualizations")
st.write("This app displays a variety of Seaborn plots created by Akash Sen, exploring the Tips dataset, which includes data on restaurant bills and tips.")

# Define a reusable function to display plots inside Streamlit
def display_plot(title, plot_func):
    st.subheader(title)                   # Add a subheader for each plot
    fig, ax = plt.subplots(figsize=(8, 6))# Create a new figure and axes
    plot_func(ax)                         # Call the plotting function, passing in the axis
    st.pyplot(fig)                        # Display the figure in Streamlit
    plt.close(fig)                        # Close the figure to free memory

# ---------- Plot Definitions ----------

# Scatter Plot: Show relationship between total_bill and tip, differentiated by time & size
def scatter_plot(ax):
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", size="size", palette="deep", ax=ax)
    ax.set_title("Scatter Plot: Total Bill vs Tip by Time and Size")

# Line Plot: Show total bill trend by party size and sex
def line_plot(ax):
    sns.lineplot(data=tips, x="size", y="total_bill", hue="sex", ci=None, marker="o", ax=ax)
    ax.set_title("Line Plot: Total Bill by Party Size and Sex")

# Bar Plot: Average total bill per day grouped by sex
def bar_plot(ax):
    sns.barplot(data=tips, x="day", y="total_bill", hue="sex", palette="muted", ax=ax)
    ax.set_title("Bar Plot: Average Total Bill by Day and Sex")

# Box Plot: Distribution of tips by day and smoker status
def box_plot(ax):
    sns.boxplot(data=tips, x="day", y="tip", hue="smoker", palette="Set2", ax=ax)
    ax.set_title("Box Plot: Tips by Day and Smoker Status")

# Violin Plot: Distribution + density of total bill by day and time
def violin_plot(ax):
    sns.violinplot(data=tips, x="day", y="total_bill", hue="time", split=True, palette="pastel", ax=ax)
    ax.set_title("Violin Plot: Total Bill by Day and Time")

# Count Plot: Frequency of orders per day grouped by smoker status
def count_plot(ax):
    sns.countplot(data=tips, x="day", hue="smoker", palette="dark", ax=ax)
    ax.set_title("Count Plot: Orders by Day and Smoker Status")

# Regression Plot: Relationship between total bill and tip with regression line
def reg_plot(ax):
    sns.regplot(data=tips, x="total_bill", y="tip", scatter_kws={"s": 50}, line_kws={"color": "red"}, ax=ax)
    ax.set_title("Regression Plot: Total Bill vs Tip")

# Histogram: Distribution of total bills with density estimate
def hist_plot(ax):
    sns.histplot(data=tips, x="total_bill", kde=True, bins=20, color="blue", ax=ax)
    ax.set_title("Histogram: Distribution of Total Bill")

# Strip Plot: Show all individual data points of tips by day & sex
def strip_plot(ax):
    sns.stripplot(data=tips, x="day", y="tip", hue="sex", palette="Set1", jitter=True, ax=ax)
    ax.set_title("Strip Plot: Tips by Day and Sex")

# Swarm Plot: Similar to strip plot but avoids overlap of points
def swarm_plot(ax):
    sns.swarmplot(data=tips, x="day", y="tip", hue="smoker", palette="Set3", ax=ax)
    ax.set_title("Swarm Plot: Tips by Day and Smoker Status")

# KDE Plot: Show distribution density of total bill separated by sex
def kde_plot(ax):
    sns.kdeplot(data=tips, x="total_bill", hue="sex", fill=True, palette="tab10", ax=ax)
    ax.set_title("KDE Plot: Total Bill Density by Sex")

# ---------- Special Complex Plots ----------

# Pair Plot: Pairwise relationships between numerical variables, grouped by sex
st.subheader("Pair Plot: Numerical Variables by Sex")
pair_fig = sns.pairplot(tips, hue="sex", vars=["total_bill", "tip", "size"], palette="husl")
pair_fig.fig.suptitle("Pair Plot: Numerical Variables by Sex", y=1.02)
st.pyplot(pair_fig.fig)   # Display in Streamlit
plt.close(pair_fig.fig)   # Close to free memory

# Joint Plot: Scatter plot + histograms showing relationship between total_bill & tip by smoker status
st.subheader("Joint Plot: Total Bill vs Tip by Smoker")
joint_fig = sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter", hue="smoker", palette="coolwarm")
joint_fig.fig.suptitle("Joint Plot: Total Bill vs Tip by Smoker", y=1.02)
st.pyplot(joint_fig.fig)
plt.close(joint_fig.fig)

# FacetGrid: Multiple histograms split by time and smoker
st.subheader("FacetGrid: Total Bill by Time and Smoker")
g = sns.FacetGrid(tips, col="time", row="smoker", margin_titles=True)
g.map(sns.histplot, "total_bill", bins=15)
g.fig.suptitle("FacetGrid: Total Bill by Time and Smoker", y=1.02)
st.pyplot(g.fig)
plt.close(g.fig)

# Catplot (Point): Point plot of tips by day and sex
st.subheader("Catplot (Point): Tips by Day and Sex")
cat_fig = sns.catplot(data=tips, x="day", y="tip", hue="sex", kind="point", palette="bright")
cat_fig.fig.suptitle("Catplot (Point): Tips by Day and Sex", y=1.02)
st.pyplot(cat_fig.fig)
plt.close(cat_fig.fig)

# ---------- Display all standard plots ----------

display_plot("Scatter Plot", scatter_plot)
display_plot("Line Plot", line_plot)
display_plot("Bar Plot", bar_plot)
display_plot("Box Plot", box_plot)
display_plot("Violin Plot", violin_plot)
display_plot("Count Plot", count_plot)
display_plot("Regression Plot", reg_plot)
display_plot("Histogram", hist_plot)
display_plot("Strip Plot", strip_plot)
display_plot("Swarm Plot", swarm_plot)
display_plot("KDE Plot", kde_plot)

# Final message
st.write("All Seaborn plots for the Tips dataset have been generated!")
