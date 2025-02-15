    public string RemoveTrailingZeros(string num) {
        if (string.IsNullOrEmpty(num)) return null;          

        var result = "";

        for (int i = num.Length-1; i >= 0;i--) {
            if (num[i] != '0'){
                result = num.Substring(0, i+1);
                break;
            }
        }

        return result;
    }