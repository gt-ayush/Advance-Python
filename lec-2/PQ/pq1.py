#(1) Store the test results for 5 students over 4 test sessions in a 2-dimensional array,
# with 100 points as the maximum score. Here, axis 0 corresponds to the students, 
# and axis 1 corresponds to the test sessions. The values can be arbitrary.
import numpy as np
test_results = np.array([[85, 90, 78, 92],
                         [88, 91, 82, 89],
                         [95, 87, 93, 88],
                         [82, 94, 86, 90],
                         [91, 89, 95, 87]])
print("Test Results:\n", test_results)