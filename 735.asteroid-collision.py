def asteroidCollision(asteroids: list[int]) -> list[int]:
    asteroids = [0] + asteroids + [0]
    current = 1
    # a = 0
    while current < len(asteroids)-1:
        if asteroids[current] > 0 and asteroids[current+1] < 0:
            a = current+1
            if asteroids[current] > abs(asteroids[a]):
                asteroids.pop(a)
                continue
            elif asteroids[current] < abs(asteroids[a]):
                asteroids.pop(current)
                current -= 1
                continue
            elif asteroids[current] == abs (asteroids[a]):
                current -= 1
                asteroids.pop(current+1)
                asteroids.pop(current+1)
                continue
            if asteroids[current] < asteroids[a]:
                current = a
                continue
        current += 1
    return asteroids[1:-1]