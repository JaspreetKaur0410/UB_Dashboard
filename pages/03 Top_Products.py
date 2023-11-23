from query import *
from main import *

# st.set_page_config(page_title="UB-Beauty", layout='wide')

col_get_top_cleanser_dry_skin,col_get_top_cleanser_dry_skin_fig=st.columns(2)
col_get_top_cleanser_oily_skin,col_get_top_cleanser_oily_skin_fig=st.columns(2)
col_get_top_cleanser_comb_skin,col_get_top_cleanser_comb_skin_fig=st.columns(2)

#################################### start QUERY count_cleansers_dry_skin ######################################################

# query to get number of people for particular cleanser for dry skin
with col_get_top_cleanser_dry_skin:
    st.info('TOP 5 - CLEANSERS COUNT DRY SKIN')
    query_get_cleanser_count_dry_skin = get_top5_cleanser_count_dry_skin()
    pddata_query_cleanser_count_dry_skin=pd.DataFrame(query_get_cleanser_count_dry_skin)
    st.dataframe(pddata_query_cleanser_count_dry_skin)

with col_get_top_cleanser_dry_skin_fig:
    # visualization
    chart_query_cleanser_count_dry_skin=alt.Chart(pddata_query_cleanser_count_dry_skin).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='best_match', 
        # Mapping the Score column to y-axis 
        y='count_people_cleanser_dry_skin'
    ).properties( width = 200, height = 500)
    st.altair_chart(chart_query_cleanser_count_dry_skin, use_container_width=True)

#################################### end  QUERY count_cleansers_oily_skin ######################################################

# query to get number of people for particular cleanser for dry skin
with col_get_top_cleanser_oily_skin:
    st.info('TOP 5 - CLEANSERS COUNT OILY SKIN')
    query_get_cleanser_count_oily_skin = get_top5_cleanser_count_oily_skin()
    pddata_query_cleanser_count_oily_skin=pd.DataFrame(query_get_cleanser_count_oily_skin)
    st.dataframe(pddata_query_cleanser_count_oily_skin)
    
with col_get_top_cleanser_oily_skin_fig:
    # visualization
    chart_query_cleanser_count_oily_skin=alt.Chart(pddata_query_cleanser_count_oily_skin).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='best_match', 
        # Mapping the Score column to y-axis 
        y='count_people_cleanser_oily_skin'
    ).properties( width = 300, height = 500)
    st.altair_chart(chart_query_cleanser_count_oily_skin, use_container_width=True)

#################################### end  QUERY count_cleansers_oily_skin ######################################################

# query to get number of people for particular cleanser for Combination skin
with col_get_top_cleanser_comb_skin:
    st.info('TOP 5 - CLEANSERS COUNT Combination SKIN')
    query_get_cleanser_count_Combination_skin =get_top5_cleanser_count_Combination_skin()
    pddata_query_cleanser_count_comb_skin=pd.DataFrame(query_get_cleanser_count_Combination_skin)
    st.dataframe(pddata_query_cleanser_count_comb_skin)

with col_get_top_cleanser_comb_skin_fig:
    # visualization
    chart_query_cleanser_count_comb_skin=alt.Chart(pddata_query_cleanser_count_comb_skin).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='best_match', 
        # Mapping the Score column to y-axis 
        y='count_people_cleanser_comb_skin'
    ).properties( width = 300, height = 500)
    st.altair_chart(chart_query_cleanser_count_comb_skin, use_container_width=True)

#################################### end  QUERY count_cleansers_oily_skin ######################################################