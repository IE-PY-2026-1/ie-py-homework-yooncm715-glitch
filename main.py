# 파일이름 :3주차 과제
# 작 성 자 :60231964 윤채민

water_database=[]

#제거 효율 계산 함수
def calculate_efficiency(in_bod, out_bod):
    if in_bod==0:
        return 0.0
    eff=((in_bod-out_bod)/in_bod)*100
    return eff
    
#데이터 입력 및 등급 판정
def input_water_data():
    global water_database
    print('\n---[수질 데이터 입력]---')
    point_name=input('측정 지점명을 입력하세요:')
    in_bod=int(input('유입수 BOD 농도(mg/L)를 입력하세요:'))
    out_bod=int(input('유출수 BOD 농도(mg/L)를 입력하세요:'))
    legal_limit=float(input('법적 방류 기준치(mg/L)를 입력하세요:'))
    
    efficiency=calculate_efficiency(in_bod, out_bod)
    if efficiency >=95:
        grade='S(우수)'
    elif efficiency>=85:
        grade='A(양호)'
    elif efficiency>=75:
        grade='B(보통)'
    elif efficiency>=65:
        grade='C(주의)'
    else:
        grade='F(불량)'
        
    special_title='일반'
        
    if efficiency>=95 and out_bod <= (legal_limit*0.5):
        special_title='정밀 진단 대상(최우수)'
        
    single_point_data=[point_name, in_bod, out_bod, legal_limit, efficiency, grade, special_title]
    
    water_database.append(single_point_data)
    print(f'{point_name} 지점의 데이터가 성공적으로 등록되었습니다.')

#전체 데이터베이스 출력
def print_database():
    if not water_database:
        print('\n 현재 등록된 수질 데이터가 없습니다. 먼저 데이터를 입력해주세요')
        return
print('\n'+'='*30)
print(' 지능형 수질 등급 판독 시스템 결과 리포트')
print('='*30)

for point in water_database:
    name=point[0]
    in_b=point[1]
    out_b=point[2]
    limit=point[3]
    eff=point[4]
    grd=point[5]
    title=point[6]
    print(f'지점명:{name}')
    print(f'- 수질 현황 : 유입 BOD{in_b}mg/L  | 유출 BOD{out_b}mg/L (기준치:{limit}mg/L)')
    print(f'- 분석 결과 :제거 효율 {eff:.2f}% | 최종 등급:{grd}')
    print(f'- 특이 사항 : {title}')
    print('-'*40)
print(f'총 {len(water_database)}개 지점 출력 완료')

#메인 제어
while True:
    print('\n======[지능형 수질 관리 시스템 메뉴]======')
    print('1. 수질 데이터 등록 및 판정')
    print('2. 전체 수질 데이터베이스 조회')
    print('3. 프로그램 종료')
    print('=========================================')
    choice=input('원하는 메뉴 번호를 선택하세요.')
    if choice == '1':
        input_water_data()
    elif choice =='2':
        print_database()
    elif choice=='3':
        print('\n 시스템을 종료합니다.')
        break
    else:
        print('\n 잘못된 입력입니다. 1,2,3번 중에서 다시 선택해주세요.')