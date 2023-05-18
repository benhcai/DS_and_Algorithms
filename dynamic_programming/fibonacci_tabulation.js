const fib = (n) => {
  const tab = Array(n).fill(0);
  tab[0] = 1;
  tab[1] = 1;
  for (let i = 2; i < tab.length; i++) {
    tab[i] = tab[i - 1] + tab[i - 2];
    console.log(tab[i]);
  }
  return tab[n - 1];
};

console.log(fib(10));
