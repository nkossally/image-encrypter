FOUR = 4

def forward_shift(matrix):
    transformed_matrix = []

    for i in range(len(matrix)):
        transformed_matrix.append([])
    
    for j in range(FOUR):
        shift_1 = ((j + 1) + FOUR) % FOUR
        shift_2 = ((j + 2) + FOUR) % FOUR
        shift_3 = ((j + 3) + FOUR) % FOUR

        
        transformed_matrix[0].append(matrix[0][j])
        transformed_matrix[1].append(matrix[1][shift_1])
        transformed_matrix[2].append(matrix[2][shift_2])
        transformed_matrix[3].append(matrix[3][shift_3])

    return transformed_matrix

def backward_shift(matrix):
    transformed_matrix = []

    for i in range(len(matrix)):
        transformed_matrix.append([])
    
    for j in range(FOUR):
        shift_1 = ((j - 1) + FOUR) % FOUR
        shift_2 = ((j - 2) + FOUR) % FOUR
        shift_3 = ((j - 3) + FOUR) % FOUR
        
        transformed_matrix[0].append(matrix[0][j])
        transformed_matrix[1].append(matrix[1][shift_1])
        transformed_matrix[2].append(matrix[2][shift_2])
        transformed_matrix[3].append(matrix[3][shift_3])

    return transformed_matrix



