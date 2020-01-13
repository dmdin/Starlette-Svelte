from tortoise import Model, fields


class Tournament(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()

    def __str__(self):
        return self.name

__models__ = [Tournament, ]
