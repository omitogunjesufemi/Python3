from mutators import P

p1 = P(42)
p2 = P(4711)
print("=>", p1.x)
p1.x = 47
print("=>", p1.x)
p1.x += p2.x
print("=>", p1.x)
