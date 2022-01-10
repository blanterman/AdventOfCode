def process_point(all_points, points_count, point):
    if point not in all_points:
        all_points.append(point)
        points_count.append(1)
    else:
        points_count[all_points.index(point)] = points_count[all_points.index(point)] + 1
    return all_points, points_count

# Add the points of a diagonal line
def add_diag_points(end_points, all_points, points_count):
    # Line going to the left up or down
    if end_points[0][0] > end_points[1][0]:
        # Line going to the left down
        if end_points[0][1] > end_points[1][1]:
            x_val = end_points[1][0]
            for val in range(end_points[1][1], end_points[0][1] + 1):
                k = [x_val, val]
                all_points, points_count = process_point(all_points, points_count, k)
                x_val = x_val + 1
        # Line going to the left and up
        if end_points[0][1] < end_points[1][1]:
            x_val = end_points[0][0]
            for val in range(end_points[0][1], end_points[1][1] + 1):
                k = [x_val, val]
                all_points, points_count = process_point(all_points, points_count, k)
                x_val = x_val - 1
    # Line going to the right up or down
    if end_points[0][0] < end_points[1][0]:
        # Line going to the right down
        if end_points[0][1] > end_points[1][1]:
            x_val = end_points[1][0]
            for val in range(end_points[1][1], end_points[0][1] + 1):
                k = [x_val, val]
                all_points, points_count = process_point(all_points, points_count, k)
                x_val = x_val - 1
        # Line going to the right and up
        if end_points[0][1] < end_points[1][1]:
            x_val = end_points[0][0]
            for val in range(end_points[0][1], end_points[1][1] + 1):
                k = [x_val, val]
                all_points, points_count = process_point(all_points, points_count, k)
                x_val = x_val + 1
    return all_points, points_count

# Add the points of a horizontal or vertical line
def add_hv_points(end_points, all_points, points_count):
    # Vertical Line
    if end_points[0][0] == end_points[1][0]:
        if end_points[0][1] <= end_points[1][1]:
            for val in range(end_points[0][1], end_points[1][1] + 1):
                k = [end_points[0][0], val]
                all_points, points_count = process_point(all_points, points_count, k)
        else:
            for val in range(end_points[1][1], end_points[0][1] + 1):
                k = [end_points[0][0], val]
                all_points, points_count = process_point(all_points, points_count, k)
    # Horizontal Line
    if end_points[0][1] == end_points[1][1]:
        if end_points[0][0] <= end_points[1][0]:
            for val in range(end_points[0][0], end_points[1][0] + 1):
                k = [val, end_points[1][1]]
                all_points, points_count = process_point(all_points, points_count, k)
        else:
            for val in range(end_points[1][0], end_points[0][0] + 1):
                k = [val, end_points[1][1]]
                all_points, points_count = process_point(all_points, points_count, k)
    return all_points, points_count


# Read data into a list and clean up the data
with open("5_1_test.txt", "r") as data:
    data_list = data.read().splitlines()
all_end_points = []
# Clean up the data to a list of lists of two line end points
for item in data_list:
    end_points = []
    end_points.append(item.split(" -> "))
    new_end_points = []
    for end_point in end_points:
        for point in end_point:
            temp_point = point.split(",")
            temp_point_ints = list(map(int, temp_point))
            new_end_points.append(temp_point_ints)
    all_end_points.append(new_end_points)
#print(all_end_points)
print("Processing all lines")

all_points = []
points_count = []

# Go through all the lists of end points, get all the lines of the points
# put the points in a list with a seperate list of how many of those points have
# been found. Then print out how many of the points have a count of 2 or more
for end_points in all_end_points:
    if end_points[0][0] == end_points[1][0] or end_points[0][1] == end_points[1][1]:
        all_points, points_count = add_hv_points(end_points, all_points, points_count)
    else:
        all_points, points_count = add_diag_points(end_points, all_points, points_count)
#for index in range(len(all_points)):
#    print("point: {}, count: {}.".format(all_points[index], points_count[index]))
more_than_one = 0
for element in points_count:
    if element >= 2:
        more_than_one = more_than_one + 1
print("{} points have 2 or more lines crossing them.".format(more_than_one))
