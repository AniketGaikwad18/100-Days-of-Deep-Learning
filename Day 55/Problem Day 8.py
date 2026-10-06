x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

n = 5

sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(a * b for a, b in zip(x, y))
sum_x2 = sum(a * a for a in x)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)

x_mean = sum_x / n
y_mean = sum_y / n

c = y_mean - m * x_mean

prediction = m * 80 + c

print(f"{prediction:.2f}")
