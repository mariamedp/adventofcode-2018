
fname <- "../day2.txt"

input <- readLines(fname)

letters_n <- lapply(strsplit(input, ''), function(x) unique(table(x)))

n_two_letters <- sapply(letters_n, function(x) any(x == 2))
n_three_letters <- sapply(letters_n, function(x) any(x == 3))

print(sum(n_two_letters) * sum(n_three_letters))
