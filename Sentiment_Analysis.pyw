from tkinter import *
from textblob import TextBlob
from newspaper import Article

root = Tk()
root.title("SENTIMENT ANALYSIS")
width = 600 
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() 
x = (screen_width/2)-(width/2)
y = (screen_height/2)-(height-(height/4))
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.config(bg='grey30')
a=0

def start_analyse():
    url = urlbox.get("1.0", "end-1c")
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    text=article.summary
    print(text)

    blob=TextBlob(text)

    sentiment=blob.sentiment.polarity
    score = round(sentiment, 3)

    res="Neutral"
    if score>= 0.3:
        res="Positive"
    if score< 0.0:
        res="Negative"
    resultbox.config(state= NORMAL)
    resultbox.delete("1.0","end")
    resultbox.insert(INSERT,"\n")
    resultbox.insert(INSERT,score)
    resultbox.insert(INSERT," ")
    resultbox.insert(INSERT,res)
    resultbox.insert(INSERT,"\n\n")
    resultbox.insert(INSERT,text)
    resultbox.config(state= DISABLED)
    print(score)

analyse=Button(root,height=4,width=15,text="Analyse",bg='grey95',relief=FLAT,command=start_analyse)
analyse.grid(row=0,column=0,padx=10,pady=10)

urlbox=Text(root, height = 7, width = 55)
urlbox.grid(row=0,column=1,padx=10,pady=10)

resultbox=Text(root, height = 7, width = 55)
resultbox.config(state= DISABLED)

resultbox.grid(row=1,column=1,padx=10,pady=10)

root.wm_attributes('-toolwindow', 'True')
root.resizable(False,False)
root.mainloop()