import pickle
import streamlit as st
from PIL import Image
def predict_note_authentication(fam_size, busexp, number, time, otherdebt, timeofcredit, income, gen_code, fam_code, edu_code, cus_code, bus_code, age, zalog_code):
    pickle_in = open("Arvand.pkl","rb")
    randf_model = pickle.load(pickle_in)
    prediction=randf_model.predict([[fam_size, busexp, number, time, timeofcredit, income, gen_code, fam_code, edu_code, filial_code, cus_code, bus_code, nat_code, age, zalog_code]])
    return prediction

def main():
    age = st.number_input("Ваш возраст:", min_value=18, max_value=100)
    gender = st.selectbox("Ваш пол:", ["Мужской", "Женский"])
    number = st.number_input("Какую сумму вы хотите взять:", min_value=0, max_value=100000000)
    income = st.number_input("Какой у вас ежемесячный доход:", min_value=0, max_value=100000000)
    timeofcredit = st.number_input("Который раз вы получаете кредит:", min_value=0, max_value=100000000)
    busexp = st.number_input("Какой у вас стаж работы:", min_value=0, max_value=100000000)
    otherdebt = st.number_input("Есть ли у вас другие кредиты(Введите сумму):", min_value=0, max_value=100000000)
    currency = st.selectbox("В какой валюте хотите получить кредит:", ["Сомони", "Доллар", "Рубль"])
    time = st.number_input("На какой период хотите взять кредит:", min_value=0, max_value=100000000)
    family = st.selectbox("Какое у вас семейное положение:", ["Оиладор", "Ҷудошуда", 'Беоила' , 'Бевазан(бевамард)'])
    zalog = st.selectbox("Какой у вас залог:", ["Поручительство", "Недвижимость", 'Движимое имущество' , 'Без залога'])
    customer = st.selectbox("Type of client:", ["Бовари (до 1 годa)", "Хамкори (от 1 до 3 лет)", "Шарик (от 3 до 5 лет)", "VIPболее (5 лет)"])
    education = st.selectbox("Education level:", ['Миёна', 'Оли', 'Миёнаи махсус', 'Олии нопурра', 'Миёнаи нопурра'])
    fam_size = st.number_input("Сколько людей в вашей семье:", min_value=1, max_value=50)
    tp_bus = st.selectbox("Type of credit:", ["Потребительский кредит", "Кредит на предпринимательскую деятельность",  "Энергосберегающие технологии", "Жилищный кредит"])
    

    gen_code = 0 
    if(gender == "Мужской"):
        gen_code = 1 
    else:
        gen_code = 0
    
    
    if(currency == 'Доллар'):
        number = number * 11 
    elif(currency == 'Рубль'):
        number = number * 0.12
        
    
    zalog_code = 0 
    if(zalog == "Поручительство"):
        zalog_code = 2
    elif(zalog == 'Недвижимость'):
        zalog_code = 4
    elif(zalog == 'Движимое имущество'):
        zalog_code = 3
    elif(zalog == 'Без залога'):
        zalog_code = 1
    
       
    bus_code = 0 
    if(tp_bus == "Потребительский кредит"):
        bus_code = 1 
    elif(tp_bus == 'Кредит на предпринимательскую деятельность'):
        bus_code = 2
    elif(tp_bus == 'Энергосберегающие технологии'):
        bus_code = 3
    elif(tp_bus == 'Жилищный кредит'):
        bus_code = 4
        
        
    edu_code = 0 
    if(education == "Миёна"):
        edu_code = 1 
    elif(education == 'Оли'):
        edu_code = 5
    elif(education == 'Миёнаи махсус'):
        edu_code = 2
    elif(education == 'Олии нопурра'):
        edu_code = 4
    elif(education == 'Миёнаи нопурра'):
        edu_code = 3
        
        
    cus_code = 0 
    if(customer == "Бовари (до 1 годa)"):
        cus_code = 4
    elif(customer == 'Хамкори (от 1 до 3 лет)'):
        cus_code = 1
    elif(customer == 'Шарик (от 3 до 5 лет)'):
        cus_code = 2
    else:
        cus_code = 3
        
        
    fam_code = 0 
    if(family == "Оиладор"):
        fam_code = 1 
    elif(family == 'Беоила'):
        fam_code = 2
    elif(family == 'Бевазан(бевамард)'):
        fam_code = 3
    else:
        fam_code = 4
    
  
    
    
        
    # Выводим данные на экран
    st.write("Your age :", age)
    st.write("Your gender:", gen_code)
    st.write("Your family situation:", fam_code)
    st.write("Your type of business:", bus_code)
    st.write("Your education:", edu_code)
    st.write("Which type of client are you :", cus_code)
    st.write("Sum of debt:", number)
    

    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(fam_size, busexp, number, time, otherdebt, timeofcredit, income, gen_code, fam_code, edu_code, cus_code, bus_code, age, zalog_code))

    if(result == 1):
        st.success('You are accepted')
    else:
        st.success('You are not accepted')
# Запускаем приложение
if __name__ == "__main__":
    main()
    