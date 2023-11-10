############################################### IMPORT PACKAGES #######################################################################

import streamlit as st
import streamlit_antd_components as sac
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from streamlit_timeline import timeline
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

############################################### SIDEBAR MENU #######################################################################


 # sidebar menu
with st.sidebar.container():
    item = sac.menu([
    sac.MenuItem('Wie ben ik', icon='person-raised-hand'),
    sac.MenuItem('Waar sta ik', icon='geo'),
    sac.MenuItem('Waar wil ik heen', icon='signpost-split'),
    ], format_func='title', open_all=True)

############################################### WIE BEN IK #######################################################################


if item == 'Wie ben ik':

 # About me section
    st.title("Wie ben ik")
    st.subheader("Laten we de feitjes op een rij zetten:")
    st.write("""
    🧑‍💻 Ik ben een  **data analist** @ [ESSENT](https://www.essent.nl/) en ik werk aan verschillende projecten zoals de BTI APP, Conversational Dashboarding, Forecasting projects for Digital / WFM, Future Energy Home.

    ❤️ Ik ben gepassioneerd over het oplossen van interessante datapuzzels en het creëren van een dataproduct dat zowel visueel aantrekkelijk is als gebruiker de tools biedt om actie te ondernemen op basis van data.
    
    🏠 Ik ben een geboren en getogen Grunninger 
             
    🏃🏼‍♀️ Sinds kort ben ik fan van **hardlopen** en **yoga**, mijn volgende doel is de 10 KM.
             
    🪡 Om te ontspannen maak ik graag mijn eigen kleding, mijn meest geliefde stuk is een trui gemaakt van Nike-sokken
    
    📫 Zo kun je mij bereiken: sophie.bode@essent.nl  """)
            
             
             
 ###*Mijn data hart gaat sneller kloppen van klant data en dan voornamelijk de kwalitatieve inzichten: hoe kunnen we de klant nou zo goed mogelijk helpen en zijn/haar gevoel het beste kwantificeren? 
 ###Hoe kunnen we sentiment of open input van klanten meenemen als voorspeller van toekomstig gedrag?*
     
  

############################################### WAAR STA IK #######################################################################

if item == 'Waar sta ik':

    btn = sac.buttons(
    items=['WordCloud', 'Portfolio'],
    index=0,
    format_func='title',
    align='center',
    direction='horizontal',
    compact=False,
    return_index=False,
        )

    if btn == 'WordCloud':

        st.title("Waar sta ik")
        st.subheader(""" Weet je wat? Ik vraag het aan mijn collega's """)
        st.markdown("""In de WordCloud hieronder zie je keywords die mijn collega's 
                hebben benoemd toen ik ze vroeg mij feedback te geven op wat ik goed doe. Als data analist kan een data visualisatie natuurlijk niet missen ;-)""")
    
        # Create some sample text
        textsample = """netwerken, kennishouder, vertrouwen, gezicht, vraagstuk, structuur, bepalen, diepe, wroeten, zoeken, 
        vragen, analyseren, visueel, technisch, skills, domeinkennis, vastbijten, contacten, gemak, vrolijk, humor, benaderbaar,
        ontwikkeling, netwerken, kennishouder, feedback"""

        # Create and generate a word cloud image:
        cloud = WordCloud(background_color = 'white', colormap = 'Greens').generate(textsample)

        # Display the generated image:
        fig = plt.figure()
        plt.imshow(cloud)
        plt.axis("off")
        st.pyplot(fig)


    if btn == 'Portfolio':
        st.subheader('Mooie dingen waar ik aan heb gewerkt')

        image = Image.open('IMAGE feh.png')

        st.image(image, caption='FEH - poster')


##st.write(f'The selected button label is: {btn}')

############################################### WAAR WIL IK HEEN #######################################################################

if item == 'Waar wil ik heen':

    btn = sac.buttons(
    items=['Ontwikkeling roadmap', 'WordCloud'],
    index=0,
    format_func='title',
    align='center',
    direction='horizontal',
    compact=False,
    return_index=False,
        )
    
    if btn == 'WordCloud':

        st.title("Waar wil ik heen")

        st.subheader("""Weet je wat? Ik vraag het aan mijn collega's """)
        st.markdown("""In de WordCloud hieronder zie je keywords die mijn collega's 
                hebben benoemd toen ik ze vroeg mij feedback te geven over wat mijn ontwikkelpunten zijn. Als data analist kan een data visualisatie natuurlijk niet missen ;-)""")
    
        # Create some sample text
        textsample1 = 'focusgebied, prioriteren, keuzes, profileren, kennisdeling, begeleiden, verspreiden, breder, leadership, '

        # Create and generate a word cloud image:
        cloud = WordCloud(background_color = 'white', colormap = 'Greens').generate(textsample1)

        # Display the generated image:
        fig = plt.figure()
        plt.imshow(cloud)
        plt.axis("off")
        st.pyplot(fig)

    if btn == 'Ontwikkeling roadmap':

        def venn_diagram():
            # Modify the set_sizes to reflect the desired sizes of the circles
            set_sizes = (2, 1.5, 1, 0.5, 0.5, 0.5, 0.5)
            venn_labels = {'100': 'Analytical skills',
                           '010': 'Networking',
                           '001': 'Visualisation/storytelling',
                           '110': '',
                           '101': '',
                           '011': '',
                           '111': ''}

            fig, ax = plt.subplots()
            venn = venn3(subsets=set_sizes, ax=ax)

            # Customize the labels in the diagram
            for idx, label in venn_labels.items():
                venn.get_label_by_id(idx).set_text(label)

            return fig

        # Create columns
        col1, col2 = st.columns([1,2])

        with col1:
            # Roadmap
            df = pd.DataFrame([
                dict(Task="Analytical skill set opbouwen", Start='2021-12-02', Finish='2023-12-30'),  
                dict(Task="Netwerk opbouwen", Start='2021-12-02', Finish='2023-12-30'),  
                dict(Task="Domein kennis opbouwen", Start='2021-12-02', Finish='2023-12-30'),  
                dict(Task="Pitch dag", Start='2023-11-13', Finish='2023-11-14'),
                dict(Task="Data storytelling", Start='2024-01-01', Finish='2024-12-01'),
                dict(Task="Begeleide rol", Start='2024-01-01', Finish='2024-12-01'),
            ])
            fig_roadmap = ff.create_gantt(df)
            st.plotly_chart(fig_roadmap)

        with col2:
            st.subheader("Roadmap")
            st.write(""" 
            """)
        
        # Create columns
        col3, col4 = st.columns([1,2])
        
        with col3:
            fig_venn = venn_diagram()
            st.pyplot(fig_venn)
        
        with col4:
            st.subheader("Focusgebieden voor ontwikkeling")
            st.write("""
                     - Focus op het samenbrengen van networking, visualization en storytelling skillset met mijn analytical skills. 
                     - Een begeleidende rol op mij nemen voor collega analisten.
            """)

        

    
     



