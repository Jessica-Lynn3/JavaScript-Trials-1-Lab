"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in the given list."""
    #   function outputAllItems(items) {
    #   for (const item of items) {
    #     console.log(item);
    #   }
    # }
    for item in items:
        print(item)


def get_all_evens(nums):
    """Given an list of numbers, return an array of all even numbers."""

    # function getAllEvens(nums) {
    #   const evenNums = [];

    #   for (const num of nums) {
    #     if (num % 2 === 0) {
    #       evenNums.push(num);
    #     }
    #   }

    #   return evenNums;
    # }

    even_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums 

def get_odd_indices(items):
    """Given a list, return all elements at odd numbered indices."""
    # function getOddIndices(items) {
    #   const result = [];

    #   for (const idx in items) {
    #     if (idx % 2 !== 0) {
    #       result.push(items[idx]);
    #     }
    #   }

    #   return result;
    # }

    result = []
    for i in range(len(items)):
        if i % 2 != 0:
            result.append(i)
    
    return result

def print_as_numbered_list(items):
    """Given a list, output a numbered list.
    Ex.:
    printAsNumberedList([1, 'hello', true]);
    1. 1
    2. hello
    3. true
    """

    #     function printAsNumberedList(items) {
    #   let i = 1;

    #   for (const item of items) {
    #     console.log(`${i}. ${item}`);

    #     i += 1;
    #   }
    # }

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1



def get_range(start, stop):
    """Return an list of numbers in a certain range.
    Ex:
    getRange(0, 5);
    [0, 1, 2, 3, 4]

    getRange(1, 3);
    [1, 2]
    """

    # function getRange(start, stop) {
    #   const nums = [];

    #   for (let num = start; num < stop; num += 1) {
    #     nums.push(num);
    #   }
    #   return nums;
    # }

    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums


def censor_vowels(word):
    """Given a string, return a string where vowels are replaced with '*'.
     Ex.:
    censorVowels('hello world');
    'h*ll* w*rld'"""

    # function censorVowels(word) {
    #   const chars = [];

    #   for (const letter of word) {
    #     if ('aeiou'.includes(letter)) {
    #       chars.push('*');
    #     } else {
    #       chars.push(letter);
    #     }
    #   }

    #   return chars.join('');
    # }

    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return chars.join('')

def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case.

    Ex.:
       > snakeToCamel('hello_world');
       'HelloWorld'"""

    # function snakeToCamel(string) {
    #   const camelCase = [];

    #   for (const word of string.split('_')) {
    #     camelCase.push(`${word[0].toUpperCase()}${word.slice(1)}`);
    #   }

    #   return camelCase.join('');
    # }

    camel_case = []

    for word in string.split('_'):
        camel_case.append(f"{word[0].upper}{word.slice[1:]}")

        return camel_case.join('')

def longest_word_length(words):
    """Return the length of the longest word in the given array of words.

    Ex.:
       > longestWordLength(['hello', 'world']);
       5
   
       > longestWordLength(['jellyfish', 'zebra']);
       9
    """
    
    #     function longestWordLength(words) {
    #   let longest = words[0].length;

    #   for (const word of words) {
    #     if (longest < word.length) {
    #       longest = word.length;
    #     }
    #   }

    #   return longest;
    # }

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest 

def truncate(string):
    """Truncate repeating characters into one character.

     Ex.:
       > truncate('aaaabbbbcccca');
       'abca'
    
       > truncate('hi***!!!! wooow');
       'hi*! wow'"""

    # function truncate(string) {
    #   const result = [];

    #   for (const char of string) {
    #     if (result.length === 0 || char !== result[result.length - 1]) {
    #       result.push(char);
    #     }
    #   }

    #   return result.join('');
    # }

    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    
    return result.join('')

    
def has_balanced_parens(string):
    """Return true if all parentheses in a given string are balanced.

     Ex.:
     > hasBalancedParens('()');
     true

     > hasBalancedParens('((This) (is) (good))');
     true

     > hasBalancedParens('(Oh no!)(');
     false"""

    # function hasBalancedParens(string) {
    #   let parens = 0;

    #   for (const char of string) {
    #     if (char === '(') {
    #       parens += 1;
    #     } else if (char === ')') {
    #       parens -= 1;

    #       if (parens < 0) {
    #         return false;
    #       }
    #     }
    #   }

    #   return parens === 0;
    # }

    parens = 0

    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1
        
            if parens < 0:
                return False
    
    return parens == 0


def compress(string):
    """Return a compressed version of the given string.

     Ex.:
       > compress('aabbaabb');
       'a2b2a2b2'

     If a character appears once, it shouldn't be followed by a number:
       > compress('abc');
       'abc'

     The function should handle all types of characters:
       > compress('Hello, world! Cows go moooo...');
       'Hel2o, world! Cows go mo4.3'"""


    # function compress(string) {
    #   const compressed = [];

    #   let currChar = '';
    #   let charCount = 0;
    #   for (const char of string) {
    #     if (char !== currChar) {
    #       compressed.push(currChar);

    #       if (charCount > 1) {
    #         compressed.push(charCount.toString());
    #       }

    #       currChar = char;
    #       charCount = 0;
    #     }

    #     charCount += 1;
    #   }

    #   compressed.push(currChar);
    #   if (charCount > 1) {
    #     compressed.push(charCount.toString());
    #   }

    #   return compressed.join('');
    # }

    compressed = []

    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

                curr_char = char
                char_count = 0
            
            char_count += 1

    compresed.append(curr_char)

    if char_count > 1:
        compressed.append(str(char_count))

    return compressed.join('')
