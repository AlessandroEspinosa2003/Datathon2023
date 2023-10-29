import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dtypes = {2: str, 6: str}
schem  = {2:str ,8:str}

states = [
    'ALABAMA',
    'ALASKA',
    'ARIZONA',
    'ARKANSAS',
    'CALIFORNIA',
    'COLORADO',
    'CONNECTICUT',
    'DELAWARE',
    'DISTRICT OF COLUMBIA',
    'FLORIDA',
    'GEORGIA',
    'HAWAII',
    'IDAHO',
    'ILLINOIS',
    'INDIANA',
    'IOWA',
    'KANSAS',
    'KENTUCKY',
    'LOUISIANA',
    'MAINE',
    'MARYLAND',
    'MASSACHUSETTS',
    'MICHIGAN',
    'MINNESOTA',
    'MISSISSIPPI',
    'MISSOURI',
    'MONTANA',
    'NEBRASKA',
    'NEVADA',
    'NEW HAMPSHIRE',
    'NEW JERSEY',
    'NEW MEXICO',
    'NEW YORK',
    'NORTH CAROLINA',
    'NORTH DAKOTA',
    'OHIO',
    'OKLAHOMA',
    'OREGON',
    'PENNSYLVANIA',
    'RHODE ISLAND',
    'SOUTH CAROLINA',
    'SOUTH DAKOTA',
    'TENNESSEE',
    'TEXAS',
    'UTAH',
    'VERMONT',
    'VIRGINIA',
    'WASHINGTON',
    'WEST VIRGINIA',
    'WISCONSIN',
    'WYOMING'
]



# Read the CSV file with specified data types
ap_df = pd.read_csv('APCOURSES.csv', header=0, dtype=dtypes)
de_df = pd.read_csv('DualEnrollment.csv', header=0, dtype=dtypes)
t1_df = pd.read_csv('Title1NoStatus.csv', header=0,dtype = schem)
nt1_df = pd.read_csv('Title1Status.csv', header=0,dtype = schem)

ap_df['sch_apenr_ind'] = ap_df['sch_apenr_ind'].map({'Yes': 1, 'No': 0})

# Set the style of the plot
sns.set(style="whitegrid")

# Create a countplot using Seaborn
sns.countplot(data=ap_df, x="lea_state", hue='sch_apenr_ind')

# Set labels for the axes
plt.xlabel("State")
plt.ylabel("Number of Schools")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set a title for the bar graph
plt.title("Number of Schools Offering vs. Not Offering AP Courses in Each State")

# Show the plot
plt.show()

de_df['sch_dual_ind'] = de_df['sch_dual_ind'].map({'Yes':1, 'No':0})


# Merge the two DataFrames on the common column (in this case, "Date")
merged_data = pd.merge(t1_df, nt1_df, on = ['lea_state', 'title_i_status'], how ='inner')

# Extract the columns you want to plot
merged_data['title_i_status'] = merged_data['title_i_status'].map({'Yes':1,'No':0})


# Set the style of the plot
sns.set(style="whitegrid")

# Create a countplot using Seaborn
sns.countplot(data=de_df, x="lea_state", hue='sch_dual_ind')

# Set labels for the axes
plt.xlabel("State")
plt.ylabel("Number of Schools")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set a title for the bar graph
plt.title("Number of schools with Dual Enrollment vs. Not Offering Dual Enrollment in Each State")

# Set the style of the plot
sns.set(style="whitegrid")

# Create a countplot using Seaborn
sns.countplot(data=merged_data, x= 'lea_state', hue='title_i_status')

# Set labels for the axes
plt.xlabel("State")
plt.ylabel("Number of Schools")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Set a title for the bar graph
plt.title("Number of Title 1 Schools vs. Non Title 1 in Each State")

# Show the graph
plt.show()


