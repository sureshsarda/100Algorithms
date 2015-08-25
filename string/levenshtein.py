def printMatrix(matrix):
    len1 = len(matrix)
    len2 = len(matrix[0])
    
    for i in range(0, len1):
        for j in range(0, len2):
            print matrix[i][j],
        print ""

def levenshtein(str1, str2):
    print "String One:", str1
    print "String Two:", str2
    print "Calculating Edit Distance..."

    len1 = len(string1)
    len2 = len(string2)

    # 1 more than length to accomodate the extra values of plain insertion and deletions
    matrix = [[0 for x in range(len2 + 1)] for x in range(len1 + 1)]
    
    # First column
    for i in range(len1 + 1):
        matrix[i][0] = i
    
    # First Row    
    for j in range(len2 + 1):
        matrix[0][j] = j

    # The main matrix, starts at 1,1 and ends at len
    for i in range(len1):
        for j in range(len2):
            if str1[i] == str2[j]:
                matrix[i + 1][j + 1] = matrix[i][j] # Copy the diagonal element as it is
            else:
                matrix[i + 1][j + 1] = min([matrix[i][j + 1] + 1, matrix[i + 1][j] + 1, matrix[i][j] + 1])

#   printMatrix(matrix)        

    costlist = []
    for i in range(len1 + 1):
        costlist.append(matrix[i][len2])
    costlist = costlist + matrix[len1]

    return min(costlist)

string1 = "iterative"
string2 = "irr"

distance = levenshtein(string1, string2)
print "Edit distance is ", distance
