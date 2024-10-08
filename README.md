To work, we need PostgreSQL, which we will run in a docker container.
Instructions for its installation and launching:
docker pull postgres:latest
docker run --name pg_db -e POSTGRES_PASSWORD=postgres -p 8080:5432 -d postgres
