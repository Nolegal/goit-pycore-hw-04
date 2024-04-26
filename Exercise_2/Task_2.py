def get_cats_info(path):
     with open('Exercise_2\\text2.txt', 'r', encoding='utf-8') as path:
          lines = [el.strip().split(',') for el in path.readlines()]
          cats_data=["id","name","age"]
          result=[]
          for line in lines:
            dictionary = dict(zip(cats_data, line))
            result.append(dictionary)
          return result


print(get_cats_info('Exercise_2\\text2.txt'))