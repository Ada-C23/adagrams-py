### Comment on lines +62 to +74 
I love that you created a helper function that will create a frequency dictionary out of any list! This syntax works and is one of the classic methods to create a frequency dictionary that you will see!

That being said, there's an even simpler way that doesn't include any conditionals at all! If we did something like:

```
for character in array:
      make_dict[character] = make_dict.get(character, 0) + 1
```

We can create a frequency dictionary just as easily!

### Comment on lines +91 to +93 
This is a great way to create our "pile" of all the letters that does a great job of accounting for the distribution of different letters. The nested for loop isn't always the best approach however. I wonder if there's a way to use the `extend()` method here instead.

What does the number 10 represent here? Bare literals like the 10 here are called **"magic numbers"**, because they just appear out of nowhere. While describing the number in a comment can help understand the number's purpose, it doesn't address their lack of maintainability. When we have magic numbers in our code, if we ever need to change the number (say we want to have a different hand size), we need to track down all occurrences of that number and change it. This is usually more complicated than a search and replace, since there is a high likelihood that there may be occurrences of the magic number unrelated to our particular use (e.g., the number 10 could easily appear in other calculations in context where it isn't being used as the hand size).

To address this, we can use CONSTANTs to give a name to the number. This makes it more self-documenting anywhere we use the constant. It also makes it more maintainable, since if we need to change the number, we only need to change the definition, and all places using the constant will be updated as well. This technique can be applied to most literals, whether numbers or strings.

```
   # earlier (likely global)
   HAND_SIZE = 10
   ...

      # here
      while hand_counter <= HAND_SIZE
```
### Comment on lines +98 to +113 
I like where your head is at with the rest of this function! You do a good job of setting everything up and making it clear just through your code what you are trying to do!

That being said, I do think this logic is a little over-engineered. Earlier in this function, you created `letter_pool_list` which holds a pile of all the letters we can choose from. This means that any time this function is called, it will start with a new pile of all the letters. We can use this to our advantage by simply destroying `letter_pool_list` as we pick letters. The overall idea would be:

1. Find a random index between 0 and the length of `letter_pool_list`.
2. Add whatever letter is at that index in `letter_pool_list` to `hand_list`.
3. Remove that letter from `letter_pool_list`

If we repeated that HAND_SIZE times, we would avoid the extra dictionaries and lists that are made!
### Comment on lines 39 to 148
While frequency dictionaries can be helpful, they do take up extra space. As written, this frequency dictionary won't do anything to affect time complexity, but it does increase the space complexity of our function to `O(n)` because we have to accommodate new memory for each copy of the letter we are creating from the word. With this in mind, we can accomplish the rest of the function in the same way without even using the new dictionary!
### Comment on lines +153 to +154 
If we go without the new dictionary you've created, we can absolutely accomplish this by simply looping through the word!
In the project docs, 8 points are added if the word is between 7 and 10 letters inclusive! Right now you'll add 8 points for 11+ letters as well! Is there a way that you could add this constraint to the conditional you have?
### Comment on lines +157 to +160
Notice that the conditions placed on how to score the word make this looping code challenging to understand. Comments can help, but since they aren't verified by Python, they can become out of sync with the code, potentially giving us bad information about how the code works. When reviewing our code, try to imagine yourself several months in the future trying to understand this code. Could you come back to this code and express the scoring rules in plain language from reading the code. I think this is probably doable, but some signposts throughout the structure could help.

For instance, why is it important that the length of the highest word is currently 10 where the current check takes place? It's because if a word is tied, it cannot beat a word that already uses the entire tile hand, which is 10 tiles long.

Rearranging some of the conditions can also be helpful. Combining similar conditions to minimize repeated blocks of logic, and eliminating unnecessary checks can help us focus on the key comparisons.

But ultimately, looking for a way to tease apart the steps might be the most helpful approach. For instance, rather than packing this all into a single loop that's comparing scores and tie breaking all at once, we could think of this more like a filtering problem. Determine the maximum score, then find all the words that have the maximum score. If there's only one, we're done. It's only if there's more than one that we need to employ the tie-breaking logic. But once we know that we are working with exactly the list of tied words, then we only need to look at the lengths for the tie-breaking, making that logic less cumbersome to think about.

Overall however, your approach to this particular function in this particular way is very well done!


