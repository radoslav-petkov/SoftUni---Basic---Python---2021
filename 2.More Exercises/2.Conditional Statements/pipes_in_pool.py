v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

first_pipe_fill = p1 * h
second_pipe_fill = p2 * h
total_fill = first_pipe_fill + second_pipe_fill

filled = (total_fill / v) * 100                 
percent_from_p1 = h * p1 / total_fill * 100
percent_from_p2 = h * p2 / total_fill * 100

if total_fill <= v:

 print(f"The pool is {filled}% full. Pipe 1: {percent_from_p1:.2f}%. Pipe 2: {percent_from_p2:.2f}%.")
else:
    litres_more = abs(v - total_fill)

    print(f"For {h} hours the pool overflows with {litres_more:.2f} liters.")