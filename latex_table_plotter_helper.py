# import this file or the function in this file into your python files to use it
# 1.0 version

# a typical latex table
"""
\begin{center}
\begin{tabular}{ c c c }
 cell1 & cell2 & cell3 \\
 cell4 & cell5 & cell6 \\
 cell7 & cell8 & cell9
\end{tabular}
\end{center}
"""

def convertArrayToLatexTable(A):
    # input is an 2-d array
    start = "\\begin{center}\n\\begin{tabular}{"
    cellCountPart = ""

    R = len(A)
    C = len(A[0])
    for c in range(C):
        cellCountPart += " c "
    start += cellCountPart
    start += "}\n"

    lines = []
    for r in range(R):
        newLine = []
        for c in range(C):
            newLine.append(str(A[r][c]))
        newLineString = "&".join(newLine)
        newLineString+="\\\\"
        lines.append(newLineString)

    endPart = "\\end{tabular}\n\\end{center}"
    final = start + "\n".join(lines) +"\n"+ endPart
    return final


def testLatexTableConvertProgram():
    anArray = [[2,3],[4,5],[1,6]]
    X = convertArrayToLatexTable(anArray)
    print(X)

testLatexTableConvertProgram()