import pandas as pd
import matplotlib as plt

#numbers = [[10], [20], [30], [40], [50]]
students = [['john', 'Doe', 90],
            ["ibra", 'Niang', 99],
            ["Fat", "Diop", 75]]
df = pd.DataFrame(students, index=["student 1", "student 2", "student 3"])
print(df)
plt.show(df)