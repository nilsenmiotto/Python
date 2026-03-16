"""Tutorial de primeiro contato com Kafka (kafka-python).

Objetivo:
1. Testar conexao com o broker em localhost:9092.
2. Criar um topico simples.
3. Enviar mensagens como produtor.
4. Ler mensagens como consumidor.

Uso rapido:
python tutorial.py --passo all
python tutorial.py --passo create-topic
python tutorial.py --passo produce --quantidade 10
python tutorial.py --passo consume --quantidade 10
"""

from __future__ import annotations

import argparse
import json
import time

from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError


def aguardar_broker(
    bootstrap_servers: str, tentativas: int = 10, pausa: float = 1.0
) -> None:
    for tentativa in range(1, tentativas + 1):
        try:
            admin = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
            admin.close()
            print(f"Broker acessivel em {bootstrap_servers}.")
            return
        except Exception as erro:
            print(f"Tentativa {tentativa}/{tentativas} falhou: {erro}")
            time.sleep(pausa)

    raise RuntimeError("Nao foi possivel conectar no broker Kafka.")


def criar_topico(bootstrap_servers: str, topico: str) -> None:
    admin = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    try:
        novo_topico = NewTopic(name=topico, num_partitions=1, replication_factor=1)
        admin.create_topics(new_topics=[novo_topico], validate_only=False)
        print(f"Topico criado: {topico}")
    except TopicAlreadyExistsError:
        print(f"Topico ja existe: {topico}")
    finally:
        admin.close()


def produzir_mensagens(bootstrap_servers: str, topico: str, quantidade: int) -> None:
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda valor: json.dumps(valor).encode("utf-8"),
    )

    for indice in range(1, quantidade + 1):
        mensagem = {"id": indice, "texto": f"Mensagem {indice}", "origem": "tutorial"}
        producer.send(topico, mensagem)
        print(f"Enviada: {mensagem}")

    producer.flush()
    producer.close()
    print(f"Total enviado: {quantidade}")


def consumir_mensagens(
    bootstrap_servers: str, topico: str, quantidade: int, grupo: str
) -> None:
    consumer = KafkaConsumer(
        topico,
        bootstrap_servers=bootstrap_servers,
        group_id=grupo,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda valor: json.loads(valor.decode("utf-8")),
        consumer_timeout_ms=5000,
    )

    recebidas = 0
    print("Consumindo mensagens...")
    for mensagem in consumer:
        print(f"Recebida: {mensagem.value}")
        recebidas += 1
        if recebidas >= quantidade:
            break

    consumer.close()
    print(f"Total recebido: {recebidas}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Primeiro contato com Kafka")
    parser.add_argument(
        "--bootstrap", default="localhost:9092", help="Endereco do broker"
    )
    parser.add_argument("--topico", default="primeiro-contato", help="Nome do topico")
    parser.add_argument(
        "--grupo", default="primeiro-contato-group", help="Consumer group"
    )
    parser.add_argument(
        "--quantidade", type=int, default=5, help="Quantidade de mensagens"
    )
    parser.add_argument(
        "--passo",
        choices=["all", "create-topic", "produce", "consume"],
        default="all",
        help="Etapa para executar",
    )
    args = parser.parse_args()

    aguardar_broker(args.bootstrap)

    if args.passo in ("all", "create-topic"):
        criar_topico(args.bootstrap, args.topico)

    if args.passo in ("all", "produce"):
        produzir_mensagens(args.bootstrap, args.topico, args.quantidade)

    if args.passo in ("all", "consume"):
        consumir_mensagens(args.bootstrap, args.topico, args.quantidade, args.grupo)


if __name__ == "__main__":
    main()
