import pandas as pd

# Read the CSV data
data = pd.read_csv('pinout-description.csv')  # replace 'data.csv' with your csv file path

# Define the initial y coordinate
y_coordinate = -12.7

# Open the output file
with open('output.txt', 'w') as f:
    # Iterate over each row in the data
    for _, row in data.iterrows():
        # Write the formatted string to the file
        f.write(f'''
      (pin output line (at 0 {y_coordinate} 0) (length 2.54)
        (name "{row['Pin Name']}" (effects (font (size 1.27 1.27))))
        (number "{row['Ball#']}" (effects (font (size 1.27 1.27))))
      )
''')
        # Decrement the y coordinate
        y_coordinate -= 2.54
        y_coordinate = round(y_coordinate, 2)
