import feedparser,datetime,pickle

#function to initiate aggregation of RSS feeds
def feedagg():
 #import feeds from CERT and MSFT
 msft = feedparser.parse("https://technet.microsoft.com/en-us/security/rss/bulletin")
 cert = feedparser.parse("https://www.kb.cert.org/vulfeed")
 getrec(msft)
 getrec(cert)

 
def getrec(stream):
 if stream.bozo:
  print ('%s RSS invalid',str(stream))
  exc = stream.bozo_exception
  print (exc.getMessage())
 else:
  #put first record for update check -- to be implemented later WIP
  first_record = ([stream.entries[0].title])
 #compare first record of feed and the tuple to check for new updates 
  for post in stream.entries:
   if first_record[0] == post.title:
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
