import numpy as np # Handles the Math
import pandas as pd # Handles data manipulation & analysis
import matplotlib.pyplot as plt # Present the data in 2D visualization

# Create a sample data of Game category and sales
data = {
    "Genres": ["Indie", "AAA", "Strategy", "First person shooter", "3rd Person shooter"],
    "Sales": [1000, 1355, 986, 1342, 1015]
}

# Frame the data using Pandas
df = pd.DataFrame(data)

# Let's do the Math using Numpy

"""Total sales, Max sale amount, Avg of sales from Genres"""

total_sales = np.sum(df["Sales"])
Highest_sale_Amount = np.amax(df["Sales"])
highest_sales_genre = df.loc[df["Sales"].idxmax(), "Genres"]
Avg_of_sales_per_Genre = np.average(df["Sales"])

# Time to visualize the data

# Make a bar chart
plt.figure(figsize=(10,8))

plt.bar(
    df["Genres"], df["Sales"],
    color = "#841D1D",
    edgecolor = 'black',
    width= 0.6
    )

# Giving title
plt.title("Video Game sales by Genre", fontsize=12, fontweight='bold', pad=12)

# Decorate X & Y label
plt.xlabel("Genres", fontweight='bold')
plt.ylabel("Sales", fontweight='bold') 

# Show the Math by Numpy
plt.text(
    0.75, 1.13, 
    f"Calculations\n"
    f"Total Sales: {total_sales}\n"
    f"Highest Sale Amount: {Highest_sale_Amount} Genre: {highest_sales_genre}\n"
    f"Average Sales Per Genre: {Avg_of_sales_per_Genre:.2f}",
    transform=plt.gca().transAxes,
    fontsize=10,
    verticalalignment="top",
    bbox=dict(
        boxstyle="round",
        facecolor="white",
        edgecolor="black"
    )
)

#Display
plt.show()
