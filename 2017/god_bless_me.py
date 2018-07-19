from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):

    def init(self):
        self.name = 'god bless me' # 設定名稱

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
        x=hero.position[0]
        y=hero.position[0]
        print(hero.health)
        if bullets: #子彈
            k={}
            for i in range(0,len(bullets)):
                m=bullets[i].position[0]
                n=bullets[i].position[1]
                k[(x-m)**2+(y-n)**2]=bullets[i]
            if min(k.keys())<15000:
                self.accelerate_towards(5000-k[min(k.keys())].position[0],4000-k[min(k.keys())].position[1])
            if polygons: #圖
                d={}
                for i in range(0,len(polygons)):
                    a=polygons[i].position[0]
                    b=polygons[i].position[1]
                    d[(x-a)**2+(y-b)**2]=polygons[i]
                    self.shoot_at(*d[min(d.keys())].position)
                if min(d.keys())>12000:
                    self.accelerate_towards(*d[min(d.keys())].position)
        else:
            if polygons: #圖
                d={}
                for i in range(0,len(polygons)):
                    a=polygons[i].position[0]
                    b=polygons[i].position[1]
                    d[(x-a)**2+(y-b)**2]=polygons[i]
                    self.shoot_at(*d[min(d.keys())].position)
                if min(d.keys())>1000:
                    self.accelerate_towards(*d[min(d.keys())].position)
        if heroes:
            if hero.level>30 and hero.health>3500:
                j={}
                for i in range(0,len(heroes)):
                    w=heroes[i].position[0]
                    z=heroes[i].position[1]
                    d[(x-w)**2+(y-z)**2]=heroes[i]
                    self.shoot_at(*j[min(j.keys())].position)
                    self.accelerate_towards(*j[min(j.keys())].position)
        for i in range(0,8):
            self.level_up(Ability.HealthRegen)
            self.level_up(Ability.BodyDamage)
            self.level_up(Ability.MaxHealth)
            self.level_up(Ability.BulletDamage)
            self.level_up(Ability.Reload)
            self.level_up(Ability.MovementSpeed)
            self.level_up(Ability.BulletSpeed)
            self.level_up(Ability.BulletPenetration)

Client.main()
