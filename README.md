# interesting_words
An NLP Project looking at presidential speeches to identify interesting words from a select group

## Preparation
Please make sure docker and docker compose are installed. Bring up the terminal in the project location.

I have set this up in an apache zeppelin. For those unfamiliar, it is very similar to jupyter but has some extra functionality/configuartions that are helpful.


Once installed, run the folling commands in your terminal:
1. To run the server:
`docker-compose up --build`
2. Check the logs to make sure the server is running. It should be visible in the terminal
3. Go to the notebook and follow along!:
`http://localhost:8087/#/notebook/2FN9C87JC`
4. Additional but not required:
After the database is created with the code in the notebook the etl portion of this project can be run with the following:
`cd ./py_code/etl.py`
