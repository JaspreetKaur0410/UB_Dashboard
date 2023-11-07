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
