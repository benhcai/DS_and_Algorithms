import { MinPriorityQueue } from "datastructures-js";

console.clear();
var topKFrequent = function (nums: number[], k: number): number[] {
  // init a freq table
  // init a min heap
  // loop through nums to create freq table
  // loop through k keys of freq table to setup heap
  // loop through rest of freq table to produce result heap

  const freq: { [key: number]: number } = {};
  const minpq = new MinPriorityQueue<number>();

  for (const el of nums) {
    freq[el] = el in freq ? ++freq[el] : 1;
  }

  for (const el in freq) {
    if (minpq.size() < k) {
      minpq.enqueue(parseInt(el));
    } else {
      if (freq[el] > freq[minpq.front()]) {
        minpq.dequeue();
        minpq.enqueue(parseInt(el));
      }
    }
  }

  return minpq.toArray();
};

const nums = [1, 1, 1, 2, 2, 3];
const k = 2;
const ans = topKFrequent(nums, k);
console.log(ans);
