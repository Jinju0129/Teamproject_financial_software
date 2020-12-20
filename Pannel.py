import pygame

# 색과 pad의 크기 선언
WHITE = (255, 255, 255)
transparent = (0, 0, 0, 0)
pad_width = 1600
pad_height = 900


# 블럭 형태의 오브젝트 생성 위한 클래스
class Block(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()


# 주 gamepad 막대, image 등을 활용하여 결과 표시
class Pannel:
    def pannel(self, result_dict):

        # 하이푼, 상단 배너 load
        hyphen_image = pygame.image.load('images/hyphen.png')
        top_banner = pygame.image.load('images/test.png')

        # tob_banner 위치 및 크기 설정
        gamepad.blit(top_banner, (0, 0.01))

        # 막대 그래프 표시를 위한 block 객체 할당을 위한 block_width_list 생성
        # block_width_list 에는 골, 패스 등의 비율 값이 저장되어 막대를 load 할 때 width 로써 사용함
        # temp_list 는 데이터 파싱 과정에서 유의미한 값들을 저장하고자 선언
        block_width_list = []
        temp_list = []

        # 메인 상단의 스코어 출력을 위한 이미지 load. gamepad의 blit을 이용하여 위치를 설정해줌
        number_image_team1 = pygame.image.load("images/number_" + result_dict["goal"][0] + ".png")
        number_image_team2 = pygame.image.load("images/number_" + result_dict["goal"][1] + ".png")
        gamepad.blit(number_image_team1, (600, 150))
        gamepad.blit(number_image_team2, (900, 150))
        gamepad.blit(hyphen_image, (780, 210))

        # 중간 부분의 글자 부분 text 출력 부분
        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("유효 공격 포인트", True, (0, 0, 0))
        gamepad.blit(text, [730, 370])

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("패스 횟수", True, (0, 0, 0))
        gamepad.blit(text, [770, 500])

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("골 점유율", True, (0, 0, 0))
        gamepad.blit(text, [770, 630])

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("선방 or 차단 횟수", True, (0, 0, 0))
        gamepad.blit(text, [730, 760])

        # Team1의 골(유효 공격) 형식으로 text 로 출력
        key_value = result_dict["goal"][0] + "(" + result_dict["shoot"][0] + ")"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [190, 430])

        # 막대의 길이를 연산하기 위한 작업. 전체 비율과 비교
        if int(result_dict["goal"][0] == 0) and int(result_dict["goal"][1] == 0):
            block_width_list.append(0.5)
        else:
            block_width = int(result_dict["goal"][0]) / (int(result_dict["goal"][0]) + int(result_dict["goal"][1]))
            block_width_list.append(block_width)

        # Team1의 패스 횟수 text 로 출력
        key_value = result_dict["pass"][0]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [160, 560])

        # result_dict["pass"] 에 저장되어 있는 값에서 value 만 추출하고자 파싱
        temp_list.append(result_dict["pass"][0].replace('(', ' ').split(" ")[0])
        temp_list.append(result_dict["pass"][1].replace('(', ' ').split(" ")[0])

        block_width = int(temp_list[0]) / (int(temp_list[0]) + int(temp_list[1]))
        block_width_list.append(block_width)

        # Team1의 점유율 text 로 출력
        key_value = result_dict["possession"][0] + "%"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [160, 690])

        # result_dict["possession"]은 퍼센테이지 값이 숫자로 저장되어 있으므로, 0.01곱해서 비율을 바로 저장
        block_width = float(result_dict["possession"][0]) * 0.01
        block_width_list.append(block_width)

        # Team1의 선방횟수 text 로 출력
        key_value = result_dict["save"][0]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [200, 820])
        if int(result_dict["save"][0]) == 0 and int(result_dict["save"][1]) == 0:
            block_width_list.append(0.5)
        else:
            block_width = int(result_dict["save"][0]) / (int(result_dict["save"][0]) + int(result_dict["save"][1]))
            block_width_list.append(block_width)

        # Team2의 골(유효공격) 형식으로 text 로 출력. 이하과정은 Team1 설정과 같다.
        key_value = result_dict["goal"][1] + "(" + result_dict["shoot"][1] + ")"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1400, 430])

        # Team2의 패스 횟수 text 로 출력
        key_value = result_dict["pass"][1]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1360, 560])

        # Team2의 점유율 text 로 출력
        key_value = result_dict["possession"][1] + "%"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1360, 690])

        # Team2의 선방횟수 text 로 출력
        key_value = result_dict["save"][1]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1400, 820])

        # 초록색과 연두색의 막대의 이미지 로드. convert() 를 통해 로드 속도 향상
        pic_1 = pygame.image.load("images/green_bar.png").convert()
        pic_2 = pygame.image.load("images/yellow_bar.png").convert()

        # pygame 의 모든 sprite 을 Group 으로 통제
        block_list = pygame.sprite.Group()

        # 연두와 초록색 막대 너비 조정하는 부분. 총 출력 라인 수가 4 줄이므로 for 문과 width 길이를 저장했던 block_width_list 사용
        for i in range(0, 4):

            # 초록 바와 옐로의 바의 크기를 바꾸어줌.
            # 너비는 골, 패스, 선방 횟수 등의 Team1과 Team2 간의 비율로 설정했던 block_width_list 활용
            pic_1 = pygame.transform.scale(pic_1, (int(800 * block_width_list[i]), 80))
            pic_2 = pygame.transform.scale(pic_2, (int(800 - 800 * block_width_list[i]), 80))

            # pic_1 은 초록 바로 block 객체로 생성
            block_1 = Block(pic_1)

            # block_1과 block_2 객체의 화면 위에 나타날 위치 설정하고 block_list 에 추가
            block_1.rect.x = 420
            block_1.rect.y = 400 + i * 130
            block_list.add(block_1)

            block_2 = Block(pic_2)
            block_2.rect.x = 420 + 800 * block_width_list[i]
            block_2.rect.y = 400 + i * 130
            block_list.add(block_2)

        # block 객체들이 저장되어 있는 block_list 를 gamepad 위에 draw 함.
        block_list.draw(gamepad)

    # flag_1는 Team1의 팀 마크
    def flag_1(self, x, y):
        gamepad.blit(flag_craft_1, (x, y))

    # flag_2는 Team2의 팀 마크
    def flag_2(self, x, y):
        gamepad.blit(flag_craft_2, (x, y))

    # pygame 의 event 처리. pygame 이 종료될 때까지 유지시키는 것으로 while 문으로 구현
    def runGame(self, result_dict):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
            # gamepad 를 흰색으로 채우고, 각 팀의 마크를 위치시킴. flip 은 update 비슷한 동작.
            gamepad.fill(WHITE)
            self.pannel(result_dict)
            self.flag_1(100, 100)
            self.flag_2(1300, 100)
            pygame.display.flip()
        # 종료 이벤트가 발생하면 quit 시킴
        pygame.quit()

    def initGame(self, flag_1, flag_2):
        global gamepad, flag_craft_1, flag_craft_2
        # pygame 라이브러리 초기화
        pygame.init()

        # 특정 크기 스크린 생성, 좌 상단 캡션을 'PySoccer'로 설정
        gamepad = pygame.display.set_mode((pad_width, pad_height))
        pygame.display.set_caption('PySoccer')

        # 이미지 로드, convert 사용해서 더 빠르게 변환
        flag_craft_1 = pygame.image.load("images/" + flag_1 + ".jpg").convert()
        flag_craft_2 = pygame.image.load("images/" + flag_2 + ".jpg").convert()
