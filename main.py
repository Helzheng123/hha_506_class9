import sys

sys.path.append('/home/helen_zheng/hha_506_class9/modules')

from modules.module1 import addition, subtraction

output1 = addition(5, 10)
output2 = subtraction(5, 10)

print('Output 1: ', output1)
print('Output 2: ', output2)

# inserting the output within the quotes
print(f"Output 1: {output1}")
print(f'Output 2: {output2}')