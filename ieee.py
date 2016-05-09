import webbrowser
import base64

def Space(j):
    i = 0
    while i<=j:
        print(" "),
        i+=1
def Credit():
    Space(9); print("#####################################")
    Space(9); print("#   IEEE PAPERS DOWNLOADER(Free)    #")
    Space(9); print("#     Scripted by CYBA TIGER        #")
    Space(9); print("#         GHOSTFLEET.ORG            #")
    Space(9); print("#####################################")

Credit()
afn=raw_input("ENTER THE AUTHOR FIRST NAME: ")
asn=raw_input("ENTER THE AUTHOR SECOND NAME: ")
asn=asn.lower()
num=raw_input("ENTER THE DOI DETAILS : ")
year=raw_input("ENTER THE YEAR OF PUBLISH: ")

encoded=base64.b64encode(num)
url="http://cyber.sci-hub.cc/"+encoded+"/"+asn+year+".pdf"
webbrowser.open(url)

