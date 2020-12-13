# Python의 정렬 

파이썬의 리스트를 정렬하는 방법으로는 `sort()`와 `sorted()` 두 가지 방식이 있다.



1. ###  sort()

   ```python
   lst = [5,4,6,2,1,3]
   lst.sort()
   print(lst)
   # [1,2,3,4,5,6]
   
   lst.sort(reverse = True)
   print(lst)
   # [6,5,4,3,2,1]
   ```

   sort 함수는 리스트 내부의 요소를 정렬해주는 함수이다.  (오직 리스트만을 위한 메소드)

   기본적으로 오름차순이며 reverse 옵션을 True로 한다면 내림차순 정렬도 가능하다.

   </br>

   ~~~python
   lst = [(3,4),(1,1),(1,-1),(2,2),(3,3)]
   lst.sort(key = lambda x: x[1])
   # 리스트 두번째 값을 비교 (기본값: 오름차순)
   
   print(lst)
   # [(1, -1), (1, 1), (2, 2), (3, 3), (3, 4)]
   
   lst = ['I','have','a','dream','a','song','to','sing']
   lst.sort(key = lambda x: len(x))	
   # 문자열 길이로 비교 (기본값: 오름차순)
   
   print(lst)
   # ['I', 'a', 'a', 'to', 'have', 'song', 'sing', 'dream']
   
   lst = [{'name':'식빵','price':1000},
         {'name':'호빵','price':500},
         {'name':'크림빵','price':1500}]
   lst.sort(key = lambda x : x['price'])
   # price 항목을 기준으로 비교 (기본값: 오름차순)
   
   print(lst)
   # [{'name': '호빵', 'price': 500}, {'name': '식빵', 'price': 1000}, {'name': '크림빵', 'price': 1500}]
   ~~~

   또한 위처럼 key 함수를 이용해서 필요한 값을 정해서 정렬 할 수도 있다.

   </br> 

2. ###  sorted()

   `sort()` 함수는 오직 리스트만 정렬해주는 함수이고 반환 값이 없는 함수인 반면 

   `sorted()` 함수는 정렬된 새로운 리스트를 리턴 해준다.

   따라서

   ```python
   lst = [5,2,3,1,4]
   
   for i in sorted(lst):
   	print(i)
   	
   # 1 2 3 4 5
   ```

   처럼 정렬 된 새로운 리스트를 바로 사용 가능하다.

   </br>

   ```python
   lst = [(3,4),(1,1),(1,-1),(2,2),(3,3)]
   for i in sorted(lst,key = lambda x: x[1]):
   	print(i)
   
   # (1, -1), (1, 1), (2, 2), (3, 3), (3, 4)
   
   lst = ['I','have','a','dream','a','song','to','sing']
   for i in sorted(lst, key = lambda x: len(x), reverse = True):
   	print(i)
       
   # dream have song sing to I a a
   ```

   `sort()`와 마찬가지로 reverse 옵션과 key 속성을 사용한 정렬까지 가능하다.

