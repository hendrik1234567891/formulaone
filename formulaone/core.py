# -*- coding: utf-8 -*-

def get_raw_data(year=2013):
    from configparser import ConfigParser
    import boto3
    from boto3.dynamodb.conditions import Key
    import pandas as pd
    import numpy as np


    #Config-Access
    file_path='../config.ini'
    config = ConfigParser()
    config.read(file_path)

    #Datenbank-Access
    session = boto3.Session(
        aws_access_key_id = config['KEYS']['aws_access_key_id'],
        aws_secret_access_key = config['KEYS']['aws_secret_access_key']
    )

    dynamo_resource = session.resource(
        'dynamodb',
        region_name='eu-west-1'
    )

    #Aus der angegebenen Tabelle als Filme aus dem Jahr 2013 rausfiltern
    movies = dynamo_resource.Table('doc-example-table-movies')
    movies=movies.query(
        KeyConditionExpression=Key('year').eq(year)
    )

    return movies


