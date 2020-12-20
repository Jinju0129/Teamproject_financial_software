# Welcome to the Group10's Teamproject_financial_software!!

금융 소프트웨어 팀 프로젝트용 repository입니다.

참가자: 맹진주, 김예진, 우용승

**해당 프로젝트는 windows10에서 진행하였으며 Microsoft excel이 필요합니다.**

작성자는 office16버전에서 진행하였으며, 타 버전은 확인해보지 못했으나, 프로젝트 진행 오류시 16버전으로 설치 뒤 진행해보길 바랍니다

(실행을 바로 원하시는 분은 [Getting started](#getting-started) 로 이동해주시면 됩니다.)

------------------------------------
### 주제: 랜덤 능력치와 FIFA게임 능력치를 활용한 축구 결과 시나리오 예측
**알고리즘을 직접 제작**함으로써 **축구 경기 결과 예측을 제공하면서** **푸아송 분포** 및 **과거의 기록들**로부터 예상되는 결과도 제공합니다.
사용자로부터 선수들의 능력치를 **random**으로 할지, auto로 설정할지(게임사이트를 통한 **웹 스크랩**)를 정해서
경기 결과를 도출하며, **사용자의 흥미도를 높이기 위해 결과를 엑셀 파일과 pygame**을 통한 gamepad로 출력합니다.
**경기 도출 방식을 정교**하게 함에 더해서 **머신러닝**을 가세한다면 더욱 정확한 결과를 도출해낼 수 있을 것입니다.

## 실행파일 목록

|       **File name**       |       **기능**       |    
|---------------------------|----------------------|
|         main.py           | 전체적인 것을 총괄합니다. method를 호출하며 사용자 입력으로부터 오류를 처리합니다| 
|       stat_players.py     | 사용자의 입력에 따라, random or auto(웹 스크랩 방식)로 선수들 스탯을 할당합니다|
|       calcul_score.py     | 선수들의 스탯을 합산한 뒤, (슈팅, 패스, 점유율, 선방횟수 등)을 계산합니다|
|       make_excel.py       | 웹 스크랩을 통하여 과거의 기록들을 excel에 작성하고, 푸아송 분포와 직접 추정한 결과를 작성합니다|
|   poisson_distribution.py | 푸아송 분포를 통해서 [team1 vs team2] 결과 간 score를 예측하고 make_excel에 전달합니다|
|        Pannel.py          | 모든 결과들을 전달 받아 pygame을 통해 image 등으로 결과를 표현합니다|


## Getting started

1. Teamproject_financial_software 프로젝트를 클론합니다

    ```
    git clone https://github.com/WooYongSeung/Teamproject_financial_software.git
    ```

2. Pycharm으로 해당 프로젝트를 open한 뒤, pycharm 하단 부분의 Terminal을 누르고 다음을 입력합니다

    ```
    pip install -U -r requirements.txt
    
    (에러시 pip install --upgrade pip를 진행한 뒤, 재입력합니다)
    (그래도 해결되지 않을시 pip install -r requirements.txt를 입력하거나 dndydtmd@naver.com으로 연락주세요)
    ```

3. main.py에서 프로그램을 실행합니다.

    ```
    main.py에서 빈 공간에 우클릭 한 뒤, Run 'main'하시면 됩니다
    ```
    
4. 하단 작업표시줄을 보시면 엑셀 결과와 pygame이 결과로 출력됩니다. pygame을 종료하면 excel이 자동으로 종료됩니다 

    ```
    result_list.xlsx파일을 임의로 open 한 뒤 프로그램을 실행하면 error가 발생합니다. 프로그램 실행 시 유의해주세요.
    ```

## Contents
- [Welcome to the Group10's Teamproject_financial_software !!](#welcome-to-the-group10s-teamproject_financial_software)
    * [Getting started](#getting-started)
    * [Contents](#contents)
    * [functions](#functions)
        + [main.py](#mainpy)
        + [stat_players.py](#stat_playerspy)
        + [calcul_score.py](#calcul_scorepy)
        + [make_excel.py](#make_excelpy)
        + [poisson_distribution.py](#poisson_distributionpy)
        + [Pannel.py](#Pannelpy)
    
    
## functions
함수들의 기능에 대해서 간략하게 작성하였습니다.

---

### main.py
> 함수 총괄(사용자 입력, 다른 method 호출 및 종료 등)

**Prototype Declaration**
```python
def    main()
```

**Description**

선수 스탯 random을 선택 시
stat_players.py의 set_start_random('팀 name') 호출  
선수 스탯 auto를 선택 시
stat_players.py의 set_start_auto('팀 name') 호출

스탯 합산 및 결과(슈팅, 패스, 점유율, 선방횟수) 계산을 위한
calcul_score.py의 Calculate('팀1 kor_name', '팀2 kor_name')와 get_result() 호출

엑셀에 결과를 저장하기 위한 make_excel.py의 Make_Excel('팀1 eng_name', '팀2 eng_name', '경기결과 result_dict변수') 호출

모든 결과를 pannel에 출력시키기 위한 Pannel.py의 initGame('팀 1 kor_name', '팀 2 kor_name') 호출
pannel의 동작을 위한 runGame('경기결과 result_dict변수') 호출  

**Return**

함수의 종료
<div align = "right">
    <b><a href = "#Contents">back to the top</a><b>
        </div>

---
### stat_players.py
> 선수들 능력치 할당(랜덤 or auto)

**Prototype Declaration**
```python
class Player:                                   # 각 선수 객체
    def __init__(self, p_name, p_position):     # 변수 선언
    def set_stat_random(self):                  # 스탯 random할당
    def set_stat_auto(self):                    # 스탯 auto할당(웹 스크랩)
    def print_player_info(self):                # 선수 스탯 정보 출력
def set_start_random(team1):                    # 선수 생성 및 set_stat_random호출
def set_start_auto(team1):                      # 선수 생성 및 set_stat_auto호출
```

**Description**


class Player는 말 그대로 각 팀에 속해있는 선수 하나의 객체를 의미

사용자가 입력한 스탯 할당 방식에 따라 선수들의 스탯을 할당

맨 처음 main에서 랜덤하게 설정한다고 하면, set_start_random()을 호출
이 메서드는 다시 클래스의 set_stat_random()을 활용

반면에, 오토(웹 스크랩 방식)로 설정한다고 하면, main에서 set_start_auto()를 호출
이 메서드는 다시 클래스의 set_stat_auto()를 활용

할당 결과를 사용자에게 확인시키기 위해 print_player_info를 통해 팀 내의 선수 전부의 스탯을 print  

**set_stat_auoto의 중요 기능인 웹 스크랩**
```python
    def set_stat_auto(self):
        # 선수들의 정보를 얻기 위해 각각의 선수에 맞는 url 조작
        url = 'https://www.futbin.com/21/players?page=1&search=' + self.p_name
        response = requests.get(url)
        # BeautifulSoup을 활용해서 Html 소스를 가져옴
        soup = BeautifulSoup(response.content, 'lxml')
        # 홈페이지 엤는 table 을 찾는 과정. 해당 table 이름이 홈페이지에 있는 선수들 스탯 창을 의미함
        table = soup.find("table",
                          {"class": "table table-bordered table-hover table-responsive w-100 d-block d-md-table"})
        # tr 에 있는 td 를 찾아 거기에 포함된 text 들을 data list 에 저장. 이 값들이 스탯 창에 있는 이용하고자 하는 수치 의미.
        data = []
        for a in table.find_all("tr"):
            for b in a.find_all("td"):
                data.append(b.get_text())

        # 포지션도 피파 홈페이지에 있는 포지션으로 할당. data[2]에 저장되어 있음.
        # 다른 선수들 능력치도 data에 저장되어 있는 값을 index로 활용가능.
        self.p_position = data[2]
        [생략]
```

  
**Return**  

스탯이 할당된 선수들 객체가 담긴 list인 p_list 반환
<div align = "right">
    <b><a href = "#Contents">back to the top</a><b>
        </div>

---

### calcul_score.py
> 종합된 선수들의 스탯을 활용하여, 경기 결과 도출

**Prototype Declaration**
```python
class Calculate:
    def __init__(self, team_stat_1, team_stat_2):   # 선수들 스탯 합산을 위한 변수들 선언
    def calculate_sum(self):                        # 선수들의 스탯 합산
    def calculate_shoot(self):                      # 두 팀간의 슈팅, 선방횟수, 골 계산
    def calculate_possession(self):                 # 점유율 
    def calculate_pass(self):                       # 패스 횟수
    def get_result(self):                           # 위의 메소드들을 호출
```

**Description**  

calculte_sum은 팀 내 선수들의 스탯을 특성대로('패스', '슈팅', '드리블' 등) 합산

calculte_shoot은 스탯의 일부를 합산하여 team1과 team2 간의 슈팅, 선방횟수, 골을 계산함. 이를 위한 자체 알고리즘 이용

calculte_possession은 선수들의 대부분의 스탯을 합산하여 %로 비교

calculate_pass는 스탯 중 '패스', '드리블', '주력', '체력'의 합산과 '수비' * 2 , '주력', '체력' 간의 비교를 진행

get_result는 위 4개의 method를 호출함  


**Return**

result_dict을 반환함. 
ex) result_dict["패스"] 는 패스에 관한 두 팀의 결과 값이 할당되어 있음

<div align = "right">
    <b><a href = "#Contents">back to the top</a><b>
        </div>
---

### make_excel.py
> 직접 도출한 결과, 푸아송 분포를 통해 예측되는 결과, 과거의 결과를 엑셀에 

**Prototype Declaration**
```python
void    main()
```
**Description**
메모리 영역 초기화

**Return**
메모리 영역 반환

<div align = "right">
    <b><a href = "#Contents">back to the top</a><b>
        </div>

---

### poisson_distribution.py
> 푸아송 분포를 통해 두 팀간의 스코어 확률을 예측함.

**Prototype Declaration**
```python
void    main()
```
**Description**
메모리 영역 초기화

**Return**
메모리 영역 반환

<div align = "right">
    <b><a href = "#Contents">back to the top</a><b>
        </div>

---

### Pannel.py
> 결과들을 pygame을 통해서 시각적으로 표현함

**Prototype Declaration**
```python
void    main()
```
**Description**
메모리 영역 초기화

**Return**
메모리 영역 반환

<div align = "right">
    <b><a href = "#Contents">back to the top</a><b>
        </div>

---
