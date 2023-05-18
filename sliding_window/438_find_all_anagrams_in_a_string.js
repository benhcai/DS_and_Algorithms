var findAnagrams = function (s, p) {
  const ans = [];
  let l = 0;
  let r = 0;

  const pMap = {};
  let curr = {};

  for (const el of p) {
    if (!(el in pMap)) pMap[el] = 0;
    pMap[el]++;
  }

  while (l <= s.length - p.length) {
    if (!(s[r] in pMap)) {
      l = r + 1;
      r = r + 1;
      curr = {};
    } else {
      if (s[r] in pMap) {
        if (!(s[r] in curr)) curr[s[r]] = 0;
        curr[s[r]]++;
      }
      while (r - l > p.length - 1 || curr[s[r]] > pMap[s[r]]) {
        curr[s[l]]--;
        if (curr[s[l]] === 0) delete curr[s[l]];
        l++;
      }
      if (r - l === p.length - 1) {
        let same = true;
        for (el in curr) {
          if (pMap[el] !== curr[el]) {
            same = false;
            break;
          }
        }
        if (same) ans.push(l);
      }
      r++;
    }
  }
  return ans;
};

const s = "bpabacabcbacb";
const p = "aabc";

console.log(findAnagrams(s, p));
