# (2) For each student, calculate the highest score, lowest score, average, and variance across the 4 test sessions. Store the results in a 2-dimensional array where axis 0 corresponds to the students and axis 1 corresponds to the aggregation results (highest score, lowest score, average, variance).
import numpy as np
test_results = np.array([[85, 90, 78, 92],
                         [88, 91, 82, 89],
                         [95, 87, 93, 88],
                         [82, 94, 86, 90],
                         [91, 89, 95, 87]])
highest_scores = np.max(test_results, axis=1)
lowest_scores = np.min(test_results, axis=1)
average_scores = np.mean(test_results, axis=1)
variance_scores = np.var(test_results, axis=1)
print("Highest Scores:\n", highest_scores)
print("Lowest Scores:\n", lowest_scores)
print("Average Scores:\n", average_scores)
print("Variance Scores:\n", variance_scores)

# 3) For each test score, calculate the absolute difference between the score and the student's average score, resulting in a 2-dimensional array with shape (5, 4).

absolute_differences = np.abs(test_results - average_scores[:, np.newaxis])
print("Absolute Differences:\n", absolute_differences)