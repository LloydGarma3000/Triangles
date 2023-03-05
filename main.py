import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
win.fill((255, 255, 255))
size1 = 50
size2 = 50
g = 300
x = 200
y = 50
k = 300
l = 450
s =200
z = True
c = True
p = True
u = True

while True:
    win.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if z:
        x += 3
    else:
        x -= 3
    if x < 0:
        z = True
    elif x > 500:
        z = False
    if c:
        y += 3
    else:
        y -= 3
    if y < 0:
        c = True
    elif y > 500:
        c = False
    if p:
        k -= 3
    else:
        k += 3
    if k < 0:
        p = False
    elif k > 500:
        p = True
    if u:
        l -= 3
    else:
        l += 3
    if l < 0:
        u = False
    elif l > 500:
        u = True

    pygame.draw.polygon(win, (255, 0, 0), ([x, y,], [y, g], [g, x]), False)
    pygame.draw.polygon(win, (0, 0, 0), ([k, l], [l,s], [ s,k]), False)
    pygame.display.update()
    pygame.time.delay(10)