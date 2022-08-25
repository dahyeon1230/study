# 하나만 출력
print("# 하나만 출력합니다.")
print('하나만 출력합니다!')

# 여러개 출력
print('#여러개 출력합니다.')
print("안녕하세요", "저는", "이다현", "입니다.")  # 안녕하세요 저는 이다현 입니다.

# 문자열 내부에 따옴표 넣기
# 작은 따옴표로 문자열 만들어 큰따옴표 포함 반대로도 가능
print('"안녕하세요?" 저는 이다현이라고 합니다.')
print("'안녕하세요?' 저는 이다현 이라고 합니다.")

# 이스케이프문자 역슬래시 기호와 함께 조합해서 사용하는 특수한 문자
print("\"안녕하세요\"라고 말했습니다.")
print('\'안녕하세요\'라고 말했습니다.')

# \n줄바꿈 \t탭
print("안녕하세요\n안녕하세요")
'''안녕하세요
안녕하세요'''

print("안녕하세요\t안녕하세요")
# 안녕하세요      안녕하세요

# 여러줄 문자열 기능:큰따옴표 작은따옴표 3번 반복

print("""동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세""")

# 위아래로 공백이 들어감
print("""
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산 대한사람
대한으로 길이 보전하세
""")

# +연산자 : 두문자열을 연결하여 새로운 문자열 만들어냄, 더하기 기호이나 다른 수행을 함

print("안녕"+"하세요")
print("안녕하세요"+"!")

# print("안녕하세요"+1)
# TypeError: can only concatenate str (not "int") to str

print("안녕하세요"+"1")  # 안녕하세요1

# *연산자 : 문자열 반복 연산자
print("안녕하세요"*3)

# 문자선택(인덱싱) 제로인덱스
myString = 'Hello world'
print(myString[0])
print(myString[1])
print(myString[2])
print(myString[3])
print(myString[4])

# 거꾸로 출력
print(myString[-1])
print(myString[-2])
print(myString[-3])
print(myString[-4])
print(myString[-5])

# 문자열 선택범위 마지막 숫자는 포함하지 않는다.
print(myString[1:5])
print(myString[0:2])

print(myString[1:])
print(myString[:1])
