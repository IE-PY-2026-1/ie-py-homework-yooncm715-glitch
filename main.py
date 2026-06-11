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
    try:
        in_bod=int(input('유입수 BOD 농도(mg/L)를 입력하세요:'))
        if in_bod<=0:
            print('유입수 BOD는 0보다 커야합니다. 입력이 취소됩니다.')
            return
        
        out_bod=int(input('유출수 BOD 농도(mg/L)를 입력하세요:'))
        legal_limit=float(input('법적 방류 기준치(mg/L)를 입력하세요:'))
    except ValueError:
        print("\n [입력 오류] 농도 및 기준치는 반드시 숫자로 입력하셔야 합니다!")
        print("-> 안전을 위해 메인 메뉴로 돌아갑니다. 다시 시도해 주세요.")
        return
    efficiency=calculate_efficiency(in_bod, out_bod)
    grade, special_title=diagnose_water(efficiency, out_bod, legal_limit)
    
    current_point=[point_name, in_bod, out_bod, legal_limit, efficiency, grade, special_title]
    water_database.append(current_point)


def diagnose_water(efficiency, out_bod, legal_limit):
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
        special_title='첨단 친환경 공정 (최우수)'
    return grade, special_title
  

def display_all_results():
    if not water_database:
        print("\n 현재 저장된 수질 데이터가 없습니다. 먼저 데이터를 등록해 주세요.")
        return
    print('\n==================================== 수질 진단 현황 데이터베이스 ====================================')
    print(f"{'지점명':<12} | {'유입 BOD':<8} | {'유출 BOD':<8} | {'기준치':<8} | {'제거효율':<8} | {'진단등급':<8} | {'특이사항'}")
    print("-" * 102)

    for point in water_database:
        print(f"{point[0]:<12} | {point[1]:<10} | {point[2]:<10} | {point[3]:<9} | {point[4]:>7.2f}% | {point[5]:<10} | {point[6]}")
    print("=" * 102)



def save_to_file():
    if not water_database:
        print('\n저장할 데이터가 없습니다. 데이터를 최소 1개 이상 입력해 주세요.')
        return
    filename='water_report.txt'

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("=== 지능형 수질 등급 판독 시스템 최종 보고서 ===\n")
            file.write("-" * 60 + "\n")
            
            for point in water_database:
                file.write(f"📍 측정 지점명: {point[0]}\n")
                file.write(f"   - 유입/유출 BOD: {point[1]} mg/L / {point[2]} mg/L\n")
                file.write(f"   - 법적 방류 기준치: {point[3]} mg/L\n")
                file.write(f"   - 최종 제거 효율: {point[4]:.2f}%\n")
                file.write(f"   - 수질 진단 등급: {point[5]}\n")
                file.write(f"   - 특이 사항 인증: {point[6]}\n")
                file.write("-" * 60 + "\n")
        print(f'\n[파일 저장 성공] 데이터가 {filename} 파일로 정상 저장되었습니다.')
    except IOError:
        print(f'\n[파일 시스템 오류] {filename} 파일 쓰기 권한을 획득하지 못했습니다.')


#메인 제어
while True:
    print("\n======= [지능형 수질 관리 시스템 V3.0] =======")
    print("1. 새로운 수질 데이터 입력 및 진단")
    print("2. 전체 수질 데이터베이스 조회")
    print("3. 파일로 결과 저장하기 (.txt)")
    print("4. 프로그램 종료")
    print("==============================================")
    
    choice=input('원하는 메뉴 번호를 선택하세요:')
 
    if choice == '1':
        input_water_data()
    elif choice =='2':
        display_all_results()
    elif choice == '3':
        save_to_file()
    elif choice=='4':
        print('\n 시스템을 안정적으로 종료합니다.')
        break
    else:
        print('\n 잘못된 입력입니다. 1,2,3,4번 중에서 다시 선택해주세요.')