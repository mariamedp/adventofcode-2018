
fname <- "../day1.txt"

input <- as.integer(readLines(fname))

freq_seq <- cumsum(input)

freq_dup <- duplicated(freq_seq)
while (!any(freq_dup)) {
  freq_seq <- c(freq_seq, tail(freq_seq, 1) + freq_seq)
  freq_dup <- duplicated(freq_seq)
}

print(freq_seq[freq_dup][1])
