import pickle
import streamlit as st
import pandas as pd
import numpy as np
 
# loading the trained model
pickle_in = open('classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(DAYS_EMPLOYED, CODE_GENDER, CNT_CHILDREN, FLAG_OWN_CAR, AMT_INCOME_TOTAL, AMT_CREDIT):   
 
    # Pre-processing user input    
    if DAYS_EMPLOYED >= 3600:
        DAYS_EMPLOYED = True
    else:
        DAYS_EMPLOYED = False
    
    if (CODE_GENDER == "0" or CODE_GENDER == "1"):
        CODE_GENDER = True
    else:
        CODE_GENDER = False
        
    if CNT_CHILDREN <="3":
        CNT_CHILDREN = True
    else:
        CNT_CHILDREN = False
 
    if (FLAG_OWN_CAR == "1" or FLAG_OWN_CAR == "0"):
        FLAG_OWN_CAR = True
    else:
        FLAG_OWN_CAR = False
        
    if AMT_INCOME_TOTAL >= AMT_CREDIT:
        AMT_INCOME_TOTAL = True
    else:
        AMT_INCOME_TOTAL = False

    AMT_CREDIT = AMT_CREDIT
        
    # Making predictions 
    prediction = classifier.predict( 
        [[DAYS_EMPLOYED,CODE_GENDER, CNT_CHILDREN, FLAG_OWN_CAR, AMT_INCOME_TOTAL, AMT_CREDIT]])
     
    if prediction == True:
        pred = 'Diterima'
    else:
        pred = 'Ditolak'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Credit Scoring</h1> 
    </div> 
    """
     
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    DAYS_EMPLOYED = st.number_input("Berapa Hari Menjadi Pegawai?")
    CODE_GENDER = st.selectbox('Jenis Kelamin',("0 (Laki-Laki)","1 (Perempuan)"))
    CNT_CHILDREN = st.number_input("Jumlah Anak")
    FLAG_OWN_CAR = st.selectbox('Apakah Anda Memiliki Mobil?',("1 (Ya)","0 (TIDAK)")) 
    AMT_INCOME_TOTAL = st.number_input("Total Pemasukan Dalam Sebulan")
    AMT_CREDIT = st.number_input("Total Credit")
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(DAYS_EMPLOYED,CODE_GENDER, NAME_FAMILY_STATUS, FLAG_OWN_CAR, AMT_INCOME_TOTAL, AMT_CREDIT) 
        st.success('Pinjaman anda {}'.format(result))
        print(AMT_CREDIT)
     
if __name__=='__main__': 
    main()