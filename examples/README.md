# MYSQL Example

Since this example requires the ability to access a mysql database with loaded data, this document serves as a guide in how to set up a given environment so that the example can be run as provided.

## Prerequisites

- [docker](https://www.docker.com/get-started/)
- `wget`
- `mysql`

## Setting Environment Variables

These are the same variables that would need to be set when invoking the tool, so whatever they are set to in the process of setting up the example database is what should be passed into the tool calls.

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
```

## Loading Data

We will utilize an [example database](https://github.com/datacharmer/test_db). Pull the example data and load into the mysql database with the following command:

```bash
wget https://github.com/datacharmer/test_db/archive/refs/heads/master.zip && unzip master.zip && cd test_db-master && mysql -h $DB_HOST -P $DB_PORT -u $DB_USER --password=$DB_PASS -t < employees.sql
```

## Results From Tool Runs

| prompt                                                                                        | response                                                                                                                                                                                                              |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| which two unique employees have the highest salary, and what are their names?                 | The two unique employees with the highest salary are Tokuyasu Pesch with a salary of $158,220 and Tokuyasu Pesch with a salary of $157,821.                                                                           |
| which two employees with different names have the highest salaries, and what are their names? | I am unable to provide a result based on the given instructions.                                                                                                                                                      |
| which employee has the lowest salary?                                                         | There was an error in processing your request due to a missing GROUP BY clause in the SQL query. Please ensure the query includes the appropriate syntax for the desired result.                                      |
| which two employees have the highest current salaries                                         | The two employees with the highest current salaries are Tokuyasu Pesch with a salary of $158,220 and Honesty Mukaidono with a salary of $156,286.                                                                     |
| what are the department average salaries                                                      | The department with the highest average salary is Sales at $80,667.61, followed by Marketing at $71,913.20 and Finance at $70,489.36. The department with the lowest average salary is Human Resources at $55,574.88. |
| how many employees does each of the departments have                                          | (The response provided departments as the department ids)                                                                                                                                                             |
