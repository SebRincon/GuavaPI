import pandas as pd

# Read the CSV data
data = pd.read_csv('pinout-description.csv')  # replace 'data.csv' with your csv file path

# Define the initial y coordinate
y_coordinate = -2.7
length = 2.54
old = ''
# Open the output file
with open('output.txt', 'w') as f:
    # TODO: Change length based on pin section
    # Iterate over each row in the data
    for _, row in data.iterrows():
        # Write the formatted string to the file
        current = row['Section']
        if old != current:
          y_coordinate -= 10

        

        f.write(f'''
      (pin output line (at 0 {y_coordinate} 0) (length {length})
        (name "{row['Pin Name']}" (effects (font (size 1.27 1.27))))
        (number "{row['Ball#']}" (effects (font (size 1.27 1.27))))
      )
''')
        # Decrement the y coordinate
        y_coordinate -= 2.54
        y_coordinate = round(y_coordinate, 2)
        old = row['Section']
