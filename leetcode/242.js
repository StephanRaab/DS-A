isAnagram(s, t) {
    if (s.length !== t.length) return false;

    const freq = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++){
        freq[s.charCodeAt(i)-97]++; //charcodes from a-z are 97-122, so if we -97, we get the index
        freq[t.charCodeAt(i)-97]--;
    }

    return freq.every(c => c === 0);
};