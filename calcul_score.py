import random

# 받아온 선수들의 스탯을 활용하여, 종합적으로 합산하고 팀 자체의 패스 성공율, 슈팅횟수, 선방횟수, 점유율 등을 구하는 클래스
class Calculate:
    def __init__(self, team_stat_1, team_stat_2):
        self.team_stat_1 = team_stat_1
        self.team_stat_2 = team_stat_2
        self.team_1_sum_dict = {"패스" : 0, "슈팅": 0, "드리블": 0, "주력": 0, "수비": 0, "체력": 0}
        self.team_2_sum_dict = {"패스" : 0, "슈팅": 0, "드리블": 0, "주력": 0, "수비": 0, "체력": 0}
        self.team_1_GK = 0
        self.team_2_GK = 0
        self.result_dict = {}

    # 각 선수들의 능력치들을 같은 능력치대로 합하는 메소드. 합한 능력치들로 결과를 도출시키기 위함.
    def caclulate_sum(self):
        for i in self.team_stat_1:
            if i.p_position != 'GK':
                self.team_1_sum_dict["패스"] = self.team_1_sum_dict["패스"] + i.stat_dict["패스"]
                self.team_1_sum_dict["슈팅"] = self.team_1_sum_dict["슈팅"] + i.stat_dict["슈팅"]
                self.team_1_sum_dict["드리블"] = self.team_1_sum_dict["드리블"] + i.stat_dict["드리블"]
                self.team_1_sum_dict["주력"] = self.team_1_sum_dict["주력"] + i.stat_dict["주력"]
                self.team_1_sum_dict["수비"] = self.team_1_sum_dict["수비"] + i.stat_dict["수비"]
                self.team_1_sum_dict["체력"] = self.team_1_sum_dict["체력"] + i.stat_dict["체력"]
            else:
                self.team_1_GK = i.stat_dict['반사신경'] +i.stat_dict['볼 핸들링'] + i.stat_dict['골킾'] + i.stat_dict['공중볼'] + \
                                 i.stat_dict['수비조율'] + i.stat_dict['공던지기']
        for i in self.team_stat_2:
            if i.p_position != 'GK':
                self.team_2_sum_dict["패스"] = self.team_2_sum_dict["패스"] + i.stat_dict["패스"]
                self.team_2_sum_dict["슈팅"] = self.team_2_sum_dict["슈팅"] + i.stat_dict["슈팅"]
                self.team_2_sum_dict["드리블"] = self.team_2_sum_dict["드리블"] + i.stat_dict["드리블"]
                self.team_2_sum_dict["주력"] = self.team_2_sum_dict["주력"] + i.stat_dict["주력"]
                self.team_2_sum_dict["수비"] = self.team_2_sum_dict["수비"] + i.stat_dict["수비"]
                self.team_2_sum_dict["체력"] = self.team_2_sum_dict["체력"] + i.stat_dict["체력"]
            else:
                self.team_2_GK = i.stat_dict['반사신경'] + i.stat_dict['볼 핸들링'] + i.stat_dict['골킾'] + i.stat_dict['공중볼'] + \
                                 i.stat_dict['수비조율'] + i.stat_dict['공던지기']

    # 합한 능력치 따라 선방 횟수와 유효 공격 포인트, 골 넣는 횟수를 구하는 메소드
    # 슈팅의 경우, 공격 수치 < 수비 수치면 수비 성공으로 간주해 save_count 를 가산하였고, 그렇지 않으면 공격수가 수비수를 뚫었다고 생각해
    # 공격수 한 선수의 평균 스탯을 합산 스코어/10 을 해서 구한 뒤, 골키퍼의 스탯과 random 함수로 비교하며 goal 여부를 파악함
    def calculate_shoot(self):
        team_1_attack = int((self.team_1_sum_dict["슈팅"] + self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] + self.team_1_sum_dict["주력"] +self.team_1_sum_dict["체력"])/5)
        team_2_defense = int((self.team_2_sum_dict["수비"] + self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] + self.team_2_sum_dict["주력"] +self.team_2_sum_dict["체력"])/5)
        team_2_attack = int((self.team_2_sum_dict["슈팅"] + self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] +
                             self.team_2_sum_dict["주력"] + self.team_2_sum_dict["체력"]) / 5)
        team_1_defense = int((self.team_1_sum_dict["수비"] + self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] +
                              self.team_1_sum_dict["주력"] + self.team_1_sum_dict["체력"]) / 5)

        print("team_1의 공격 값: %.3f" % team_1_attack)
        print("team_2의 공격 값: %.3f" % team_2_attack)
        print("team_1의 수비 값(골키퍼 제외): %.3f" % team_1_defense)
        print("team_2의 수비 값(골키퍼 제외): %.3f" % team_2_defense)
        print("team_1의 GK: %.3f" % self.team_1_GK)
        print("team_2의 GK: %.3f" % self.team_1_GK)

        save_count = 0
        goal_team_1 = 0
        goal_team_2 = 0
        save_team_1 = 0
        save_team_2 = 0

        # team1의 공격에 관한 것. 적당한 횟수로 파악하고자 100회 반복을 시켰음
        for i in range(0, 100):
            attack_range = random.randrange(1, team_1_attack)
            defense_range = random.randrange(1, team_2_defense)

            # 공격 수치보다 수비 수치가 높으면 save_count 를 증가시킴
            if attack_range <= defense_range:
                save_count = save_count + 1
            else:
                # 선수들의 평균 슈팅을 GK의 합으로 나눈다음 100을 곱하면 골을 넣을 확률이 됨. 여기다가 다시 100을 넣어서 range(0, 100)과 비교
                # 수비력에 대한 슈팅 percentage
                shoot_range = int(((self.team_1_sum_dict["슈팅"]/10) / (self.team_2_sum_dict["수비"]/10 )) * 100 )
                if random.randrange(1, int(shoot_range)) >= random.randrange(1, self.team_2_GK):
                    goal_team_1 = goal_team_1 + 1
                else:
                    save_team_2 = save_team_2 + 1
                if goal_team_1 >= 10:
                    i = 0
                    goal_team_1 = 0
                    save_count = 0
                    continue

        shoot_count_1 = save_count - goal_team_1
        if shoot_count_1 > 0:
            shoot_count_1 = random.randrange(goal_team_1, shoot_count_1)
        else:
            shoot_count_1 = random.randrange(save_count, goal_team_1)

        save_count = 0
        # team2의 공격에 관한 것. 이하 동작은 team1 과 같음
        for i in range(0, 100):
            attack_range = random.randrange(1, team_2_attack)
            defense_range = random.randrange(1, team_1_defense)
            if attack_range <= defense_range:
                save_count = save_count + 1
            else:
                # 선수들의 평균 슈팅을 GK의 합으로 나눈다음 100을 곱하면 골을 넣을 확률이 됨. 여기다가 다시 100을 넣어서 range(0, 100)과 비교
                # 수비력에 대한 슈팅 percentage
                shoot_range = int(((self.team_2_sum_dict["슈팅"] / 10) / (self.team_1_sum_dict["수비"] / 10)) * 100)
                if random.randrange(1, int(shoot_range)) >= random.randrange(1, self.team_1_GK):
                    goal_team_2 = goal_team_2 + 1
                else:
                    save_team_1 = save_team_1 + 1
                if goal_team_2 >= 10:
                    i = 0
                    goal_team_2 = 0
                    save_count = 0
                    continue
        shoot_count_2 = save_count - goal_team_2
        if shoot_count_2 > 0:
            shoot_count_2 = random.randrange(goal_team_2, shoot_count_2)
        else:
            shoot_count_2 = random.randrange(save_count, goal_team_2)
        print("save_count %d " % save_count)
        print("TEAM1 goal, TEAM2save %d %d" % (goal_team_1, save_team_2))
        print("TEAM2 goal, TEAM1save %d %d" % (goal_team_2, save_team_1))

        # 계산이 끝난 뒤에는, result_dict[] 에 각각의 결과들을 저장함. index 0 부분이 team_1, index 1 부분이 team_2의 value 들임
        self.result_dict["goal"] = [str(goal_team_1), str(goal_team_2)]
        self.result_dict["save"] = [str(save_team_1), str(save_team_2)]
        self.result_dict["shoot"] = [str(shoot_count_1), str(shoot_count_2)]

    # 팀들의 점유율을 구하기 위한 메소드
    def calculate_possession(self):
        team_1_sum = int((self.team_1_sum_dict["슈팅"] + self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] +
                          self.team_1_sum_dict["주력"] + self.team_1_sum_dict["체력"] + self.team_1_sum_dict["수비"]) / 6)
        team_2_sum = int((self.team_2_sum_dict["수비"] + self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] +
                          self.team_2_sum_dict["주력"] + self.team_2_sum_dict["체력"] + self.team_2_sum_dict["슈팅"]) / 6)
        # 점유율의 경우 경기의 종합적인 면이 강하게 작용하므로, 필드 선수들의 능력치를 종합하는 것으로 계산함
        possession_team_1 = format(team_1_sum / (team_1_sum + team_2_sum) * 100, ".2f")
        possession_team_2 = format(team_2_sum / (team_1_sum + team_2_sum) * 100, ".2f")

        self.result_dict["possession"] = [str(possession_team_1), str(possession_team_2)]

    # 팀들의 패스 횟수를 구하기 위한 메소드
    # 패스의 경우 공격 선수들의 패스, 드리블, 주력, 체력 vs 수비 선수들의 수비, 주력, 체력 을 random 을 활용해서 count함
    def calculate_pass(self):
        pass_count_1 = 0
        pass_false_1 = 0

        pass_count_2 = 0
        pass_false_2 = 0

        pass_team_1 = int((self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] + self.team_1_sum_dict["주력"] +
                           self.team_1_sum_dict["체력"]) / 4)
        pass_team_2 = int((self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] + self.team_2_sum_dict["주력"] +
                           self.team_2_sum_dict["체력"]) / 4)
        pass_defense_team_1 = int((self.team_1_sum_dict["수비"] * 2 + self.team_1_sum_dict["주력"] +
                                   self.team_1_sum_dict["체력"]) / 4)
        pass_defense_team_2 = int((self.team_2_sum_dict["수비"] * 2 + self.team_2_sum_dict["주력"] +
                                   self.team_2_sum_dict["체력"]) / 4)
        # pass 하는 팀과 pass 를 수비하는 팀들 간의 random 을 이용하여 수치 계산
        for i in range(0, random.randrange(100, 300)):
            if random.randrange(1, pass_team_1) > random.randrange(1, pass_defense_team_2):
                pass_count_1 = pass_count_1 + 1
            else:
                pass_false_1 = pass_false_1 + 1
        for i in range(0, random.randrange(100, 300)):
            if random.randrange(1, pass_team_2) > random.randrange(1, pass_defense_team_1):
                pass_count_2 = pass_count_2 + 1
            else:
                pass_false_2 = pass_false_2 + 1
        print("pass_count_1 %d pass_false_1 %d" % (pass_count_1, pass_false_1))
        print("pass_count_2 %d pass_false_2 %d" % (pass_count_2, pass_false_2))
        self.result_dict["pass"] = [str(pass_count_1) + "(" + str(pass_count_1 + pass_false_1) + ")", str(pass_count_2) + "(" + str(pass_count_2 + pass_false_2) + ")"]

    # 위의 메소드들을 구하기 위해 각각 호출하는 메소드. main 에서는 이 메소드만을 호출함
    def get_result(self):
        self.caclulate_sum()
        self.calculate_shoot()
        self.calculate_possession()
        self.calculate_pass()

        # result_dict 을 return 함으로써 Pannel 에서 원하는 value 추출을 용이하게 함
        return self.result_dict
