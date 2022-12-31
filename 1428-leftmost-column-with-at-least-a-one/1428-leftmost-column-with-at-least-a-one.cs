class Solution
    {
    private const int MaxMatrixLength = 100;
    private BinaryMatrix _binaryMatrix;
    private int _rows;
    private int _cols;
    private int _leftmostColumnWithOne = MaxMatrixLength + 1;

    public int LeftMostColumnWithOne(BinaryMatrix binaryMatrixParam)
    {
        _binaryMatrix = binaryMatrixParam;
        _rows = _binaryMatrix.Dimensions()[0];
        _cols = _binaryMatrix.Dimensions()[1];

        var rowsWithOnes = GetRowsWithOnes();

        foreach (var row in rowsWithOnes) BinarySearchRow(row);

        if (_leftmostColumnWithOne == MaxMatrixLength + 1)
            return -1;
        return _leftmostColumnWithOne;
    }

    private HashSet<int> GetRowsWithOnes()
    {
        var rowsWithOnes = new HashSet<int>();
        for (var row = 0; row < _rows; row++)
            if (_binaryMatrix.Get(row, _cols - 1) == 1)
                rowsWithOnes.Add(row);
        return rowsWithOnes;
    }

    private void BinarySearchRow(int row)
    {
        var left = 0;
        var right = _cols - 1;

        while (left <= right)
        {
            var mid = (left + right) / 2;
            if (_binaryMatrix.Get(row, mid) == 1)
            {
                _leftmostColumnWithOne = Math.Min(_leftmostColumnWithOne, mid);
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
                if (left >= _leftmostColumnWithOne)
                    break;
            }
        }
    }
}