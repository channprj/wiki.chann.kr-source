Title: 파이썬 자료형, 연산자 기초
Date: 2016-01-04 20:12
Slug: python-variable-operator

# 파이썬 자료형, 연산자 기초
> 작성중

## 특징
* 인터프리터 언어
* 가독성이 좋음
* 접착성이 좋음(풀 언어(glue language)라고도 부름)
* 무료
* 방대한 오픈소스
* 유니코드 기반
* 동적 타이핑

----

## 2.x와 3.x의 차이
> 작성중

* print 함수 형태 변경
* int 형으로 통일됨
* 하지만 나누기 결과는 float
* 3.x는 문자열 기본 인코딩이 유니코드

----

## 설치법
### 윈도우
> 작성중

----

### 맥
> 작성중

----

### 리눅스
> 작성중

----

## 변수명
변수명은 문자, 숫자, 언더바(_)를 포함 가능하지만 숫자가 먼저 올 수 없다.

```python
>>> python = 1
>>> Python = 2
>>> python_var = 3
>>> python_1 = 4
```
<br>

사전에 기능과 의미가 정의된 파이썬 키워드는 변수명으로 사용할 수 없다.

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

----

## 문자열
반드시 큰따옴표("")나 작은따옴표('')로 감싸야 한다.

```python
>>> 'str'
>>> "str"
>>> "This is 'str'"

# 여러 줄 입력일 경우
>>> print("""
나는
너의
동반자
""")
```
<br>

이스케이프 문자는 C와 유사하다.

* `\n`	: 줄바꿈
* `\t`	: 탭
* `\r`	: 캐리지 반환
* `\0`	:  NULL
* `\\`	: '\'문자
* `\'`	: 따옴표 문자
* `\"`	: 쌍따옴표 문자

```python
>>> print("This is \nEscape character.")
This is
Escape character.
>>> 
```
<br>

문자열을 다루는 것도 쉽다. 잘라 쓰기 쉽고 붙이기는 더 쉽다. 자동으로 배열처럼 인덱싱도 된다. 인덱스를 이용하여 문자열의 특정 문자를 다른 문자로 변경할 수는 없으나 문자열 전체를 변경하는 것은 가능하다.

```python
>>> '파이' '썬'
'파이썬'

>>> '파이'+'썬'
'파이썬'

>>> '파이' * 3
'파이파이파이'

>>> a = '파이썬'
>>> a[2]
'썬'

# 0(시작)부터 2글자 슬라이싱
>>> a[0:2]
'파이'

# 시작(0 생략)부터 3글자까지 슬라이싱
>>> a[:3]
'파이썬'

# 뒤에서부터 1글자만 슬라이싱
>>> a[-1:]
'썬'
```

----

## 리스트
파이썬에서의 리스트는 값의 나열이라 순서가 있으며 여러 종류의 값을 담을 수 있다. 인덱스는 0부터 시작하며 슬라이싱도 가능하다.

```python
# 배열의 선언
>>> food = ['rice', 'cheese', 'apple']

# 배열 출력
>>> food
['rice', 'cheese', 'apple']

# 배열의 타입 체크
>>> type(food)
<class 'list'>

# append() 함수로 리스트 뒤에 새 아이템 추가
>>> food.append('chicken')
>>> food
['rice', 'cheese', 'apple', 'chicken']

# insert() 함수로 리스트 중간에 새 아이템 추가
>>> food.insert(2, 'banana')
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken']

# extend() 함수로 여러 아이템을 한번에 추가
>>> food.extend(['cola', 'cider', 'coffee'])
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken', 'cola', 'cider', 'coffee']

# += 연산자로 리스트 붙이기
>>> food += ['cake']
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken', 'cola', 'cider', 'coffee', 'cake']

# 문자열을 붙일 경우 각 문자단위로 쪼개져서 붙음
>>> food += 'ice'
>>> food
['rice', 'cheese', 'banana', 'apple', 'chicken', 'cola', 'cider', 'coffee', 'cake', 'i', 'c', 'e']

# index() 함수로 인덱스 번호 체크
>>> food.index('apple')
3

## 인덱스 찾는 시작점 부여
>>> food += ['apple'] # 리스트 아이템 추가
>>> food.index('apple', 5)
12

# count() 함수로 리스트 아이탬 갯수 체크
>>> food.count('apple')
2
```
<br>

기본적으로 리스트 아이템을 삭제하는 건 크게 2가지 방법이 있다.

* pop()	: 뒤에서부터 값을 빼내옴.
* remove()	: 위치에 상관없이 리스트 아이템 삭제.

```python
# pop() 함수는 리스트 맨 뒤 아이템을 출력 후 삭제
>>> food.pop()
'banana'

# remove()는 위치에 관계없이 조용히 해당 리스트 아이템만 삭제
>>> food.remove('i')
>>> food.remove('e')

# 지우고자 하는 아이템이 없으면 오류메시지 출력
>>> food.remove('r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list

```
<br>

정렬방법은 아래와 같다.

```python
# 순방향 정렬
>>> food.sort()
>>> food
['apple', 'apple', 'banana', 'c', 'cake', 'cheese', 'chicken', 'cider', 'coffee', 'cola', 'e', 'i', 'rice']

# 역순 정렬
>>> food.reverse()
>>> food
['rice', 'i', 'e', 'cola', 'coffee', 'cider', 'chicken', 'cheese', 'cake', 'c', 'banana', 'apple', 'apple']
```

----

## 세트
> 작성중

----

## 튜플
> 작성중

----

## 사전
> 작성중

----

## 논리연산자
> 작성중

----

## 얕은 복사, 깊은 복사
> 작성중

