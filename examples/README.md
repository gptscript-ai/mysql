# MYSQL Example

Since this example requires the ability to access a mysql database with loaded data, this document serves as a guide in how to set up a given environment so that the example can be run as provided.

## Prerequisites

- [docker](https://www.docker.com/get-started/)
- `wget`
- `mysql`

## Setting Environment Variables

| variable  | example value        |
| --------- | -------------------- |
| `DB_USER` | `root`               |
| `DB_PASS` | `your_root_password` |
| `DB_HOST` | `localhost`          |
| `DB_PORT` | `3306`               |
| `DB_NAME` | `employees`          |

## Deploying a MYSQL Container in Docker Locally

To deploy a docker container containing a MYSQL container locally, run the following command:

```bash
docker run -d --name mysql_container -e MYSQL_ROOT_PASSWORD=$DB_PASS -p 3306:$DB_PORT mysql:latest
# old
docker run -d --name mysql_container -e MYSQL_ROOT_PASSWORD=your_root_password -p 3306:3306 mysql:latest
```

## Loading Data

Pull the example data and load into the mysql database with the following command:

```bash
wget https://github.com/datacharmer/test_db/archive/refs/heads/master.zip && unzip master.zip && cd test_db-master && mysql -h $DB_HOST -P $DB_PORT -u $DB_USER --password=$DB_PASS -t < employees.sql
```
