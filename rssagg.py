import feedparser,datetime,pickle

#function to initiate aggregation of RSS feeds
def feedagg():
 #import feeds from CERT and MSFT
 msft = feedparser.parse("https://technet.microsoft.com/en-us/security/rss/bulletin")
 cert = feedparser.parse("https://www.kb.cert.org/vulfeed")
 getrec(msft)
 getrec(cert)

def createpick(stream):
 pickle.dump([stream.entries[0].title],open(stream+".p",'wb')
 

 
def getrec(stream):
 if stream.bozo:
  print ('%s RSS invalid',str(stream))
  exc = stream.bozo_exception
  print (exc.getMessage())
 else:
  pickwrite = createpick(stream)
  readpick = pickle.load(open(stream+'.p','r')
 #compare first record of feed and the pickle to check for new updates 
  for post in stream.entries:
   if pickread == post.title:
    print('no new updates from %s',str(stream))
   else:
    print (post.title+":"+post.link+"\n")

 
  
def main():
 try:
  feedagg()
 except (RuntimeError,NameError,TypeError,pickle.PickleError) as e:
  print("RSS error -",e)
 
if __name__ == '__main__':
 main()
