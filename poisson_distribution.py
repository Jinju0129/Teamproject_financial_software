from math import factorial, exp

# 푸아송 분포를 활용하여 team1 vs team2 일때 각각의 팀들의 과거 기록들을 살피며, score 중 확률이 제일 높은 점수를 도출하기 위한 클래스
class Poisson:
    def __init__(self, team_1_score, team_2_score):
        # 리그의 평균 득점은 1.492이고 평균 실점은 1.207로 고정
        self.league_goalFor = 1.492
        self.league_goalAgainst = 1.207
        # attack 은 팀의 공격력, defense 는 팀의 방어력
        # 팀의 공격력은 해당 팀의 평균 득점 / 리그 평균 득점
        # 팀의 방어력은 해당 팀의 평균 실점 / 리그 평균 실점
        self.team_1_attack = team_1_score / self.league_goalFor
        self.team_1_defense = team_2_score / self.league_goalAgainst
        self.team_2_attack = team_2_score / self.league_goalFor
        self.team_2_defense = team_1_score / self.league_goalAgainst

        # team1의 골 득점 확률은 team1의 공격력 * team2의 방어력 * leage 평균 득점
        self.team_1_goal_pb = self.team_1_attack * self.team_2_defense * self.league_goalFor
        self.team_2_goal_pb = self.team_2_attack * self.team_1_defense * self.league_goalFor

    def get_poisson_list(self):
        team1_poisson_list = []
        team2_poisson_list = []

        # range(0, 10) 을 함으로써 각 팀들이 0골부터 9골까지 넣을 확률을 푸아송 분포로 구했습니다.
        # 이 결과는 make_excel 에서 사용하는데, 각 확률 중 최고의 확률을 보인 것을 찾음으로써 팀의 예상 득점을 구할 수 있습니다.
        for i in range(0, 10):
            team1_poisson_list.append([i, self.result(i, self.team_1_goal_pb)] )
            team2_poisson_list.append( [i, self.result(i, self.team_2_goal_pb)] )
        return team1_poisson_list, team2_poisson_list

    # 푸아송 분포의 식에 대입. 결과를 반환함으로써 위에 get_poisson_list 에 알맞은 값을 추가함
    def result(self, number, win_prob):
        x = number
        miu = win_prob
        poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)

        return poisson_prob
