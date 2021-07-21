
def decorator(func):
    def decorated(h,l):
        if h > 0 and l > 0:
            func(h,l)
        else:
            print('error 발생')#raise ValueError()
    return decorated

@decorator #이름 변경 가능하다
def rectangular(height, length):
    result = height*length
    print(result)

@decorator
def triangle(height, length):
    result = height*length*0.5
    print(result)

# raise PermissionError
triangle(2,-4)



