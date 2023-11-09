import streamlit as st

import streamlit_antd_components as sac
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from streamlit_timeline import timeline
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
from PIL import Image
##import streamlit_wordcloud as wc

 # sidebar menu
with st.sidebar.container():
    item = sac.menu([
    sac.MenuItem('Wie ben ik', icon='person-raised-hand'),
    sac.MenuItem('Waar sta ik', icon='geo'),
    sac.MenuItem('Waar wil ik heen', icon='signpost-split'),
    ], format_func='title', open_all=True)


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
    
    📫 Zo kun je mij bereiken: sophie.bode@essent.nl
             
      
             





 -------------------------------------------------------------------------------------------------------------------------------------

             
 *Mijn data hart gaat sneller kloppen van klant data en dan voornamelijk de kwalitatieve inzichten: hoe kunnen we de klant nou zo goed mogelijk helpen en zijn/haar gevoel het beste kwantificeren? 
 Hoe kunnen we sentiment of open input van klanten meenemen als voorspeller van toekomstig gedrag?*
     
    """)


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

if item == 'Waar wil ik heen':

    btn = sac.buttons(
    items=['WordCloud', 'Focusgebied', 'Roadmap'],
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

    if btn == 'Focusgebied':

        st.subheader("Focusgebieden")
        st.write("""
                
                - Storytelling en visuele tooling om data inzichten nog meer kracht bij te zetten
                - Machine learning skills 
                - Meer ruimte nemen voor eigen ontwikkeling 
                - Kennisdeling en begeleidende rol binnen het team

                """)


    if btn == 'Roadmap':
        st.subheader("Roadmap")


        df = pd.DataFrame([
        dict(Task="Pitch dag", Start='2023-11-13', Finish='2023-11-14'),
        dict(Task="Kennis ophalen / meelopen met UI/UX team", Start='2024-02-01', Finish='2024-04-01'),
        dict(Task="Begeleiding bieden aan collega (startende) analisten", Start='2024-01-01', Finish='2024-12-01'),
        dict(Task="Storytelling cursus", Start='2024-06-01', Finish='2024-07-01'),
        dict(Task="Mentor programma volgen", Start='2024-02-01', Finish='2024-07-01')
        ])

        fig = ff.create_gantt(df)
        st.plotly_chart(fig)

    ##fig = px.timeline(df, x_start='Start', x_end='Finish', y='Task')
   ## fig.update_yaxes(autorange="reversed") 
   ## st.plotly_chart(fig)
     


