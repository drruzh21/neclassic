import psycopg
from psycopg import sql


class PostgresRepository:
    def __init__(self, db_config):
        self.connection = psycopg.connect(**db_config)
        self.connection.autocommit = True

    def create_table(self, table_index, headers):
        """
        Создает таблицу с указанным индексом и заголовками атрибутов.

        :param table_index: Индекс таблицы (название).
        :param headers: Массив строк с названиями колонок.
        """
        # Генерируем динамический SQL для создания таблицы
        columns = ", ".join([f"{header} TEXT" for header in headers])
        query = sql.SQL("CREATE TABLE IF NOT EXISTS {} ({})").format(
            sql.Identifier(f"table_{table_index}"),
            sql.SQL(columns)
        )

        with self.connection.cursor() as cursor:
            cursor.execute(query)
        print(f"Таблица table_{table_index} успешно создана.")

    def insert_data(self, table_index, data_batch):
        """
        Вставляет батчи данных в таблицу с указанным индексом.

        :param table_index: Индекс таблицы (название).
        :param data_batch: Массив кортежей с данными для вставки.
        """
        # Предполагаем, что у нас есть данные с нужным количеством колонок
        if not data_batch:
            print("Нет данных для вставки.")
            return

        # Определяем количество колонок по первому кортежу
        placeholders = ", ".join(["%s"] * len(data_batch[0]))
        query = sql.SQL("INSERT INTO {} VALUES ({})").format(
            sql.Identifier(f"table_{table_index}"),
            sql.SQL(placeholders)
        )

        with self.connection.cursor() as cursor:
            cursor.executemany(query, data_batch)
        print(f"Данные вставлены в table_{table_index}.")

    def close(self):
        """
        Закрывает соединение с базой данных.
        """
        self.connection.close()
        print("Соединение с базой данных закрыто.")



# Пример использования
if __name__ == "__main__":
    # Конфигурация подключения к базе данных
    db_config = {
        'dbname': 'neclassic',
        'user': 'neclassic',
        'password': 'neclassic',
        'host': 'localhost',
        'port': 5434
    }

    repo = PostgresRepository(db_config)

    # Создаем таблицу с индексом 1 и заголовками
    headers = ['id', 'name', 'email']
    repo.create_table(1, headers)

    # Вставляем данные батчами
    data = [
        ('1', 'John Doe', 'john.doe@example.com'),
        ('2', 'Jane Doe', 'jane.doe@example.com')
    ]
    repo.insert_data(1, data)

    # Закрываем соединение
    repo.close()
