from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(HeadlessClient):
    def init(self):
        self.name = '卍ˋ煞氣a呃ˊ卍'  # 設定名稱

    def action(self, hero, heroes, polygons, bullets):
        print("I'm", hero)
        print(f'level: {hero.level}',
              f'experience: {hero.experience}/{hero.experience_to_level_up}')
        print("I'm surrounded by these polygons:", polygons)
        print("I'm surrounded by these heroes:", heroes)
        print("I'm surrounded by these bullets:", bullets)
        print('-' * 79)

        if hero.level > 22 and hero.health > hero.abilities.max_health.value * 5 / 12:
            if heroes:
                for i in range(0, len(heroes)):
                    if heroes[i].health < hero.health:

                        self.shoot_at(*heroes[i].position)
                        self.accelerate_towards(*heroes[i].position)
                    else:
                        self.shoot_at(*heroes[i].position)
                        self.accelerate_towards(5000 - heroes[i].position[0],
                                                4000 - heroes[i].position[1])
            else:
                if polygons:
                    if hero.health < hero.abilities.max_health.value * 2 / 3:
                        self.shoot_at(*polygons[0].position)
                        self.accelerate_towards(*hero.position)
                    else:
                        self.shoot_at(*polygons[0].position)
                        self.accelerate_towards(*polygons[0].position)
        else:
            if heroes:
                self.accelerate_towards(5000 - heroes[0].position[0],
                                        4000 - heroes[0].position[1])
            if polygons:
                if hero.health < hero.abilities.max_health.value * 2 / 3:
                    self.shoot_at(*polygons[0].position)
                    self.accelerate_towards(*hero.position)
                else:
                    self.shoot_at(*polygons[0].position)
                    self.accelerate_towards(*polygons[0].position)

        if hero.skill_points > 0:
            self.level_up(Ability.HealthRegen)
            if hero.abilities.health_regen.level == 8:
                self.level_up(Ability.MaxHealth)
                if hero.abilities.max_health.level == 8:
                    self.level_up(Ability.BodyDamage)
                    if hero.abilities.body_damage.level == 8:
                        self.level_up(Ability.MovementSpeed)
                        if hero.abilities.movement_speed.level == 8:
                            self.level_up(Ability.Reload)
                            if hero.abilities.reload.level == 8:
                                self.level_up(Ability.BulletDamage)
                                if hero.abilities.bullet_damage.level == 8:
                                    self.level_up(Ability.BulletPenetration)
                                    if hero.abilities.bullet_penetration.level == 8:
                                        self.level_up(Ability.BulletSpeed)


#priority = ['health', 'damage']
#for i in range(0,len(priority))
#if hero.abilities.priority[i] > 0:
#self.level_up(Ability.priority[i])

Client.main()
