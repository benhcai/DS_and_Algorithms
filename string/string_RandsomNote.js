function determineValidRandsomNote(randsomNote, magazine) {
  const rnFreq = {};
  for (let i = 0; i < randsomeNote.length; i++) {
    if (!(randsomeNote[i] in rnFreq)) rnFreq[randsomeNote[i]] = 0;
    rnFreq[randsomeNote[i]]++;
  }

  const magazineFreq = {};
  for (let i = 0; i < magazine.length; i++) {
    if (!(magazine[i] in magazineFreq)) magazineFreq[magazine[i]] = 0;
    magazineFreq[magazine[i]]++;
  }

  for (const el in randsomNote) {
    if (magazineFreq[el] < rnFreq[el]) return false;
    if (!(el in magazineFreq)) return false;
  }
  return true;
}

// Take time to look over the solution at the end then consider if you can improve it.
// Check in with the interviewer "How does this sound to you"
// Be clear when going over test case
// Be less awkward, make a joke?`
