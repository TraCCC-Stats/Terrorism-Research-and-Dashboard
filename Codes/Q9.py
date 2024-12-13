import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency




# Load the incidents dataset
incidents_df = pd.read_csv(r"E:\Zeeshan Graduate Studies\04- Last Semester\GMU TraCCC - Terrorism Research and Dashboard\Terrorism-Research-and-Dashboard\Data\20241019-GRID_INCIDENTS.csv")

# Inspect the first few rows to understand structure
print(incidents_df.head())


print(incidents_df.columns)


# Question 8: Analyze correlation between perpetrator types and tactics used
# Selecting relevant columns (adjust column names as needed)
data_perp_tactic = incidents_df[['perpetrator_column', 'tactic_column']]






import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Load the incidents dataset
incidents_df = pd.read_csv(r"E:\Zeeshan Graduate Studies\04- Last Semester\GMU TraCCC - Terrorism Research and Dashboard\Terrorism-Research-and-Dashboard\Data\20241019-GRID_INCIDENTS.csv")

# Set option to display all columns
pd.set_option('display.max_columns', None)

# Inspect the first few rows to understand structure
print(incidents_df.head())

# Print all column names
print(incidents_df.columns)