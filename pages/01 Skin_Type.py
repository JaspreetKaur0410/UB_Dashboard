from query import *
from main import *

# st.set_page_config(page_title="UB-Beauty", layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header("UB Beauty")


#################################### start QUERY skintype vs age ######################################################

query_get_skintype_age=people_count_skin_type_age_groups();
# get data into dataframe
pddata_query_get_skintype_age=pd.DataFrame(query_get_skintype_age)
#visulaize age_range & skin_type together
st.subheader('number of people in different age groups based on skin_type')
pddata_melt_form=pddata_query_get_skintype_age;
#transform dataframe 
melted_data=pd.melt(pddata_melt_form, id_vars=['age_range'])
chart_melted_data=alt.Chart(melted_data).mark_bar(strokeWidth=100).encode(
    #paddingOuter - you can play with a space between 2 models 
    x=alt.X('variable:N', title="", scale=alt.Scale(paddingOuter=0.5)),
    y='value:Q',
    color='variable:N',
    #spacing =0 removes space between columns, column for can and st 
    column=alt.Column('age_range:N', title="", spacing =0), 
).properties( width = 140, height = 150, ).configure_header(labelOrient='bottom').configure_view(
    strokeOpacity=0)
st.altair_chart(chart_melted_data)

col_dry,col_oily=st.columns(2)
col_sen,col_comb=st.columns(2)

# Making the Bar chart dry skin
with col_dry:
    st.info('number of people in different age groups - DRY SKIN')
    chart_age_vs_skintype_dry=alt.Chart(pddata_query_get_skintype_age).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='age_range', 
        # Mapping the Score column to y-axis 
        y='Dry'
    )
    st.altair_chart(chart_age_vs_skintype_dry, use_container_width=True)

# Making the Bar chart oily skin
with col_oily:
    st.info('number of people in different age groups - OILY SKIN')
    chart_age_vs_skintype_oily=alt.Chart(pddata_query_get_skintype_age).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='age_range', 
        # Mapping the Score column to y-axis 
        y='Oily'
    )
    st.altair_chart(chart_age_vs_skintype_oily, use_container_width=True)

# Making the Bar chart sensitive skin
with col_sen:
    st.info('number of people in different age groups - SENSITIVE SKIN')
    chart_age_vs_skintype_sensitive=alt.Chart(pddata_query_get_skintype_age).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='age_range', 
        # Mapping the Score column to y-axis 
        y='Sensitive'
    )
    st.altair_chart(chart_age_vs_skintype_sensitive, use_container_width=True)

# Making the Bar chart combination skin
with col_comb:
    st.info('number of people in different age groups - COMBINATION SKIN')
    chart_age_vs_skintype_comb=alt.Chart(pddata_query_get_skintype_age).mark_bar().encode( 
        # Mapping the Website column to x-axis 
        x='age_range', 
        # Mapping the Score column to y-axis 
        y='Combination'
    )
    st.altair_chart(chart_age_vs_skintype_comb, use_container_width=True)

 #################################### END QUERY skintype vs age ##################################################################