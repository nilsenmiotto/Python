# Base images
docker pull mysql
docker pull postgres
docker pull mongo

# Reset container/volume to ensure fresh init (needed for MYSQL_DATABASE to take effect)
docker rm -f mysql-local
docker volume rm mysql_data
docker volume create mysql_data

# Start MySQL with initial database creation
docker run -d --name mysql-local --memory 2g --memory-swap 2g -e MYSQL_ROOT_PASSWORD=mudar123 -e MYSQL_DATABASE=meu_banco -p 3306:3306 -v mysql_data:/var/lib/mysql mysql:latest

# Reset container/volume to ensure fresh init (needed for POSTGRES_DB to take effect)
docker rm -f postgres-local
docker volume rm postgres_data
docker volume create postgres_data

# Start PostgreSQL with initial database creation
docker run -d --name postgres-local --memory 2g --memory-swap 2g -e POSTGRES_PASSWORD=mudar123 -e POSTGRES_DB=meu_banco -p 5432:5432 -v postgres_data:/var/lib/postgresql postgres:latest

# Reset container/volume to ensure fresh init (needed for MONGO_INITDB_DATABASE to take effect)
docker rm -f mongo-local
docker volume rm mongo_data
docker volume create mongo_data

# Start MongoDB with initial database creation
docker run -d --name mongo-local --memory 2g --memory-swap 2g -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=mudar123 -e MONGO_INITDB_DATABASE=meu_banco -p 27017:27017 -v mongo_data:/data/db mongo:latest

# Create and connect MySQL container to custom network
docker network create minha-rede
docker network connect minha-rede mysql-local
docker network connect minha-rede postgres-local
docker network connect minha-rede mongo-local