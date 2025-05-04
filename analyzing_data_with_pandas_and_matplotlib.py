# Analyzing Data with Pandas and Visualizing Results with Matplotlib

# Task 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (Iris dataset)
df = pd.read_csv('iris.csv')

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data types
print("\nData Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset (drop or fill missing values)
df = df.dropna()  # or use df.fillna(value)

# Task 2: Basic Data Analysis
# Summary statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by a categorical column and compute the mean
# Group by 'species' and calculate mean values for each species
if 'species' in df.columns:
    grouped = df.groupby('species').mean()
    print("\nMean values grouped by species:")
    print(grouped)

# Task 3: Data Visualization
# Line Chart Example
plt.figure(figsize=(8,5))
if 'sepal length (cm)' in df.columns:
    df['sepal length (cm)'].plot(kind='line')
    plt.title("Sepal Length Over Index")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length (cm)")
    plt.grid(True)
    plt.show()

# Bar Chart Example
plt.figure(figsize=(8,5))
if 'species' in df.columns:
    df['species'].value_counts().plot(kind='bar', color='skyblue')
    plt.title("Count of Each Species")
    plt.xlabel("Species")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()

# Pie Chart Example
plt.figure(figsize=(6,6))
if 'species' in df.columns:
    df['species'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=140)
    plt.title("Species Distribution")
    plt.ylabel("")
    plt.show()

# Histogram Example
plt.figure(figsize=(8,5))
if 'petal length (cm)' in df.columns:
    df['petal length (cm)'].plot(kind='hist', bins=10, color='lightgreen')
    plt.title("Petal Length Distribution")
    plt.xlabel("Petal Length (cm)")
    plt.grid(True)
    plt.show()

# Findings/Observations
print("\nObservations:")
print("- The dataset contains", len(df), "rows after cleaning.")
print("- The grouped statistics show differences between categories.")
print("- Visualizations highlight data distribution and trends.")
