docker rm -f kafka-local
docker volume rm kafka_data
docker volume create kafka_data

docker run -d --name kafka-local --hostname kafka-kraft -p 9092:9092 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_NODE_ID=1 \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka-kraft:9093 \
    -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
    -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
    -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER \
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT \
    -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
    -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 \
    -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 \
    -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 \
    -e CLUSTER_ID=MkU3OEVBNTcwNTJENDM2Qk \
    -v kafka_data:/var/lib/kafka/data \
    -v kafka_data:/etc/kafka/secrets \
    -v kafka_data:/mnt/shared/config \
    apache/kafka:latest