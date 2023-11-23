import streamlit as st
import pymysql
import sys
import boto3
import os


ENDPOINT=st.secrets["ENDPOINT"]
PORT=st.secrets["PORT"]
USER=st.secrets["USER"]
REGION=st.secrets["REGION"]
DBNAME=st.secrets["DBNAME"]
PASSWORD=st.secrets["PASSWORD"]
aws_access_key_id=st.secrets["aws_access_key_id"]
aws_secret_access_key=st.secrets["aws_secret_access_key"]


#gets the credentials from .aws/credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=REGION
)


# client = session.client('rds')
# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT,passwd=PASSWORD, DBUsername=USER, Region=REGION)
# print("*************"+token)

conn =  pymysql.connect(host=ENDPOINT, user=USER, passwd=PASSWORD, port=PORT, database=DBNAME)  



query_get_skintype_age = ('''select age_range,
	MAX(CASE WHEN skin_type = 'Dry' THEN people_count_by_skin_type ELSE NULL END) AS 'Dry',
	MAX(CASE WHEN skin_type = 'Oily' THEN people_count_by_skin_type ELSE NULL END) AS 'Oily',
	MAX(CASE WHEN skin_type = 'Sensitive' THEN people_count_by_skin_type ELSE NULL END) AS 'Sensitive',
	MAX(CASE WHEN skin_type = 'Combination' THEN people_count_by_skin_type ELSE NULL END) AS 'Combination'
from(
	select ur.age_range,ur.skin_type,count(skin_type) as 'people_count_by_skin_type'
	from
		(select age, skin_type,
		case when age>=12 and age<=18 then '12-18'
		when age>=19 and age<=25 then '19-25'
		when age>=26 and age<=34 then '26-34'
		when age>=35 and age<=45 then '35-45'
		when age>=46 and age<55 then '46-55'
		else '55+' end as 'age_range'
		from master_recomm) ur
		group by ur.age_range,skin_type
	) temp
group by temp.age_range
order by temp.age_range''')

query_fav_cleanser='''with temp_table as
(
	select ur.age_range, ur.best_match, count(best_match) as 'people_count' 
				from
					(select age,product_type,best_match,
						case when age>=12 and age<=18 then '12-18'
						when age>=19 and age<=25 then '19-25'
						when age>=26 and age<=34 then '26-34'
						when age>=35 and age<=45 then '35-45'
						when age>=46 and age<55 then '46-55'
						else '55+' end as 'age_range'
					from master_recomm where product_type='cleanser'
					) ur
	group by ur.age_range,ur.best_match
)
select * from temp_table where (temp_table.age_range,temp_table.people_count) 
IN (select age_range, max(people_count) 
from temp_table
group by age_range
)'''

query_fav_mosturiser='''with temp_table as
(
	select ur.age_range, ur.best_match, count(best_match) as 'people_count' 
				from
					(select age,product_type,best_match,
						case when age>=12 and age<=18 then '12-18'
						when age>=19 and age<=25 then '19-25'
						when age>=26 and age<=34 then '26-34'
						when age>=35 and age<=45 then '35-45'
						when age>=46 and age<55 then '46-55'
						else '55+' end as 'age_range'
					from master_recomm where product_type='moisturiser'
					) ur
	group by ur.age_range,ur.best_match
)
select * from temp_table where (temp_table.age_range,temp_table.people_count) 
IN (select age_range, max(people_count) 
from temp_table
group by age_range
)'''

query_fav_sunscreen = '''with temp_table as
(
	select ur.age_range, ur.best_match, count(best_match) as 'people_count' 
				from
					(select age,product_type,best_match,
						case when age>=12 and age<=18 then '12-18'
						when age>=19 and age<=25 then '19-25'
						when age>=26 and age<=34 then '26-34'
						when age>=35 and age<=45 then '35-45'
						when age>=46 and age<55 then '46-55'
						else '55+' end as 'age_range'
					from master_recomm where product_type='sunscreen'
					) ur
	group by ur.age_range,ur.best_match
)
select * from temp_table where (age_range,people_count) 
IN (select age_range, max(people_count) 
from temp_table
group by age_range
)'''

query_get_top5_cleanser_count_dry_skin='''select best_match, count(best_match) as count_people_cleanser_dry_skin
from master_recomm
where best_match <>''and product_type='cleanser' and skin_type='dry'
group by best_match
order by count_people_cleanser_dry_skin DESC limit 5'''

query_get_top5_cleanser_count_oily_skin = '''select best_match, count(best_match) as count_people_cleanser_oily_skin
from master_recomm
where best_match <>''and product_type='cleanser' and skin_type='Oily'
group by best_match
order by count_people_cleanser_oily_skin DESC limit 5'''

query_get_top5_cleanser_count_Combination_skin = '''select best_match, count(best_match) as count_people_cleanser_comb_skin
from master_recomm
where best_match <>''and product_type='cleanser' and skin_type='Combination'
group by best_match
order by count_people_cleanser_comb_skin DESC limit 5'''


def view_all_data():
    try:
        with conn.cursor() as cur:
            cur.execute("""select age,location,gender,reason,source_type,skin_type,product_type,product_name,best_match from master_recomm order by id asc""")
            query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            cur.close()
            return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")
    
def people_count_skin_type_age_groups():
    try:
        with conn.cursor() as cur:
            cur.execute(query_get_skintype_age)
            query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            cur.close()
            return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")
    
# FAVOURITES  
def query_get_fav_cleanser():
    try: 
         with conn.cursor() as cur:
             cur.execute(query_fav_cleanser)
             query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
             cur.close()
             return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")
     
def query_get_fav_mosturiser():
    try:
        with conn.cursor() as cur:
            cur.execute(query_fav_mosturiser)
            query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            cur.close()
            return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")
    
def query_get_fav_sunscreen():
    try: 
         with conn.cursor() as cur:
             cur.execute(query_fav_sunscreen)
             query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
             cur.close()
             return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")

def get_top5_cleanser_count_dry_skin():
    try: 
         with conn.cursor() as cur:
             cur.execute(query_get_top5_cleanser_count_dry_skin)
             query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
             cur.close()
             return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")

def get_top5_cleanser_count_oily_skin():
    try: 
         with conn.cursor() as cur:
             cur.execute(query_get_top5_cleanser_count_oily_skin)
             query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
             cur.close()
             return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")
     
def get_top5_cleanser_count_Combination_skin():
    try: 
         with conn.cursor() as cur:
             cur.execute(query_get_top5_cleanser_count_Combination_skin)
             query_results = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
             cur.close()
             return query_results
    except Exception as e:
        print(f"Error while connecting to MySQL using Connection pool : {e}")
         

        
    


    