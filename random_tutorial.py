# ref. https://docs.python.org/3/library/random.html

from random import choice

if __name__ == "__main__":
    num_seqs = range(20)
    print('num_seqs', list(num_seqs))
    print('choice(num_seqs)', choice(num_seqs))
    print('choice(num_seqs)', choice(num_seqs))
