
FROM python:3.9.13-slim-buster

# working directory
WORKDIR /home

# entrypoint must be bash to run python hubconf.py
ENTRYPOINT [ "bash" ]