import matplotlib.pyplot as plt

# ranking data
students = ['Student A', 'Student B', 'Student C', 'Student D']
march_ranks = [1, 1, 3, 2]
april_ranks = [4, 3, 4, 3]
may_ranks = [3, 4, 2, 4]
june_ranks = [2, 2, 1, 1]

# make charts
plt.figure(figsize=(10, 6))

for i, student in enumerate(students):
    plt.plot(['March', 'April', 'May', 'June'], [march_ranks[i], april_ranks[i], may_ranks[i], june_ranks[i]], marker='o', label=student)

# add title
plt.title('Ranking Changes of Students Over Time')
plt.xlabel('Month')
plt.ylabel('Rank')
plt.legend()
plt.grid(True)

# show chart
plt.show()
