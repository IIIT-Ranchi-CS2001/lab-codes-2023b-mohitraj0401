import os
import pandas as pd
import matplotlib.pyplot as plt

election_data = [
    ['Madhya Pradesh', 'BJP', 163, 230, 72.1],
    ['Madhya Pradesh', 'INC', 66, 230, 72.1],
    ['Madhya Pradesh', 'BSP', 0, 230, 72.1],
    ['Madhya Pradesh', 'Others', 1, 230, 72.1],
    ['Rajasthan', 'BJP', 115, 200, 74.2],
    ['Rajasthan', 'INC', 69, 200, 74.2],
    ['Rajasthan', 'BSP', 2, 200, 74.2],
    ['Rajasthan', 'Others', 13, 200, 74.2]
]

file_path = 'election_data.csv'

if not os.path.exists(file_path):
    try:
        df = pd.DataFrame(election_data, columns=['State', 'Party', 'Seats_Won', 'Total_Seats', 'Voter_Turnout'])
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error writing to file: {e}")
else:
    print("File already exists.")

try:
    df = pd.read_csv(file_path)
except Exception as e:
    print(f"Error reading the file: {e}")

try:
    df['Seats_Percentage'] = (df['Seats_Won'] / df['Total_Seats']) * 100
except Exception as e:
    print(f"Error calculating seats percentage: {e}")

try:
    highest_seats_party = df.loc[df.groupby('State')['Seats_Won'].idxmax()]
    print("\nParty with highest seats in each state:")
    print(highest_seats_party[['State', 'Party', 'Seats_Won']])
except Exception as e:
    print(f"Error determining the party with highest seats: {e}")

try:
    plt.figure(figsize=(10, 6))
    for state in df['State'].unique():
        state_data = df[df['State'] == state]
        plt.bar(state_data['Party'], state_data['Seats_Won'], label=state)
    plt.xlabel('Party')
    plt.ylabel('Seats Won')
    plt.title('Number of Seats Won by Each Party in Each State')
    plt.legend(title='State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Error creating the bar chart: {e}")
