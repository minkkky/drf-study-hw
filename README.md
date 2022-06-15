# Python 기초 확인

## *args, **kwargs를 사용하는 예제 코드 짜보기
- `*args`
  - \*arguments의 줄임말이다.
  - 함수에 복수의 인자를 `튜플`의 형태로 받을 때 사용한다.
  - 튜플을 풀어주는 역할을 하는 `*`을 붙이기만 하면, 변수명은 바꿀 수 있다.
```
def add(*args): # *nums 라고 써도 동작함 
  result = 0
  for i in args:
    result += i
  print(f'result = {result}')

add(1, 2, 4)
>> result = 7
```
- `**kwargs`
  - \**keyword arguments의 줄임말이다.
  - 함수에 `딕셔너리` 형태로 값을 저장하며, key값을 함께 보낼 수 있다.
  - 딕셔너리를 풀어주는 역할을 하는 `**`을 붙이기만 하면, 변수명은 바꿀 수 있다. 
```
def view_info(**kwargs): # **datas 라고 써도 동작함
  for key, value in kwargs.items():
    print(f'{key} : {value}')

view_info(name='sunset', age=17)
>> name : sunset
   age : 17
```
  
## mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
- `mutable`
  - mutable은 값이 변한다. 즉, 수정 가능한 객체이다.
  - 해당하는 자료형은 `[리스트]`와 `{딕셔너리}`이다.
- `immutable`
  - immutable은 값이 변하지 않는다. 즉, 수정 불가능한 객체이다.
  - 해당하는 자료형은 `'문자형'`, `숫자형`, `(튜플)`이다.
  
## DB Field에서 사용되는 Key 종류와 특징 서술하기
- `Primary Key`는 기본키로, 모든 테이블은 하나의 기본키를 반드시 가져야 한다.
  - 기본키는 null값을 가질 수 없으며, 중복될 수도 없다.
  - 테이블 데이터를 식별할 수 있는 `유일성`을 가져야 한다.
- `Unique Key`는 고유키로, 유일해야 하는 컬럼이다.
  - 고유키는 null값을 가질 수 있으나, 중복되어선 안 된다.
- `Foreign Key`는 외래키로, 두 개의 테이블을 연결해주는 다리 역할을 한다.
  - 외래키가 포함된 테이블은 `자식 테이블`이라고 하고, 외래키 값을 제공하는 테이블을 `부모 테이블`이라고 한다.
  - 부모 테이블의 기본키, 혹은 고유키를 외래키로 지정할 수 있다.
  
## Django에서 QuerySet과 object는 어떻게 다른지 서술하기
- `object`는 Model과 데이터베이스 간에 연산을 수행하는 역할을 하고, `objects`를 통해 데이터베이스와 연산해서 얻은 여러 모델 데이터가 담겨 있는 것이 `Queryset`이다.
- `QuerySet`은 `리스트 안에 딕셔너리`가 들어있는 형태이다.
  - <QuerySet [{'key':value, ..., 'key':value}]>
