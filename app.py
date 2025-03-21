from tkinter import *
from tkinter import  messagebox

from mydb import Database
from myapi import API


class NLPApp:

    def __init__(self):
        self.dbo=Database()
        self.apio=API()

        self.root=Tk()
        self.root.title("NLPApp")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry("400x600")
        self.root.configure(bg="#efa898")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear()
        headline=Label(self.root,text="NLPApp",foreground="white",bg="#efa898")
        headline.pack(pady=(30,30))
        headline.configure(font=("verdana",30,"bold"))

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))

        self.email_input=Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10, 10))

        self.password = Entry(self.root, width=50,show="*")
        self.password.pack(pady=(5, 10), ipady=4)


        login_btn=Button(self.root,text="Login",width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="Not a Member?")
        label3.pack(pady=(10, 10))

        register_btn = Button(self.root, text="Register Now", width=30, height=2,command=self.register_gui)
        register_btn.pack(pady=(10, 10))


    def register_gui(self):
        self.clear()

        headline = Label(self.root, text="NLPApp", foreground="white", bg="#efa898")
        headline.pack(pady=(30, 30))
        headline.configure(font=("verdana", 30, "bold"))

        label0 = Label(self.root, text="Enter name")
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=(10, 10))

        self.password = Entry(self.root, width=50, show="*")
        self.password.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", width=30, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

    def perform_registration(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password.get()
        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('Success', 'Registration successful. You can login now')
            self.login_gui()
        else:
            messagebox.showerror('Error', 'Email already exists')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password.get()
        response = self.dbo.search(email, password)

        if response:
            messagebox.showinfo("Sucess","Login Sucessful")
            self.home_gui()
        else:
            messagebox.showinfo("Error","Incorrect Email/Password")




    def home_gui(self):

        self.clear()

        headline = Label(self.root, text="NLPApp", foreground="white", bg="#efa898")
        headline.pack(pady=(30, 30))
        headline.configure(font=("verdana", 30, "bold"))


        Sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=5,command=self.sentiment_gui)
        Sentiment_btn.pack(pady=(20, 10))

        ner_btn = Button(self.root, text="Name Entity Recognition", width=30, height=5,command=self.ner_gui)
        ner_btn.pack(pady=(20, 10))

        emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=5,command=self.emotion_gui)
        emotion_btn.pack(pady=(20, 10))

    def sentiment_gui(self) :
        self.clear()

        headline = Label(self.root, text="NLPApp", foreground="white", bg="#efa898")
        headline.pack(pady=(30, 30))
        headline.configure(font=("verdana", 30, "bold"))

        headline1 = Label(self.root, text="Sentiment Analysis", foreground="white", bg="#efa898")
        headline1.pack(pady=(15, 15))
        headline1.configure(font=("verdana", 16))

        label0 = Label(self.root, text="Enter text")
        label0.pack(pady=(10, 10))

        self.text = Entry(self.root, width=50)
        self.text.pack(pady=(5, 10), ipady=4)

        analysis = Button(self.root, text="Analyze", width=30, height=5, command=self.do_sentiment)
        analysis.pack(pady=(20, 10))

        self.sentiment_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def ner_gui(self) :
        self.clear()

        headline = Label(self.root, text="NLPApp", foreground="white", bg="#efa898")
        headline.pack(pady=(30, 30))
        headline.configure(font=("verdana", 30, "bold"))

        headline1 = Label(self.root, text="Name Entity Recognition", foreground="white", bg="#efa898")
        headline1.pack(pady=(10, 10))
        headline1.configure(font=("verdana", 16))

        label0 = Label(self.root, text="Enter text")
        label0.pack(pady=(5, 5))

        self.text = Entry(self.root, width=50)
        self.text.pack(pady=(5, 10), ipady=4)

        label0 = Label(self.root, text="Enter Entity")
        label0.pack(pady=(5, 5))

        self.entity = Entry(self.root, width=50)
        self.entity.pack(pady=(5, 10), ipady=4)

        analysis = Button(self.root, text="Analyze", width=30, height=5, command=self.do_ner)
        analysis.pack(pady=(20, 10))

        self.ner_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.ner_result.pack(pady=(16, 12))
        self.ner_result.configure(font=('verdana', 8))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))


    def emotion_gui(self) :
        self.clear()

        headline = Label(self.root, text="NLPApp", foreground="white", bg="#efa898")
        headline.pack(pady=(30, 30))
        headline.configure(font=("verdana", 30, "bold"))

        headline1 = Label(self.root, text="Emotion Prediction", foreground="white", bg="#efa898")
        headline1.pack(pady=(10, 10))
        headline1.configure(font=("verdana", 16))

        label0 = Label(self.root, text="Enter text")
        label0.pack(pady=(5, 5))

        self.text = Entry(self.root, width=50)
        self.text.pack(pady=(5, 10), ipady=4)

        analysis = Button(self.root, text="Analyze", width=30, height=5, command=self.do_emotion)
        analysis.pack(pady=(20, 10))

        self.emotion_result = Label(self.root, text='', bg='#34495E', fg='white')
        self.emotion_result.pack(pady=(16, 12))
        self.emotion_result.configure(font=('verdana', 8))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment(self):
        text=self.text.get()
        result=self.apio.sentiment_analysis(text)
        txt =""
        for i in result:
            txt = txt + i + ' -> ' + str(result[i]) + '\n'
        print(txt)
        self.sentiment_result['text'] = txt


    def do_ner(self):
        text=self.text.get()
        entity=self.entity.get()
        result=self.apio.ner(text,entity)
        txt=""
        if "result" in result:  # Check if API returned expected data
            for i in result["result"]:
                txt += " " + i.get("text", "") +"\n" # Extract text safely
        else:
            txt = "No entities found."

        self.ner_result['text'] = txt

    def do_emotion(self):
        text=self.text.get()
        result=self.apio.emotion(text)
        emotion=list(result.keys())
        score=list(result.values())
        self.emotion_result["text"]=str(emotion[score.index(max(score))])
        print(self.emotion_result["text"])




    def clear(self ):
        for i in self.root.slaves():
            i.destroy()



nlp=NLPApp()