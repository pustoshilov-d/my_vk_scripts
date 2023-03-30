# conda activate pattern
from pattern3 import web
import requests


with open('temp2.html','r', encoding="utf-8") as doc:
    page = doc.read().encode('ascii', 'ignore')
    dom = web.Element(page)
    # print(dom[:100])
    artists =  dom.by_class("audio_row__performers")
    titles =  dom.by_class("audio_row__title_inner")

    with open('save tracks.txt', 'w') as save_to:
      for i in range(len(artists)):
        strt = artists[i].by_tag("a")[0].content+' - '+titles[i].content + '\n'
        print(strt)
        print(str(i)+' of ' + str(len(artists)))
        save_to.write(strt)

    # abstr = dom.by_id("enc-abstract").by_tag("p")[0].content.replace("\\n", "").replace("\n", "")
    # abstr = str(id) + "\t" +re.sub('\<.*\>', '', abstr).strip()
    # abstr = abstr+'\n'
    # print(abstr)
    # doc.write(abstr)
    # # print(dom.by_tag("abstracttext")[0].content)

    doc.close()
