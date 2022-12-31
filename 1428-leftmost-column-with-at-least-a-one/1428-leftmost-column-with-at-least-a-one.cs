/**
 * // This is BinaryMatrix's API interface.
 * // You should not implement it, or speculate about its implementation
 * class BinaryMatrix {
 *     public int Get(int row, int col) {}
 *     public IList<int> Dimensions() {}
 * }
 */


class Solution
{
    private static int MAX_MATRIX_LENGTH = 100;
    private BinaryMatrix binaryMatrix;
    private int rows;
    private int cols;
    private int leftmostColumnWithOne = MAX_MATRIX_LENGTH + 1;

    public int LeftMostColumnWithOne(BinaryMatrix binaryMatrixParam)
    {
        binaryMatrix = binaryMatrixParam;
        rows = binaryMatrix.Dimensions()[0];
        cols = binaryMatrix.Dimensions()[1];

        var rowsWithOnes = GetRowsWithOnes();

        foreach (var row in rowsWithOnes)
        {
            BinarySearchRow(row);
        }

        if (leftmostColumnWithOne == MAX_MATRIX_LENGTH + 1)
        {
            return -1;
        }
        else
        {
            return leftmostColumnWithOne;
        }
    }

    public HashSet<int> GetRowsWithOnes()
    {
        var rowsWithOnes = new HashSet<int>();
        for (var row = 0; row < rows; row++)
        {
            if (binaryMatrix.Get(row, cols - 1) == 1)
            {
                rowsWithOnes.Add(row);
            }
        }
        return rowsWithOnes;
    }

    public void BinarySearchRow(int row)
    {
        var left = 0;
        var right = cols - 1;

        while (left <= right)
        {
            var mid = (left + right) / 2;
            if (binaryMatrix.Get(row, mid) == 1)
            {
                leftmostColumnWithOne = Math.Min(leftmostColumnWithOne, mid);
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
                if (left >= leftmostColumnWithOne)
                {
                    break;
                }
            }
            {

            }
        }
    }
}