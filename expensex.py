import matplotlib.pyplot as plt

def main():
  expenses = [1000, 250, 350, 200, 375, 800]
# Create the slice labels.
  slices_labels = ['Rent', 'Gas', 'Food', 'Clothing', 'Car Payment', 'Misc']
  plt.pie(expenses, labels= slices_labels)
  
  plt.show()
main()