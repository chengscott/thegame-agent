from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient
import random


class Client(GuiClient):

    def init(self):
        self.name = '清眼究極龍' # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(
            f'level: {hero.level}',
            f'experience: {hero.experience}/{hero.experience_to_level_up}'
        )

        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)

        if heroes:
            opp=0
            d=(hero.position[0]-(heroes[0].position[0]))**2+(hero.position[1]-(heroes[0].position[1]))**2
            for i in range(1,len(heroes)):
                if d>(hero.position[0]-heroes[i].position[0])**2+(hero.position[1]-heroes[i].position[1]):
                    d=(hero.position[0]-heroes[i].position[0])**2+(hero.position[1]-heroes[i].position[1])
                    opp=i
            if hero.health<=heroes[opp].health:
                self.accelerate_towards(1.3*(2*hero.position[0]-heroes[opp].position[0]),0.8*(2*hero.position[1]-heroes[opp].position[1]))
                self.shoot_at(*heroes[opp].position)
            elif hero.abilities.body_damage.level>heroes[opp].abilities.body_damage.level:
                self.accelerate_towards(*heroes[opp].position)
                self.shoot_at(*heroes[opp].position)
        if polygons:
            pd=(hero.position[0]-polygons[0].position[0])**2+(hero.position[1]-polygons[0].position[1])**2
            ply=0
            for i in range(1,len(polygons)):
                if pd>(hero.position[0]-polygons[i].position[0])**2+(hero.position[1]-polygons[i].position[1]):
                    pd=(hero.position[0]-polygons[i].position[0])**2+(hero.position[1]-polygons[i].position[1])
                    ply=i
            self.shoot_at(*polygons[ply].position)
            if hero.health>0.5*hero.abilities.max_health.value:
                self.accelerate_towards(*polygons[ply].position)


        if hero.skill_points>0:
            ra=random.randint(0,25)
            if 0<=ra<=3:
                self.level_up(Ability.BulletSpeed)
            elif 14<=ra<=17:
                self.level_up(Ability.MaxHealth)
            elif 18<=ra<=23:
                self.level_up(Ability.BulletDamage)
            elif 9<=ra<=13:
                self.level_up(Ability.BodyDamage)
            elif ra==24:
                self.level_up(Ability.MaxHealth)
            elif ra==25:
                self.level_up(Ability.HealthRegen)
            elif 4<=ra<=8:
                self.level_up(Ability.HealthRegen)
Client.main()
