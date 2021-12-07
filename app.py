from flask import Flask,render_template,request
import pickle
import jsonify
import requests
import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor



app=Flask(__name__)
model = pickle.load(open('C:\\Users\\Dinesh ram\\Downloads\\models\\gem\\model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':     
        print('k')                                               # color  E', 'G', 'F', 'D', 'H', 'J', 'I
        caret_type = float(request.form['caret_type'])
        print(caret_type)
        depth_type=request.form['depth_type']
        print(depth_type)
        table_type=request.form['table_type']
        print(table_type)
        color=request.form['color_type']
        print(color)
        if color=='E':                                    
            E=1
            F=0
            G=0                                           # clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=0
            H=0
            J=0
            I=0
        elif color=='G':
            E=0
            F=0
            G=1                                           #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=0
            H=0
            J=0
            I=0
        elif color=='F':
            E=0
            F=1
            G=0                                         
            D=0
            H=0
            J=0
            I=0
        elif color=='D':
            E=0
            F=0
            G=0                                           #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=1
            H=0
            J=0
            I=0
        elif color=='H':
            E=0
            F=0
            G=0                                           #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=0
            H=1
            J=0
            I=0
        elif color=='J':
            E=0
            F=0
            G=0                                           #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=0
            H=0
            J=1
            I=0
        elif color=='I':
            E=0
            F=0
            G=0                                           #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=0
            H=0
            J=0
            I=1
        else:
            E=0
            F=0
            G=0                                           #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
            D=0
            H=0
            J=0
            I=0
        E=E
        F=F
        G=G                                        #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2', 'SI2', 'I1' 
        D=D
        H=H
        J=J
        I=I
        
        cut_type=request.form['cut_type']  
        print(cut_type)                              #cu'Fair': 1, 'Good': 2,'Very Good': 3,'Premium':4,'Ideal': 5
        if(cut_type=='Ideal'):
           cut_type=5
        elif(cut_type=='Premium'):
            cut_type=4
        elif(cut_type=='Very Good'):
            cut_type=3
        elif(cut_type=='Good'):
            cut_type=2
        elif(cut_type=='Fair'):
            cut_type=1             #clarity  'SI1', 'IF', 'VVS2', 'VS1', 'VVS1', 'VS2' 'SI2', 'I1'
        else:
            print("cut_type Not selected")
        print(cut_type)
        clarity_type=request.form['clarity_type']
        print(clarity_type)
        if(clarity_type=='SI1'):
            SI1=1
            IF=0
            VVS2=0
            VS1=0
            VVS1=0
            VS2=0
            SI2=0
            I1=0
        elif(clarity_type=='IF'):
            SI1=0
            IF=1
            VVS2=0
            VS1=0
            VVS1=0
            VS2=0
            SI2=0
            I1=0  
        elif(clarity_type=='VVS2'):
            SI1=0
            IF=0
            VVS2=1
            VS1=0
            VVS1=0
            VS2=0
            SI2=0
            I1=0
        elif(clarity_type=='VS1'):
            SI1=0
            IF=0
            VVS2=0
            VS1=1
            VVS1=0
            VS2=0
            SI2=0
            I1=0
        elif(clarity_type=='VVS1'):
            SI1=0
            IF=0
            VVS2=0
            VS1=0
            VVS1=1
            VS2=0
            SI2=0
            I1=0
        elif(clarity_type=='VS2'):
            SI1=0
            IF=0
            VVS2=0
            VS1=0
            VVS1=0
            VS2=1
            SI2=0
            I1=0
        elif(clarity_type=='SI2'):
            SI1=0
            IF=0
            VVS2=0
            VS1=0
            VVS1=0
            VS2=0
            SI2=1
            I1=0
        elif(clarity_type=='I1'):
            SI1=0
            IF=0
            VVS2=0
            VS1=0
            VVS1=0
            VS2=0
            SI2=0
            I1=1
        else:
            print("error")
        SI1=SI1
        IF=IF
        VVS2=VVS2
        VS1=VS1
        VVS1=VVS1
        VS2=VS2
        SI2=SI2
        I1=I1
        
        print(H)
            
        input=[caret_type,cut_type,depth_type,table_type,E,F,G,H,I,J,IF,SI1,SI2,VS1,VS2,VVS1,VVS2]
        print(input)
        prediction=model.predict([input])
        print(prediction[0])
        output=prediction
        if output<0:
            return render_template('index.html',prediction_text="Sorry something went wrong")
        else:
            return render_template('index.html',prediction_text="predicted gem price :"+str(output))
    else:
        return render_template('index.html')
        
        
    
if __name__=="__main__":
    app.run(debug=False)       
            
        
        
            