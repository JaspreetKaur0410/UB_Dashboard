from query import *
from main import *

st.set_page_config(page_title="UB-Beauty", layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header("UB Beauty")

col_get_fav_cleanser,col_get_fav_cleanser_fig=st.columns(2)
col_get_fav_most,col_get_fav_most_fig=st.columns(2)
col_get_fav_sun,col_get_fav_sun_fig=st.columns(2)

#################################### start QUERY FAVOURITE-MOSTURISER vs age ######################################################

# query to get number of people in particular age_range with FAVOURITE-CLEANSER

with col_get_fav_cleanser:
	st.info('FAVOURITE-CLEANSER')
	query_get_fav_cleanser = query_get_fav_cleanser()
	pddata_query_getPeopleCount_fav_cleanser=pd.DataFrame(query_get_fav_cleanser)
	st.dataframe(pddata_query_getPeopleCount_fav_cleanser)

	# visualization
	group_by_fav_cleanser_age=pddata_query_getPeopleCount_fav_cleanser.groupby('age_range')
	for name, group in group_by_fav_cleanser_age:
		plt.plot(group.people_count, group.best_match,marker='o',linestyle='',markersize=12,label=name)
	plt.xlabel("people-count")
	plt.ylabel("favourite-cleanser")
	fig=plt.legend()
with col_get_fav_cleanser_fig:
	st.info('PLOT')
	st.pyplot(plt.savefig('favcleanser_by_age.png'))

#################################### end QUERY favourite cleanser vs age ##########################################################

# query to get number of people in particular age_range with FAVOURITE-MOSTURISER
with col_get_fav_most:
	st.info('FAVOURITE-MOSTURIZER')
	query_get_fav_mosturiser = query_get_fav_mosturiser()
	pddata_query_getPeopleCount_fav_mosturiser=pd.DataFrame(query_get_fav_mosturiser)
	st.dataframe(pddata_query_getPeopleCount_fav_mosturiser)

	# visualization
	group_by_fav_moturizer_age=pddata_query_getPeopleCount_fav_mosturiser.groupby('age_range')
	for name, group in group_by_fav_moturizer_age:
		plt.plot(group.people_count, group.best_match,marker='o',linestyle='',markersize=12,label=name)
	
	plt.xlabel("people-count")
	plt.ylabel("favourite-mosturizer")
	fig=plt.legend()
with col_get_fav_most_fig:
	st.info('PLOT')
	st.pyplot(plt.savefig('favmosturizer_by_age.png'))

#################################### end QUERY FAVOURITE-MOSTURISER vs age ######################################################

# query to get number of people in particular age_range with FAVOURITE-SUNSCREEN
with col_get_fav_sun:
	st.info('FAVOURITE-SUNSCREEN')
	query_get_fav_sunscreen = query_get_fav_sunscreen()

	pddata_query_getPeopleCount_fav_sunscreen=pd.DataFrame(query_get_fav_sunscreen)
	st.dataframe(pddata_query_getPeopleCount_fav_sunscreen)

	# visualization
	group_by_fav_sunscreen_age=pddata_query_getPeopleCount_fav_sunscreen.groupby('age_range')
	for name, group in group_by_fav_sunscreen_age:
		plt.plot(group.people_count, group.best_match,marker='o',linestyle='',markersize=12,label=name)
	
	plt.xlabel("people-count")
	plt.ylabel("favourite-sunscreen")
	fig=plt.legend()
with col_get_fav_sun_fig:
	st.info('PLOT')
	st.pyplot(plt.savefig('favmosturizer_by_age.png'))

#################################### end QUERY FAVOURITE-MOSTURISER vs age ######################################################