#Initialize matrix a  
a = [[1, 2, 3],  
    [4, 5, 6],  
    [7, 8, 9]]  
   
#Calculates number of rows and columns present in given matrix  
rows = len(a);  
cols = len(a[0]);  
   
#Calculates sum of each row of given matrix  
for i in range(0, rows):  
    sumRow = 0;  
    for j in range(0, cols):  
        sumRow = sumRow + a[i][j];  
    print("Sum of " + str(i+1) +" row: " + str(sumRow));  
   
#Calculates sum of each column of given matrix  
for i in range(0, rows):  
    sumCol = 0;  
    for j in range(0, cols):  
        sumCol = sumCol + a[j][i];  
    print("Sum of " + str(i+1) +" column: " + str(sumCol));

#Calculates sum of diagonal
diagonal=0
for k in range(0,rows):
    diagonal=diagonal+a[k][k]
print("Diagonal sum",diagonal)
