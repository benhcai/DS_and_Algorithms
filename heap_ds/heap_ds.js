"use strict";
exports.__esModule = true;
var Heap = /** @class */ (function () {
    function Heap(values) {
        this.nodes = Array.isArray(values) ? values : [];
    }
    Heap.prototype.toArray = function () {
        return Array.from(this.nodes);
    };
    Heap.prototype.size = function () {
        return this.nodes.length;
    };
    Heap.prototype._hasLeftChild = function (parentIndex) {
        var leftChildIndex = parentIndex * 2 + 1;
        return leftChildIndex < this.size();
    };
    return Heap;
}());
exports["default"] = Heap;
