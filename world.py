
class World:
    def __init__(self, tilemap):
        self.tilemap = tilemap

    def able_walk(self, rect):
        if rect.x < 0 or rect.y < 0 or rect.x+rect.w > self.tilemap.view_w or rect.y+rect.h > self.tilemap.view_h:
            return False
        layer = self.tilemap.layers.by_name["Tile Layer 1"]
        cells = layer.collide(rect, "terrain")
        for i in cells:
            if i["terrain"] == 0:
                return False
        return True