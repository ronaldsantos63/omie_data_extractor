from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from model.data import mapper_registry


class DatabaseManager:
    __engine = create_engine("sqlite:///omie_database.db", echo=True)
    __session_maker: Session = sessionmaker(bind=__engine, future=True)
    __session: Session = __session_maker()

    def create_all_tables(self) -> None:
        with self.__engine.connect() as connection:
            mapper_registry.metadata.create_all(connection)

    def get_all(self, entity) -> object:
        return self.__session.query(entity).all()

    def get_by_filter(self, statement) -> object:
        return self.__session.execute(statement).scalar_one_or_none()

    def add_all(self, entities: list[object]):
        self.__session.add_all(entities)

    def add(self, entity) -> None:
        self.__session.add(entity)
        self.__session.commit()

    def update(self, entity):
        if self.__session.is_modified(entity):
            self.__session.commit()

    def delete_by_filter(self, entity, filter_statement) -> None:
        self.__session.query(entity).filter(filter_statement).delete(synchronize_session=False)
        self.__session.commit()

    def close(self):
        self.__session.close()
