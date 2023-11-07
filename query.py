import streamlit as st
from all_queries import *
import pymysql
import sys
import boto3
import os
import pymysql.cursors

ENDPOINT=st.secrets["ENDPOINT"]
PORT=st.secrets["PORT"]
USER=st.secrets["USER"]
REGION=st.secrets["REGION"]
DBNAME=st.secrets["DBNAME"]
PASSWORD=st.secrets["PASSWORD"]
aws_access_key_id=st.secrets["aws_access_key_id"]
aws_secret_access_key=st.secrets["aws_secret_access_key"]

class DB:
    def __init__(self):
        self.conn = pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME,cursorclass=pymysql.cursors.DictCursor)

    def query(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row.values())) for row in cursor.fetchall()]
            return query_results
        except pymysql.OperationalError:
            # if the connection was lost, then it reconnects
            self.conn.ping(reconnect=True) 
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row.values())) for row in cursor.fetchall()]
            return query_results
        finally:
            # if the connection was lost, then it reconnects
            self.conn.ping(reconnect=True) 
            cursor = self.conn.cursor()
            cursor.execute(sql)
            desc = cursor.description
            column_names = [col[0] for col in desc]
            query_results = [dict(zip(column_names, row.values())) for row in cursor.fetchall()]
            return query_results


db = DB()


def view_all_data():
    query_results=db.query('''select age,location,gender,reason,source_type,skin_type,product_type,product_name,best_match from master_recomm order by id asc''')
    return query_results
    
def people_count_skin_type_age_groups():
    query_results=db.query(query_get_skintype_age)
    return query_results
    
# FAVOURITES  
def query_get_fav_cleanser():
    query_results=db.query(query_fav_cleanser)
    return query_results
     
def query_get_fav_mosturiser():
    query_results=db.query(query_fav_mosturiser)
    return query_results
    
def query_get_fav_sunscreen():
    query_results=db.query(query_fav_sunscreen)
    return query_results

def get_top5_cleanser_count_dry_skin():
    query_results=db.query(query_get_top5_cleanser_count_dry_skin)
    return query_results

def get_top5_cleanser_count_oily_skin():
    query_results=db.query(query_get_top5_cleanser_count_oily_skin)
    return query_results
     
def get_top5_cleanser_count_Combination_skin():
    query_results=db.query(query_get_top5_cleanser_count_Combination_skin)
    return query_results