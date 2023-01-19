class Solution
{
    public int GetIndex(ArrayReader reader)
    {
        var l = 0;
        var y = reader.Length() - 1;
        
        while (l < y)
        {
            var third = (y - l) / 3;
            var r = l + third;
            var x = y - third;
            
            switch (reader.CompareSub(l, r, x, y))
            {
                case 0:
                    l = r + 1;
                    y = x - 1;
                    break;
                case 1:
                    y = r;
                    break;
                case -1:
                    l = x;
                    break;
            }
        }
        
        return l;
    }
}