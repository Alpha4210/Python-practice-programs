# import pandas as pd
# import datetime

# def sendEmail(to, sub, msg):
#     print(f"Email to {to} sent with the subject: {sub} and message {msg}")

# if __name__ == "__main__":
#     df = pd.read_excel("data.xlsx") #Used to read an excel file
#     print(df)
#     # today = datetime.datetime.now() #Used to get today's date and current time
#     today = datetime.datetime.now().strftime("%d-%m")
#     yearNow = datetime.datetime.now().strftime("%y")
#     writeInd = []
#     for index, item in df.iterrows(): #df.iterrows() is used to access values in a row
#         # print(index, item['Birthday']) #item['value'] will show the values in the row named 'value'
#         bday = item['Birthday'].strftime("%d-%m")
#         if (today==bday) :
#             sendEmail(item['Email'], "Happy Birthday", item['Dialogue'])
#             writeInd.append(index)
#     print(writeInd)
    
import pandas as pd
import datetime
import smtplib #Used for sending mail
import os
os.chdir(r"D:\MyData\Business\code playground\Python Practice Programs\birthday wisher")
# os.mkdir("testing") 

# Enter your authentication details
GMAIL_ID = ''
GMAIL_PSWD = ''


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    # Below code is for sending email
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}") #(from, to, body)
    s.quit()
    

if __name__ == "__main__":
    #just for testing
    # sendEmail(GMAIL_ID, "subject", "test message")
    # exit()

    df = pd.read_excel("data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(type(today))
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday) 
        if(today == bday) and yearNow not in str(item['Year']):
            
            sendEmail(item['Email'], "Happy Birthday", item['Dialogue']) 
            writeInd.append(index)

    # print(writeInd)
    for i in writeInd:
        yr = df.loc[i, 'Year']
        df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
        # print(df.loc[i, 'Year'])

    # print(df) 
    df.to_excel('data.xlsx', index=False)  #Convert df(dataframe) to excel, index=false for avoid getting the useless rows from getting created