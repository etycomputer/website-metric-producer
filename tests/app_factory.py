from app import producer, database, kafka
from app.producer import Producer
from app.database import MyPostgresDB
from app.kafka import MyKafkaProducer, MyKafkaConsumer


def build_production_app() -> Producer:
    app = producer.create_producer()
    return app


def build_postgres_db(test_mode=True) -> MyPostgresDB:
    db = database.create_postgres_db(test_mode)
    return db


def build_kafka_producer(test_mode=True) -> MyKafkaProducer:
    kafka_p = kafka.create_kafka_producer(test_mode)
    return kafka_p


def build_kafka_consumer(test_mode=True) -> MyKafkaConsumer:
    kafka_c = kafka.create_kafka_consumer(test_mode)
    return kafka_c
