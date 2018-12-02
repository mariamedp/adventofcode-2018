
fname <- "../day2_test.txt"

input <- readLines(fname)

letters <- strsplit(input, '')

diffs <- sapply(letters, function(x)
                sapply(letters, function(y) 
                  sum(x != y)))

ind_result <- which(diffs == 1, arr.ind=TRUE)
word1 <- letters[[ind_result[1, "row"]]]
word2 <- letters[[ind_result[1, "col"]]]

print(paste(word1[word1 == word2], collapse=""))
