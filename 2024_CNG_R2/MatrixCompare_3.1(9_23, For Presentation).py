
# Brendan Hall

#use python 3.7 Mac pro

import numpy as np
import sys
import warnings

warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
np.set_printoptions(linewidth=300)

# PrintYN = "Y"
# #PrintYN = input("Print full output: Y/N or Q to Quit:\n")
# #This will allow user to see all matricies as outputs or quit the program
# if PrintYN == "Q":
#     quit()

def sizeroller():
    global x2
    global x1
    global y2
    global y1
    global toprun
    global overrun

    x1 = 1
    x2 = 1
    y1 = 1
    y2 = 1

    for j in range(10):

        for i in range(10):

            for l in range(10):

                for k in range(10):
                    generateInitial(x1+j, x2+i, y1+l, y2+k)
                    run(x1+j, x2+i, y1+l, y2+k)

def print2file(PD):
    original_stdout = sys.stdout  # Save a reference to the original standard output

    with open(f"{x2}x{x1}_{y2}x{y1}.txt", 'a') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print(PD)
        sys.stdout = original_stdout  # Reset the standard output to its original value

def generateInitial(groundLength,groundHeight,figureLength,figureHeight):
  global Y
  global X

  X = np.full((30, 30), 0.2)
  Y = np.full((30, 30), 2.0)

  X = generateGround(X,groundLength,groundHeight)
  Y = generateFigure(Y,figureLength+1,figureHeight+1)

  a = {"Ground": X, "Figure": Y}

  return a

def generateGround(field,length,height):
  for i in range(30):
    for j in range(30):
      if j >= 11 and j < 11 + length:
        if i >= 11 and i < 11 + height:
          field[i][j] = .1
          if i != 11 and i != 10 + height and j != 11 and j != 10 + length:
            field[i][j] = 0
  return field

def generateFigure(field,length,height):
  for i in range(30):
    for j in range(30):
      if j > 30 - length:
        if i > 30 - height:
          field[i][j] = 1
          if i != 29 and i != 31 - height and j != 29 and j != 31 - length:
            field[i][j] = 0
  return field

def matchmatrix(result,ID,P,Q,R,S,x1,x2,y1,y2):

    MatrixData = {'001001111': 'a',
    '000001011': 'b',
    '000001111': 'c',
    '001001011': 'd',
    '001011111': 'e',
    '011111111': 'f',
    '110111011': 'g',
    '111111111': 'h',
    '010111011': 'i',
    '101011111': 'j',
    '100011011': 'k',
    '000011011': 'l',
    '110111111': 'm',
    '010111111': 'n',
    '011111011': 'o',
    '111111011': 'p',
    '100111111': 'q',
    '100011111': 'r',
    '101011011': 's',
    '111011011': 't',
    '100111011': 'u',
    '000111011': 'v',
    '010011011': 'w',
    '110011011': 'x',
    '111011111': 'y',
    '110011111': 'z',
    '101111011': 'aa',
    '101111111': 'ab',
    '011011111': 'ac',
    '010011111': 'ad',
    '001111011': 'ae',
    '001111111': 'af',
    '000011111': 'ag',
    '000111111': 'ah',
    '011011011': 'ai',
    '001011011': 'aj',
    '100110111': 'ak',
    '000110111': 'al',
    '011011001': 'am',
    '111011001': 'an',
    '000010011': 'ao',
    '000110011': 'ap',
    '010011001': 'aq',
    '000011001': 'ar',
    '100110011': 'as',
    '000010111': 'at',
    '001011001': 'au',
    '110011001': 'av',
    '100010111': 'aw',
    '100011001': 'ax',
    '100010011': 'ay',
    '101011001': 'az',
    '100100111': 'ba',
    '000100111': 'bb',
    '011001001': 'bc',
    '111001001': 'bd',
    '100100011': 'be',
    '000100011': 'bf',
    '010001001': 'bg',
    '110001001': 'bh',
    '100010001': 'bi',
    '000010001': 'bj'}

        # MatrixDataframe = pd.DataFrame(MatrixData, columns=["IntMatrix", "ID"])

    result_array = np.array(result)

    ID_array = np.array(ID)
    P = np.array(P)
    Q = np.array(Q)
    R = np.array(R)
    S = np.array(S)
    x1 = np.array(x1)
    x2 = np.array(x2)
    y1 = np.array(y1)
    y2 = np.array(y2)

    s = "".join(str(x) for x in result_array)

    if s in MatrixData:
        second_value = MatrixData[s]
        result_ID_array = np.hstack((second_value, ID_array, 30 - Q - y2, 30 - P - y1, x2, x1, y2, y1))
        print2file(result_ID_array)
    else:
        result_ID_array = np.hstack((str(s), ID_array, 30 - Q - y2, 30 - P - y1, x2, x1, y2, y1))
        #MatrixData[s] = 'Z'
        print2file(result_ID_array)

    return result, ID

# CSV_Output_name=(f"{x2}x{x1}_{y1-1}x{y2-1}.csv")

# These arrays are appended to the bottom and end respectively to 'move' the dynamic array

# This function updates the blank intersection matrix with the corresponding element of the nine-intersection matrix

def intersectionarray(unique_result):

    for row in unique_result:
        if np.all(row == 0):
            # print("0.0 found")
            Int_Matrix[0, 0] = 1

    for row in unique_result:
        if np.all(row == .1):
            # print("0.1 found")
            Int_Matrix[1, 0] = 1

    for row in unique_result:
        if np.all(row == .2):
            # print("0.2 found")
            Int_Matrix[2, 0] = 1

    for row in unique_result:
        if np.all(row == 1.0):
            # print("1.0 found")
            Int_Matrix[0, 1] = 1

    for row in unique_result:
        if np.all(row == 1.1):
            # print("1.1 found")
            Int_Matrix[1, 1] = 1

    for row in unique_result:
        if np.all(row == 1.2):
            # print("1.2 found")
            Int_Matrix[2, 1] = 1

    for row in unique_result:
        if np.all(row == 2.0):
            # print("2.0 found")
            Int_Matrix[0, 2] = 1

    for row in unique_result:
        if np.all(row == 2.1):
            # print("2.1 found")
            Int_Matrix[1, 2] = 1

    for row in unique_result:
        if np.all(row == 2.2):
            # print("2.2 found")
            Int_Matrix[2, 2] = 1

# This section runs the iterations / movement of the dynamic array and calls the intersectionarray
# function to update the blank intersection array matrix with unique results as they occur

def run(x1, x2, y1, y2):
    global Y
    global X
    global toprun
    global overrun
    global unique_result
    global Int_Matrix

    Int_Matrix = np.array([

        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ])
    toprun = y1 - 0
    overrun = y2 - 0

    horizontal_array_update = np.full((1, 30), 2)

    vertical_array_update = np.full((30, 1), 2)

    base_array = [
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
         0.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    iteration_id = 1
    horz_comp = 1

    empty_array = np.array([])
    empty_array2 = np.array([])

    NewY = Y

    for P in range(len(X) - toprun):                                    # prevents top overrun
    # for P in range(len(X)):
        for Q in range(len(Y) - overrun):                               # prevents left overrun
        # for Q in range(len(Y)):
            for R in range(len(X)):

                for S in range(len(X[0])):                              # changing to len(X) missing [0] adds
                                                                       # intersection, possible erroneous?
                    base_array[R][S] = X[R][S] + Y[R][S]                # adds two matrices together
                    # print(P, R)
            # if PrintYN == "Y":                                          # handles printing preference
            #     print("\nWhole Matrix:", iteration_id)
            #
            # for r in base_array:
            #     if PrintYN == "Y":                                      # handles printing preference
            #         print(r)

            unique_result = np.unique(base_array)

            intersectionarray(unique_result)

            s = Int_Matrix.flatten().tolist()

            matchmatrix(s, iteration_id, P, Q, R, S, x1, x2, y1, y2)

            empty_array = np.append(empty_array, [Int_Matrix])

            # if PrintYN == "Y":                                          # handles printing preference
            #     print("\nIntersection Matrix:\n")
            #     print(Int_Matrix)
            #     print("\nEnd of Matrix Comparison:", iteration_id)

            iteration_id += 1
            if not np.array_equal(Int_Matrix, unique_result):

                empty_array2 = np.append(empty_array2, [Int_Matrix, P, Q, iteration_id])

            Int_Matrix = np.array([
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ])

            Y = np.delete(Y, 0, 1)
            Y = np.append(Y, vertical_array_update, axis=1)

        Y = NewY

        # if PrintYN == "Y":                                              # handles printing preference
        #     print("\nEnd of horizontal comparison: ", horz_comp)

        horz_comp += 1
        NewY = np.delete(NewY, 0, 0)
        NewY = np.append(NewY, horizontal_array_update, axis=0)

        Y = np.delete(Y, 0, 0)
        Y = np.append(Y, horizontal_array_update, axis=0)

sizeroller()








# This section creates list of unique 9-intersection results
#
# D = list(empty_array)                                               # updated all intersections
# Q = 9                                                               # grouping size
# E = [D[i:i + Q] for i in range(0, len(D), Q)]                       # probably a much easier way to group values
# T = Counter(map(tuple, E))                                          # probably a much easier way to find unique values
# U = list(T)                                                         # probably a much easier way to find unique values
#


# print(empty_array)
# print(empty_array2)

# This section handles reading in the matrix definitions and getting the dataframes ready to merge based on common field

# MatrixDict = pd.read_table("512matrices_dict_2.1.txt", dtype=str)   # creates DF of matrix definitions
#
# UU = pd.DataFrame(U)                                                # creates DF out of unique results
# #print(UU)
# UU.to_csv(CSV_Output_name + " Unique")                              # outputs unique results to csv (does not truncate 0's)
#
# UU_1 = UU.astype(int)                                               # converts UU DF to include type integers
# UU_2 = UU_1.astype(str)                                             # converts UU_1 to string (had trouble preserving 0's
#                                                                     # and this fixed it)
#
# # This concatenates unique results in nine columns into single string in one column
#
# UU_conc = UU_2[0]+UU_2[1]+UU_2[2]+UU_2[3]+UU_2[4]+UU_2[5]+UU_2[6]+UU_2[7]+UU_2[8]
#
# UU_3 = pd.DataFrame(UU_conc)
# UU_3.columns = ["IntMatrix"]                                        # adds column header necessary for pd.merge
# print("\nThe number of unique intersections:", len(UU_3))
# print("\nUnique Results: \n")



# MatrixMerge = pd.merge(left=MatrixDict, right=UU_3, left_on='IntMatrix', right_on='IntMatrix')
# print(MatrixMerge)
# #print2file(MatrixMerge)
#
# UU_4 = MatrixMerge.astype(str)
#
# UU_4.to_csv(CSV_Output_name + " Merged")
#
# print("\nMatrices:", CSV_Output_name[:-4])
#
# format = ['%s']
# np.savetxt('output.csv', empty_array2, delimiter=',',fmt=format)

#matchmatrix(U)

#%%

#%%
