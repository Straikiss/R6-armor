class Player():
    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def hit_body_light(self, health, hits, damage):
        return self.health - ((damage * hits) * 1)

    def hit_body_medium(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.9)

    def hit_body_heavy(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.8)

    def hit_body_light_rook(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.8)

    def hit_body_medium_rook(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.72)

    def hit_body_heavy_rook(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.64)

    def hit_leg_light(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.75)

    def hit_leg_medium(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.675)

    def hit_leg_heavy(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.52)

    def hit_leg_light_rook(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.6)

    def hit_leg_medium_rook(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.54)

    def hit_leg_heavy_rook(self, health, hits, damage):
        return self.health - ((damage * hits) * 0.416)