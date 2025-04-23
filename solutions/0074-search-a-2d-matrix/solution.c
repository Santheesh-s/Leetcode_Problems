bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    for(int i=0;i<matrixSize * *matrixColSize;i++)
    {
        if(matrix[i/ *matrixColSize][i% *matrixColSize]==target)
            return true;
    }
    return false;
}
