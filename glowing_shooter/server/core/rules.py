from config.default import MAP_SIZE


class PhysicalObjectRules:

    @classmethod
    def x(cls, obj, value):
        return max(0, min(MAP_SIZE, value))

    @classmethod
    def y(cls, obj, value):
        return max(0, min(MAP_SIZE, value))


class SimpleBullet(PhysicalObjectRules):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def x(cls, obj, value) -> []:
        if value < 0:
            obj.to_delete = True
            return 0
        elif value > MAP_SIZE:
            obj.to_delete = True
            return MAP_SIZE
        return value

    @classmethod
    def y(cls, obj, value):
        if value < 0:
            obj.to_delete = True
            return 0
        elif value > MAP_SIZE:
            obj.to_delete = True
            return MAP_SIZE
        return value
