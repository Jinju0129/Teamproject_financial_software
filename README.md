# Welcome to the Teamproject_financial_software!!

금융 소프트웨어 팀 프로젝트용 repository입니다.

참가자: 맹진주, 김예진, 우용승

해당 프로젝트는 windows10에서 진행하였으며 Microsoft excel이 필요합니다.

작성자는 office16버전에서 진행하였으며, 타 버전은 확인해보지 못했으나, 프로젝트 진행 오류시 16버전으로 설치 뒤 진행해보길 바랍니다

------------------------------------
### 주제: 랜덤 능력치와 FIFA게임 능력치를 활용한 축구 결과 시나리오 예측
알고리즘을 직접 제작함으로써 축구 경기 결과 예측을 제공하면서 푸아송 분포 및 과거의 기록들로부터 예상되는 결과도 제공합니다.
사용자로부터 선수들의 능력치를 랜덤으로 할지, auto로 설정할지(게임사이트를 통한 웹 스크랩)를 정해서
경기 결과를 도출하며, 사용자의 흥미도를 높이기 위해결과를 엑셀 파일과 pygame을 통한 gamepad로 출력합니다.
경기 도출 방식을 정교하게 함에 더해서 머신러닝을 가세한다면 더욱 정확한 결과를 도출해낼 수 있을 것입니다.

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

    ```shell
    git clone https://github.com/WooYongSeung/Teamproject_financial_software.git
    ```

2. Pycharm으로 해당 프로젝트를 open한 뒤, pycharm 하단 부분의 Terminal을 누르고 다음을 입력합니다

    ```shell
    pip install -U -r requirements.txt
    에러시 pip install --upgrade pip를 진행한 뒤, 재입력합니다
    그래도 에러시 pip install -r requirements.txt를 입력합니다
    ```

3. main.py에서 프로그램을 실행합니다.

    ```shell
    main.py에서 빈 공간에 우클릭 한 뒤, Run 'main'하시면 됩니다
    ```

## Contents
- [Welcome to the Teamproject_financial_software !!](#welcome-to-the-teamproject_financial_software)
    * [Getting started](#getting-started)
    * [Contents](*contents)
    * [functions](*functions)
        + [main.py](#mainpy)
        + [stat_players.py](#stat_playerspy)
        + [calcul.py](#calcul_py)
        + [make_excel.py](#make_excelpy)
        + [poisson_distribution.py](#poisson_distributionpy)
        + [Pannel.py](#Pannelpy)
    
    
## functions
함수들의 기능에 대해서 간략하게 작성하였습니다.

---

### main.py
> 함수 총괄

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
### stat_players.py
> 선수들 능력치 할당(랜덤 or auto)

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

### calcul_score.py
> 종합된 선수들의 스탯을 활용하여, 경기 결과 도출

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
