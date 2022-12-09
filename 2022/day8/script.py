from collections import Counter
import numpy as np

def create_forest(file):
    with open(file, 'r') as fs:
        lines = fs.readlines()

    forest = None
    for line in lines:
        line = line.rstrip('\n')
        list_ints = [int(char) for char in line]
        if forest is None:
            forest = np.array(list_ints, dtype=int)
        else:
            forest = np.vstack((forest, list_ints))
    return forest

def calculate_visible_trees(forest):
    # Disclaimer, I'm not a data scientist, sorry about the O(n2) loops
    visible = 0
    for row, tree_row in enumerate(forest):
        for col, tree in enumerate(tree_row):
            # build the views
            view_from_left = tree_row[:col+1]
            view_from_right = tree_row[col:]
            view_from_top = forest[:,col][:row+1]
            view_from_bottom = forest[:,col][row:]

            if (max(view_from_left) == tree 
                and Counter(view_from_left)[tree] == 1
            ):
                visible += 1
            elif (max(view_from_right) == tree
                and Counter(view_from_right)[tree] == 1
            ):
                visible += 1
            elif (max(view_from_top) == tree
                and Counter(view_from_top)[tree] == 1
            ):
                visible += 1
            elif (max(view_from_bottom) == tree
                and Counter(view_from_bottom)[tree] == 1
            ):
                visible += 1
    print("Visible trees : %s" % visible)
    return visible

def view_score(iterable, reverse=False):
    if reverse:
        iterable = np.flip(iterable)
    index = 0
    while index < len(iterable) - 1:
        index += 1
        if iterable[index] >= iterable[0]:
            break    
    return index

def calculate_best_scenic_score(forest):
    top_score = 0
    for row, tree_row in enumerate(forest):
        for col, tree in enumerate(tree_row):
            # build the views
            view_from_left = tree_row[:col+1]
            view_from_right = tree_row[col:]
            view_from_top = forest[:,col][:row+1]
            view_from_bottom = forest[:,col][row:]

            score_left = view_score(view_from_left, reverse=True)
            score_right = view_score(view_from_right)
            score_top = view_score(view_from_top, reverse=True)
            score_bottom = view_score(view_from_bottom)

            tree_score = score_left * score_right * score_top * score_bottom

            if tree_score > top_score:
                top_score = tree_score
    print("Best scenic score : %s" % top_score)
    return top_score            

test_forest = create_forest('test.txt')
assert 21 == calculate_visible_trees(test_forest)
assert 8 == calculate_best_scenic_score(test_forest)

input_forest = create_forest('input.txt')
calculate_visible_trees(input_forest)
calculate_best_scenic_score(input_forest)
