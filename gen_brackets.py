def gen_brackets(n, prefix, left, right):
    if n == left and n == right:
        print(prefix)
    else:
        if left < n:
            gen_brackets(n, prefix + '(', left + 1, right)
        if right < left:
            gen_brackets(n, prefix + ')', left, right + 1)

gen_brackets(n=int(input()), prefix='', left=0, right=0)
