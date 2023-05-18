// const Heap = require("./heap_ds");
import { PriorityQueue } from "datastructures-js";
const Heap = PriorityQueue;
const nums = [7, 4, 2, 6, 8, 2, 3, 1];
const heap = new Heap((a: number, b: number) => a - b);
nums.forEach((num) => heap.enqueue(num));
console.log(heap.toArray());
