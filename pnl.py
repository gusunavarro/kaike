import streamlit as st
from summarizer import summarize

col1, col2 = st.columns([2,1])
datos = col2.file_uploader(" Carga aquí tu archivo de datos.csv ")


#Headings for Web Application
st.title("procesamiento del lenguaje natural")
st.subheader("Que servicio del lenguaje natural desea utilizar?")
#Picking what NLP task you want to do
option = st.selectbox('NLP Servicio',('Análisis de Sentimiento', 'Extracción de entidad', 'Resumen texto')) #option is stored in this variable
#Textbox for text user is entering
st.subheader("Entre el texto que le gustaría analizar")
text = st.text_input('Entrar texto') #text is stored in this variable
#Display results of the NLP task
st.header("Resultado")

import nltk

from nltk.tokenize import word_tokenize, sent_tokenize


from textblob import TextBlob
import nltk

if option != 'Análisis de Sentimiento':

    summWords = summarize(text)
    st.subheader("Summary")
    st.write(summWords)
#Sentiment Analysis
else:
    #Creating graph for sentiment across each sentence in the text inputted
    sents = sent_tokenize(text) #tokenizing the text data into a list of sentences
    entireText = TextBlob(text) #storing the entire text in one string
    sentScores = [] #storing sentences in a list to plot
    for sent in sents:
        text = TextBlob(sent) #sentiment for each sentence
        score = text.sentiment[0] #extracting polarity of each sentence
        sentScores.append(score)

    #Plotting sentiment scores per sentencein line graph
    st.line_chart(sentScores) #using line_chart st call to plot polarity for each sentence

    # Polarity and Subjectivity of the entire text inputted
    sentimentTotal = entireText.sentiment
    st.write("El sentimiento del texto general a continuación.")
    st.write(sentimentTotal)

 