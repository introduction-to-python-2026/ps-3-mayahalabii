def approximate_pi(n_terms=10):
    pass # replace pass with your code

    pi = 0
    for i in range(n_terms) :
    pi += 4 * (((-1) ** i) / (2*i + 1))
    return pi
