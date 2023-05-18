type Value = number | string | object;

interface CompareType {
  (a: any, b: any): number;
}

interface HeapType {
  toArray: () => any[];
  push: (value: Value) => this;
  pop: () => null | Value;
  root: () => null | Value;
}

class Heap implements HeapType {
  public nodes;
  private compare;

  constructor(compare: CompareType, values: Value[]) {
    this.compare = compare;
    this.nodes = Array.isArray(values) ? values : [];
  }

  public toArray() {
    return Array.from(this.nodes);
  }

  public push(value: any) {
    this.nodes.push(value);
    this.heapifyUp(this.size() - 1);
    return this;
  }

  public size() {
    return this.nodes.length;
  }

  private heapifyUp(startIndex: number) {
    let childIndex = startIndex;
    let parentIndex = this.getParentIndex(childIndex);
    while (this.shouldSwap(parentIndex, childIndex)) {
      this.swap(parentIndex, childIndex);
      childIndex = parentIndex;
      parentIndex = this.getParentIndex(childIndex);
    }
  }

  private getParentIndex(childIndex: number) {
    return Math.floor((childIndex - 1) / 2);
  }

  private shouldSwap(parentIndex: number, childIndex: number) {
    if (parentIndex < 0 || parentIndex >= this.size()) return false;
    if (childIndex < 0 || childIndex >= this.size()) return false;
    const parentNode = this.nodes[parentIndex];
    const childNode = this.nodes[childIndex];
    return this.compare(parentNode, childNode) > 0;
  }

  private swap(indexA: number, indexB: number) {
    const temp = this.nodes[indexA];
    this.nodes[indexA] = this.nodes[indexB];
    this.nodes[indexB] = temp;
  }

  public pop() {
    if (this.isEmpty()) return null;
    const root = this.root();
    this.nodes[0] = this.nodes[this.size() - 1];
    this.nodes.pop();
    this.heapifyDown(0);
    return root;
  }

  private isEmpty() {
    return this.size() === 0;
  }

  public root() {
    return this.nodes[0];
  }

  private heapifyDown(startIndex: number) {
    let parentIndex = startIndex;
    let childIndex = this.compareChildrenOf(parentIndex);
    while (this.shouldSwap(parentIndex, childIndex)) {
      this.swap(parentIndex, childIndex);
      parentIndex = childIndex;
      childIndex = this.compareChildrenOf(parentIndex);
    }
  }

  private compareChildrenOf(parentIndex: number) {
    if (!this.hasLeftChild(parentIndex) && this.hasRightChild(parentIndex)) return -1;

    const leftChildIndex = parentIndex * 2 + 1;
    const rightChildIndex = parentIndex * 2 + 2;

    if (!this.hasLeftChild(parentIndex)) return rightChildIndex;
    if (!this.hasRightChild(parentIndex)) return leftChildIndex;

    const leftChildNode = this.nodes[leftChildIndex];
    const rightChildNode = this.nodes[rightChildIndex];
    const compare = this.compare(rightChildNode, leftChildNode);
    return compare > 0 ? rightChildIndex : leftChildIndex;
  }

  private hasLeftChild(parentIndex: number) {
    const leftChildIndex = parentIndex * 2 + 1;
    return leftChildIndex < this.size();
  }

  private hasRightChild(parentIndex: number) {
    const rightChildIndex = parentIndex * 2 + 2;
    return rightChildIndex < this.size();
  }
}

export default Heap;
