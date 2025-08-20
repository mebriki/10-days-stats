# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = input()

# prep x
x = list(map(float, x.split()))
x.sort()

#mean
mean = sum(x)/n
print(mean)

#median
def median(x):
    c = int(n/2)
    if n % 2 == 0:
        return (x[c-1]+x[c])/2
    else:
        return x[c]

print(median(x))

#mode
def mode(x):
    y = list(set(x))
    z = {num: x.count(num) for num in y}
    mx = max(z.values())
    md = [k for k, v in z.items() if v == mx]
    return min(md)

print(mode(x))