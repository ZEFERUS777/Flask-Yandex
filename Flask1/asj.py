x1, y1, w1, h1 = map(int, input().split())
x2, y2, w2, h2 = map(int, input().split())

left1, right1 = x1, x1 + w1
top1, bottom1 = y1, y1 + h1

left2, right2 = x2, x2 + w2
top2, bottom2 = y2, y2 + h2

if (right1 <= left2 or
        left1 >= right2 or
        bottom1 <= top2 or
        top1 >= bottom2):
    print("YES")
else:
    print("NO")
