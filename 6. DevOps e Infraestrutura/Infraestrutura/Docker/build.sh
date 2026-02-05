cd "..\..\..\2. Frameworks e Bibliotecas Populares\Web\FastAPI"
docker build -t fastapi-app .
docker run --name fastapi-app -p 8000:8000 fastapi-app

cd "..\..\..\5. Banco de Dados\ORM\SQLAlchemy"
docker build -t sqlalchemy-demo .
docker run --rm --name app --network minha-rede sqlalchemy-demo