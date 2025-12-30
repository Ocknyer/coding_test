def solution(my_string):
#     result = [0 for i in range(52)]
#     alpha = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    
#     for i in my_string:
#         for j, v in enumerate(alpha):
#             if i == v:
#                 result[j] += 1
                
#     return result

    result=[0]*52
    
    for x in my_string:
        if x.isupper():
            result[ord(x)-65]+=1
        else:
            result[ord(x)-71]+=1
            
    return result

    
    