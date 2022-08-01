# ref. https://docs.python.org/3/library/random.html

from random import choice, sample

if __name__ == "__main__":
    num_seqs = range(20)
    print("num_seqs", list(num_seqs))
    print("choice(num_seqs)", choice(num_seqs))
    print("choice(num_seqs)", choice(num_seqs))

    print(sample(num_seqs, 3))
    print(sample(num_seqs, 3))
    print(sample(num_seqs, 5))
    print(sample(num_seqs, 5))
