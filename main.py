
## Name: Lal Mawia 
## Date: 04/13/2025

import statistics

def processData(week_6_Lab):
  try:
    
    with open(week_6_Lab, "r") as f: 
      monthName = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

      income_values = []

      print("Monthly Income in 2025")
      print("_________________________\n")
      print()  

      for month, line in zip(monthName, f):
        item = float(line.strip())
        income_values.append(item)
        print(f"${month}: ${item:,.2f}")


      average = statistics.mean(income_values)
      stdev = statistics.stdev(income_values)

      print()
      print(f"Average Monthly Income: ${average:,.2f}")
      print(f"Standard Deviation: ${stdev:,.2f}")

  except FileNotFoundError: 
    print(f"Error: The file was not found.")
  except IOError: 
    print("Error: There was a problem with reading the file.")

processData("week_6_Lab/data_file.txt")


  