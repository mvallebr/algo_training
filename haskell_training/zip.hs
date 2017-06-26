-- zip' should merge two lists into a list of tuples
zip' :: [a] -> [b] ->[(a,b)]
zip' [] [] = []
zip' (ah:at) (bh:bt) = (ah, bh) : zip at bt