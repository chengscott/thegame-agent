from thegame import HeadlessClient, Ability, Polygon, Bullet, Hero
from thegame.gui import GuiClient


class Client(GuiClient):

    def init(self):
        self.name = 'pop' # 設定名稱

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
        if heroes:
            minHealth = 999999
            minPos = (0, 0)
            for p in heroes:
                if p.health <= minHealth:
                    minHealth = p.health
                    minPos = p.position
            self.shoot_at(*minPos)

        else:
            minHealth = 999999
            minPos = (0, 0)
            for p in polygons:
                if p.health <= minHealth:
                    minHealth = p.health
                    minPos = p.position
            self.shoot_at(*minPos)

        if hero.reload_level<7:
            self.level_up(Ability.Reload)
        elif hero.health_regen_level<2:
            self.level_up(Ability.HealthRegen)
        elif hero.bullet_penetration_level<5:
            self.level_up(Ability.BulletPenetration)
        elif hero.reload_level<8:
            self.level_up(Ability.Reload)
        elif hero.health_regen_level<3:
            self.level_up(Ability.HealthRegen)
        elif hero.bullet_damage_level<5:
            self.level_up(Ability.BulletDamage)
        elif hero.health_regen_level<4:
            self.level_up(Ability.HealthRegen)
        elif hero.max_health_level<7:
            self.level_up(Ability.MaxHealth)
        elif hero.body_damage_level<3:
            self.level_up(Ability.BodyDamage)
        elif hero.bullet_penetration_level<6:
            self.level_up(Ability.BulletPenetration)
        elif hero.bullet_damage_level<7:
            self.level_up(Ability.BulletDamage)
        elif hero.health_regen_level<6:
            self.level_up(Ability.HealthRegen)
        elif hero.max_health_level<8:
            self.level_up(Ability.MaxHealth)
        elif hero.bullet_damage_level<8:
            self.level_up(Ability.BulletDamage)
        elif hero.bullet_penetration_level<8:
            self.level_up(Ability.BulletPenetration)
        elif hero.body_damage_level<5:
            self.level_up(Ability.BodyDamage)
        elif hero.health_regen_level<8:
            self.level_up(Ability.HealthRegen)

        if hero.health<=hero.max_health*0.5:
            self.accelerate_towards(*hero.position)

        elif heroes:
            asd = 999999
            MinPos = (0, 0)
            for p in heroes:
                if hero.level <= p.level - 5:
                    MinPos = p.position
            self.accelerate_towards(hero.position[0] * 2 - MinPos[0], hero.position[1] * 2 - MinPos[1])
            #self.accelerate_towards(MinPos[0]-500,MinPos[1]-500)

        else:
            minHealth = 999999
            minPos = (0, 0)
            for p in heroes:
                if p.health <= minHealth:
                    minHealth = p.health
                    minPos = p.position
            self.accelerate_towards(*minPos)
Client.main()