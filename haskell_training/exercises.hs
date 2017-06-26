-- examples from Python

-- zip' should merge two lists into a list of tuples
zip' :: [a] -> [b] ->[(a,b)]
zip' [] [] = []
zip' (ah:at) (bh:bt) = (ah, bh) : zip at bt

-- repeat' should repeat its (single) argument indefinitely
repeat' :: a -> [a]
repeat' a = a : repeat' a

-- cycle' should repeat its (list) argument indefinitely
cycle' :: [a] -> [a]
cycle' a = a ++ cycle' a

-- takeWhile' should take elements from a list until the predicate fails
-- takeWhile' :: TBD
takeWhile' :: [a] -> (a -> Bool) -> [a]
takeWhile' (ah:at) predicate = if predicate ah then ah:takeWhile' at predicate else []
--takeWhile' [1,2,3,4,5,6,7,8,9] (<4) 
--[1,2,3]
-- Examples from std::algorithm

-- accumulate should sum the range
-- accumulate :: TBD
accumulate :: Num a => [a] -> a
accumulate [] = 0
accumulate (ah:at) = ah + accumulate at 
-- accumulate [1,4,5]
-- 10


-- λ> partial_sum [0..10]
-- [0,1,3,6,10,15,21,28,36,45,55]
partial_sub_sum :: Num a => a -> [a] -> [a]
partial_sub_sum a [] = []
partial_sub_sum a (ah:at) = a+ah : partial_sub_sum (a+ah) at

partial_sum :: Num a => [a] -> [a]
partial_sum [] = []
partial_sum l = partial_sub_sum 0 l

-- λ> all_of (>0) [1..10]
-- True
all_of :: (a -> Bool) -> [a] -> Bool
all_of f [] = True
all_of f (h:t) = if f h then all_of f t else False

-- λ> any_of (>5) [1..10]
-- True
any_of :: (a -> Bool) -> [a] -> Bool
any_of f [] = False
any_of f (h:t) = if f h then True else any_of f t

-- λ> for_each (>0) [0,1]
-- [False, True]
for_each :: (a -> b) -> [a] -> [b]
for_each = undefined

-- count the number of elements matching a predicate
-- count_if :: TBD
count_if = undefined

-- λ> lexigraphical_compare [1..10] [1..9]
-- True
lexigraphical_compare :: Ord a => [a] -> [a] -> Bool
lexigraphical_compare = undefined

-- λ> max_element [1,2,1]
-- 2
max_element :: Ord a => [a] -> a
max_element = undefined

-- merge should merge two sorted lists
-- λ> merge [0..10] [4..5]
-- [0,1,2,3,4,4,5,5,6,7,8,9,10]
-- merge :: TBD
merge = undefined

-- λ> mergesort [5,3,1,2,4]
-- [1,2,3,4,5]
mergesort :: [a] -> [a]
mergesort = undefined

-- mismatch should return the index of the first mismatch between two lists,
-- or nothing
-- λ> mismatch [1..10] [1..10]
-- Nothing
-- λ> mismatch [1..10] [1..5]
-- Just 5
mismatch :: [a] -> [a] -> Maybe Int
mismatch = undefined

-- inits should return all possible initial lists in ascending order, 
-- including the empty list
-- λ> inits [0..2] 
-- [[], [0], [0,1], [0,1,2]]
inits' :: [a] -> [[a]]
inits' = undefined

-- tails should return all possible initial lists in descending order, 
-- including the empty list
-- λ> tails [0..2]
-- [[0,1,2], [1,2], [2], []]
tails' :: [a] -> [[a]]
tails' = undefined

-- splits should return every possible split of the list
-- > splits [0..2]
-- > [([],[0,1,2]),([0],[1,2]),([0,1],[2]),([0,1,2],[])]
splits' :: [a] -> [([a], [a])]
splits' = undefined

-- hint: define permutations in terms of splits
-- permutations (x:xs) is x interleaved with every split, of every permutation of xs
-- λ> permutations [1..3] 
-- [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
permutations :: [a] -> [[a]]
permutations = undefined