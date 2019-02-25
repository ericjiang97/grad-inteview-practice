# Hash Tables

The hash table is a collection of elements, when the index of the item is determined by its' _hash function_.

for example.

```python
hash = hashFunction(key)
# position to insert
index = hash % array_size
```

## Resolving Conflicts

Sometimes, when the hash function is not as 'perfect', we will see collisions - when 2 elements in an array collide with one another.
We can:

- insert at the next available index
- insert at the next available (probing) - `newHash = hashFunction(oldHash)`
- make an array at the index, and insert to the end of that index.
- round robin (using 2 hash functions, and choosing best position to insert)
- double hashing - `hashFunc(hashFunc(key))`
