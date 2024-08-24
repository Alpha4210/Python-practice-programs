import pandas as pd
import datetime

def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with the subject: {sub} and message {msg}")

if __name__ == "__main__":
    df = pd.read_excel("data.xlsx") #Used to read an excel file
    print(df)
    # today = datetime.datetime.now() #Used to get today's date and current time
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%y")
    writeInd = []
    for index, item in df.iterrows(): #df.iterrows() is used to access values in a row
        # print(index, item['Birthday']) #item['value'] will show the values in the row named 'value'
        bday = item['Birthday'].strftime("%d-%m")
        if (bday==today) and (yearNow not in str(item['Year'])):
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
            writeInd.append(index)