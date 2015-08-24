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
    
    matrix = [[0 for x in range(len1)] for x in range(len2)]
    
    for i in range(0, len1):
        matrix[0][i] = i
    
    for j in range(0, len2):
        matrix[j][0] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i] == str2[j]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                print i, j
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + 1)

    printMatrix(matrix)

string1 = "iterative"
string2 = "irretative"

levenshtein(string1, string2)
