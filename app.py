import streamlit as st

from streamlit_lottie import st_lottie
import streamlit_antd_components as sac
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from streamlit_timeline import timeline
import plotly.express as px
import pandas as pd
import plotly.figure_factory as ff
from PIL import Image


 # sidebar menu
with st.sidebar.container():
    item = sac.menu([
    sac.MenuItem('Get to know me', icon='person-raised-hand'),
    sac.MenuItem('Where I am', icon='geo'),
    sac.MenuItem('Where I want to get to', icon='signpost-split'),
    ], format_func='title', open_all=True)


if item == 'Get to know me':

 # About me section
    st.title("Sophie Bode's pitch")
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a **data analist** @ [ESSENT](https://www.essent.nl/) working on multiple projects such as the BTI APP, Conversational Dashboarding, Forecasting projects for Digital / WFM

    - ❤️ I am passionate about solving interesting data puzzles, working days on end on a query and it resulting in something awesome, creating a data product that is both visually attractive as well as providing stakeholders with the tools to take action based on data
        
    - 🏃🏼‍♀️ Recently noticed that I quite like **running** and **yoga**
             
    - 🪡 To relax I like to create my own clothing, my most loved piece is a sweater made from Nike socks
    
    - 📫 How to reach me: sophie.bode@essent.nl
    
    - 🏠 I live in Groningen and travel almost 2.000 km's a month to go to work
    """)


if item == 'Where I am':

    st.subheader('What my colleagues think of me')
    st.markdown("""In the WordCloud below are keywords mentioned by colleagues when asked to provide feedback on what I am doing well at this moment ☺️""")
    
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


    st.subheader('What I made recently spiking my interest to combine data and visual storytelling')

    image = Image.open('sunrise.jpg')

    st.image(image, caption='Sunrise by the mountains')


##st.write(f'The selected button label is: {btn}')

if item == 'Where I want to get to':

    st.title('Roadmap')

    st.subheader('What my colleagues think of me')
    st.markdown("""In the WordCloud below are keywords mentioned by colleagues when asked to provide feedback on my development""")
    
    # Create some sample text
    textsample1 = 'focusgebied, prioriteren, keuzes, profileren, kennisdeling, begeleiden, verspreiden, breder, leadership, '

# Create and generate a word cloud image:
    cloud = WordCloud(background_color = 'white', colormap = 'Greens').generate(textsample1)

# Display the generated image:
    fig = plt.figure()
    plt.imshow(cloud)
    plt.axis("off")
    st.pyplot(fig)


    st.subheader("Focusgebieden")
    st.write("""
             
             - Visuele aspect van data combineren met de beta kant van data
             - Machine learning skills opkrikken
             - Meer ruimte nemen voor eigen ontwikkeling'
             - Kennisdeling binnen het team

             """)



    st.subheader("Timeline of development")


    df = pd.DataFrame([
    dict(Task="Pitch day", Start='2023-11-13', Finish='2023-11-14'),
    dict(Task="Exchange knowledge with UI/UX team", Start='2024-02-01', Finish='2024-04-01'),
    dict(Task="Start learning more about mentoring / guiding junior data analists", Start='2024-04-01', Finish='2024-05-01'),
    dict(Task="Storytelling course", Start='2024-06-01', Finish='2024-07-01'),
    dict(Task="Mentor program", Start='2024-02-01', Finish='2024-07-01')
    ])

    fig = ff.create_gantt(df)
    st.plotly_chart(fig)

    ##fig = px.timeline(df, x_start='Start', x_end='Finish', y='Task')
   ## fig.update_yaxes(autorange="reversed") 
   ## st.plotly_chart(fig)
     

##btn = sac.buttons(
##items=['Sophie', 'Verbinding', 'Blabla'],
##index=0,
##format_func='title',
##align='center',
##direction='horizontal',
##shape='round',
##compact=False,
##return_index=False,
##    )
