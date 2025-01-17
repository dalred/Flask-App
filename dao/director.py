from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Director).get(bid)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def update(self, update):
        self.session.add(update)
        self.session.commit()

    def delete(self, bid):
        director = self.get_one(bid)
        self.session.delete(director)
        self.session.commit()
