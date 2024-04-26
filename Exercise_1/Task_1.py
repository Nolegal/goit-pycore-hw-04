

def total_salary(path):
  
    with open('Exercise_1\\text.txt', 'r', encoding='utf-8') as path:
       lines = [el.strip().split(',') for el in path.readlines()]  
       total=0
       for line in lines:  
          salary=int(line[1])
          total+=salary
          average=total/len(lines)
       print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

total_salary('Exercise_1\\text.txt')