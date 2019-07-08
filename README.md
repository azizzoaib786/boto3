Lightweight script to manage EC2 instances in AWS

## About

This project used boto3 to manage instances in AWS

## Configuring

It uses the configuration file created by aws cli

aws configure --profile awsbot

## Running

pipenv run python awsboto3.py list
pipenv run python awsboto3.py start
pipenv run python awsboto3.py stop