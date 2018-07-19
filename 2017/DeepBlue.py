from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):

    def init(self):
        self.name = 'DeepBlue' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)
        if polygons:
            polydis=[]
            for i1 in range(0,len(polygons)):
                polydis.append(0)
            for j1 in range(0,len(polygons)):
                polydis[j1]=((polygons[j1].position[0]-hero.position[0])**2+(polygons[j1].position[1]-hero.position[1])**2)**0.5
                print(polydis)
                if len(polydis) >=0:
                    minpolydis = min (polydis)
            for k1 in range(0,len(polygons)):
                if polydis[k1] == minpolydis:
                    break

            enemydis=[]
            for x1 in range(0,len(heroes)):
                enemydis.append(0)
            for y1 in range(0,len(heroes)):
                enemydis[y1]=((heroes[y1].position[0]-hero.position[0])**2+(heroes[y1].position[1]-hero.position[1])**2)**0.5
                if len(enemydis) >= 0:
                    minenemydis = min (enemydis)
            for z1 in range(0,len(heroes)):
                if enemydis[z1] == minenemydis:
                    break
            import random
            x=(random.randint(-300,300))
            y=(random.randint(-300,300))
            if heroes and enemydis[z1]-polydis[k1]<=1000 :
                enemydis=[]
                for x1 in range(0,len(heroes)):
                    enemydis.append(0)
                for y1 in range(0,len(heroes)):
                    enemydis[y1]=((heroes[y1].position[0]-hero.position[0])**2+(heroes[y1].position[1]-hero.position[1])**2)**0.5
                    if len(enemydis) >= 0:
                        minenemydis = min (enemydis)
                for z1 in range(0,len(heroes)):
                    if enemydis[z1] == minenemydis:
                        break
                enemylv=[]
                for p in range(0,len(heroes)):
                    enemylv.append(0)
                for q in range(0,len(heroes)):
                    enemylv[q]=heroes[q].level
                maxenemylv = max(enemylv)
                minenemylv = min(enemylv)
                for r in range(0,len(heroes)):
                    if enemylv[r] == maxenemylv:
                        break
                for s in range (0,len(heroes)):
                    if enemylv[s] == minenemylv:
                        break

                polydis=[]
                for i1 in range(0,len(polygons)):
                    polydis.append(0)
                for j1 in range(0,len(polygons)):
                    polydis[j1]=((polygons[j1].position[0]-hero.position[0])**2+(polygons[j1].position[1]-hero.position[1])**2)**0.5
                    print(polydis)
                    if len(polydis) >=0:
                        minpolydis = min (polydis)
                for k1 in range(0,len(polygons)):
                    if polydis[k1] == minpolydis:
                        break

                ft= enemydis[z1]/hero.abilities.bullet_speed.value

                if minenemydis >= 100 and enemylv[r]-hero.level<1 and hero.level> 5 :
                    self.accelerate_towards(heroes[z1].position[0],heroes[z1].position[1])
                    self.shoot_at ((heroes[z1].position[0]),(heroes[z1].position[1]))
                    if minenemydis <= 50 and enemylv[r]-hero.level<1  :
                        self.accelerate_towards(-(heroes[z1].position[0]),-(heroes[z1].position[1]))
                        self.shoot_at ((heroes[z1].position[0]),(heroes[z1].position[1]))
                if minenemydis >= 100 and enemylv[r]-hero.level>=1:
                    self.accelerate_towards(-(heroes[z1].position[0]),-(heroes[z1].position[1]))
                    self.shoot_at ((heroes[z1].position[0]) ,(heroes[z1].position[1]))

            if polygons :
                polydis=[]
                for i1 in range(0,len(polygons)):
                    polydis.append(0)
                for j1 in range(0,len(polygons)):
                    polydis[j1]=((polygons[j1].position[0]-hero.position[0])**2+(polygons[j1].position[1]-hero.position[1])**2)**0.5
                    print(polydis)
                    if len(polydis) >=0:
                        minpolydis = min (polydis)
                for k1 in range(0,len(polygons)):
                    if polydis[k1] == minpolydis:
                        break

                if minpolydis >=150:
                    self.accelerate_towards((polygons[k1].position[0])+x,(polygons[k1].position[1])+x)
                    self.shoot_at (polygons[k1].position[0],polygons[k1].position[1])
                if minpolydis <=150:
                    self.accelerate_towards(-(polygons[k1].position[0]),-(polygons[k1].position[1]))
                    self.shoot_at (polygons[k1].position[0],polygons[k1].position[1])


        i=1
        while i<=16:
            if hero.abilities.health_regen.level <= hero.abilities.max_health.level:
                self.level_up (0)
            elif hero.abilities.health_regen.level > hero.abilities.max_health.level:
                self.level_up (1)
            i=i+1
            if hero.abilities.max_health.level>=2:
                self.level_up (2)
        if hero.abilities.body_damage.level>=4:
            self.level_up(6)
        if hero.abilities.reload.level>=2:
           self.level_up (5)

        if hero.abilities.bullet_damage.level >=4:
             if hero.abilities.movement_speed.level <= hero.abilities.bullet_speed.level:
                 self.level_up (7)
             elif hero.abilities.movement_speed.level>hero.abilities.bullet_speed.level:
                 self.level_up (3)


Client.main()