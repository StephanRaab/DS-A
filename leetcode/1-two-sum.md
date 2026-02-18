# Two Sum

- We assume **exactly one solution** exists.
- We can **not** use the same element twice.
- Return the answer with the **smaller index first**. *(Worth pointing out: some variants require this, while LeetCode lets you return in **any** order.)*

*Below are a few of the approaches that I went through, starting with the easiest brute force method and working up to the optimal one-pass hash lookup.*

---

## Solution 1: Easiest (Brute Force)

```js
for (let i = 0; i < nums.length; i++) {
  for (let j = i + 1; j < nums.length; j++) {
    if (nums[i] + nums[j] === target) {
      return [i, j];
    }
  }
}
```

This is the clear brute force approach: try every pair of numbers and return the first pair that adds up to `target`.

**Time**: O(n²), **Space**: O(1)

---

## Solution 2: Double Pass (Hash Table / Lookup)

```js
const numberToIndex = Object.create(null);

// build the lookup (number -> index)
for (let i = 0; i < nums.length; i++) {
  numberToIndex[nums[i]] = i;
}

// search using the lookup
for (let i = 0; i < nums.length; i++) {
  const targetNum = target - nums[i];

  // must exist AND can't be the same element
  if (Object.hasOwn(numberToIndex, targetNum) && numberToIndex[targetNum] !== i) {
    const j = numberToIndex[targetNum];
    return [Math.min(i, j), Math.max(i, j)];
  }
}
```

1. We first initialize a lookup object (number -> index)
2. Loop over the numbers and store them as `key/value` pairs:
   - key = the number  
   - value = its index  

   Example:

   `nums = [5, 4, 6], target = 10`

   ```js
   numberToIndex = {
     5: 0,
     4: 1,
     6: 2
   }
   ```

3. Now that we have the lookup built, we loop over `nums` again.
4. For each `nums[i]`, compute the complement we need:

   `targetNum = target - nums[i]`

5. If that complement exists in the lookup (and it’s not the same index), return the pair.
6. Since the second index *can* be before or after `i` in the double-pass approach, we return `[min(i, j), max(i, j)]` to enforce **“smaller index first.”**

> **Reminder**: `numberToIndex[4]` returns the index where `4` occurs (e.g. `1`).  
> **Note on duplicates**: if a number appears more than once, the lookup stores the most **recent** index for that number. That’s okay in this case because we only need any valid pair.

**Time**: O(n) (build) + O(n) (search) → O(n), **Space**: O(n)

---

## Solution 3: Single Pass (One Loop, Same Lookup)

*We finally made it to the single pass version. Hopefully with the earlier knowledge, these small tweaks won't be too much of a lift.*

```js
const numberToIndex = Object.create(null);

for (let i = 0; i < nums.length; i++) {
  const targetNum = target - nums[i];

  // if we've already seen the complement, we're done
  if (Object.hasOwn(numberToIndex, targetNum)) {
    return [numberToIndex[targetNum], i];
  }

  // otherwise, store this number for future lookups
  numberToIndex[nums[i]] = i;
}
```

1. Very similar to the double pass solution, but a bit more “clever”.
1. In a single loop, we check first and then store the current number’s index.
1. The key idea: when we’re at index `i`, the lookup contains only numbers from indices `< i`.
1. **Important**: storing `numberToIndex[nums[i]] = i` must happen *after* the check, otherwise we could accidentally match the same element with itself.

> Since the lookup only contains earlier indices, this naturally returns the **smaller index first**.

**Time**: O(n), **Space**: O(n)

---

## Solution 4: Map Bonus

```js
const numberToIndex = new Map();

for (let i = 0; i < nums.length; i++) {
  const targetNum = target - nums[i];

  if (numberToIndex.has(targetNum)) {
    return [numberToIndex.get(targetNum), i];
  }

  numberToIndex.set(nums[i], i);
}
```

*Lol, no one is going to read this far...*

This is basically Solution 3, but `Map` gives you cleaner membership checks (`has`) and avoids key string-coercion.

> Same reason as Solution 3: the value you get from the map is always from an earlier index, so this returns the **smaller index first**.

**Time**: O(n), **Space**: O(n)

---

## Random Implementation Notes (Object vs `Map`)

You’ll often see this problem solved using either a plain object (`{}`) or a JavaScript `Map`. Both work.

### Why `Object.create(null)` instead of `{}`?

In the example we used:

```js
const numberToIndex = Object.create(null);
```

instead of `{}`, because `{}` inherits from `Object.prototype`, meaning it comes with built-in keys like `toString`, `constructor`, and edge cases like `__proto__`.

`Object.create(null)` creates a “pure” dictionary with no prototype, which makes it a safer lookup table. *(Though in reality it probably doesn't matter here at all, just wanted to share.)*

### Why `Object.hasOwn(...)` instead of `!== undefined`?

You'll sometimes see:

```js
if (numberToIndex[targetNum] !== undefined) { ... }
```

That works for this problem, but `Object.hasOwn(...)` is a more reliable way to check whether the key actually exists on the object:

```js
if (Object.hasOwn(numberToIndex, targetNum)) { ... }
```

If you use a `Map`, as we saw in our secret 4th solution, this becomes even cleaner:

```js
if (map.has(targetNum)) { ... }
```

---

## The End

*Thank you for coming to my Ted Talk*