import sys
dimmensions = sys.stdin.read().split()
answer = 0
for d in dimmensions:
    l, w, h = d.split('x')
    l = int(l)
    w = int(w)
    h = int(h)
    sides = (l*w, w*h, h*l)
    answer += sum(sides) * 2 + min(sides)
print(answer)