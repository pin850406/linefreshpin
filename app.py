from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom, BaseSize, ImagemapArea,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction, URIImagemapAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageSendMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, ImagemapSendMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('BaV2jhZRr3nkCg8XeEXuzEYeUgjDO1opnnHJsy6Evfb/cnvursyt9hRG07tg/htpJDiTm9FftEppB9wSLoj3md9oTFE4KUSv+LNJ+LfprA2mKYyOjlUuGUZfME21DWwBaxylvHoMWBCR9r7TMT/kfgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5baf84e499afd4ca9d152a9e5af26715')
# Heroku App Name
appName = 'pinh'

# 監聽所有來自 /callback 的 Post Request
@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text =  event.message.text
    # message = TextSendMessage(text=event.message.text)
    if text.find("自我介紹") != -1:
        selfIntroduction(event.reply_token)
    elif text.find("工作經歷") != -1:
        workExperience(event.reply_token)
    elif text.find("東吳大學課程助教") != -1:
        TA(event.reply_token)
    elif text.find("勤業眾信風險諮詢實習") != -1:
        intern(event.reply_token)
    elif text.find("求學歷程") != -1:
        education(event.reply_token)
    elif text.find("得獎經歷") != -1:
        prize(event.reply_token)    
    elif text.find("大學專題") != -1:
        project(event.reply_token)
    elif text.find("專題介紹") != -1:
        projectd(event.reply_token)
    elif text.find("參賽經歷") != -1:
        comp(event.reply_token)          
        
        pass
    else:
        default(event.reply_token)



# customize function
def selfIntroduction(reply_token):
    message1 = TextMessage(text="我是黃品瑄，現在就讀於台灣科技大學資管所碩士班一年級。我的個性穩重、善解人意，事認真負責。我喜歡與夥伴溝通，在待人我處事上總是可以尊重、聽取他人的想法。我的興趣是旅行與攝影，回憶旅行中的任何大小事是我平常最喜歡的紓壓方式。")
    #image_url1 = createUri('/static/pics/ya-wen.png')
    #image1 = ImageSendMessage(original_content_url=image_url1,preview_image_url=image_url1)
    message2 = ImageSendMessage(
    original_content_url='https://i.imgur.com/E1sszHt.jpg',
    preview_image_url='https://i.imgur.com/E1sszHt.jpg')
    sticker1 = StickerSendMessage(
        package_id='3',
        sticker_id='247')
    
    line_bot_api.reply_message(
        reply_token,
        [message1,sticker1,message2])

def prize(reply_token):
    message1 = TextMessage(text="2018/台灣科技大學邁向頂尖大學計畫/資管系碩士班優秀新生/獲獎\n"+"2017/東吳大學修讀學士學位優秀學生/第三名\n"+"2016/東吳大學資訊管理學系學科獎/系統分析與設計科目/第一名\n"+"2016/東吳資管第二屆系服設計大賽/第一名\n"+"2015/東吳資管朱賢泓系友優秀學生獎學金")
    
    line_bot_api.reply_message(
        reply_token,
        message1)        



def workExperience(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='工作經歷', text='請選擇下方按鍵來了解更多：',
        thumbnail_image_url = 'https://i.imgur.com/KHmX12t.jpg', 
        actions=[
            MessageTemplateAction(label='「勤業眾信風險諮詢實習」', text='勤業眾信風險諮詢實習'),
            MessageTemplateAction(label='「東吳大學課程助教」', text='東吳大學課程助教'),
        ])
    template_message = TemplateSendMessage(
        alt_text='工作經歷', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def project(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='大學畢業專題', text='請點選以下按鈕了解品瑄的大學專題：',
        thumbnail_image_url = 'https://i.imgur.com/2tS85NP.jpg', 
        actions=[
            MessageTemplateAction(label='專題介紹', text='專題介紹'),
            URITemplateAction(label='專題影片', uri='https://www.youtube.com/watch?v=IT1poa3s0q8&t=2s'),
           
        ])
    template_message = TemplateSendMessage(
        alt_text='大學專題', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)

def projectd(reply_token):
    message1 = TextMessage(text="大學畢業專題入圍了第22 屆全國大專校院資訊應用服務創新競賽，我們的主題和AR擴增實境技術有關。這是我第一次參加全國性的比賽，比賽時與評審的問答考驗了我們的臨場反應，同時也能觀摩其他同學們的創意與技術應用。在專題組中我擔任組長，這個角色讓我學習在一年的期間中，要如何領導一個團隊，並協調每個成員的工作與心情。")
    message2= TextMessage(text="運用技術:\n"+"(1)Android Studio：Android系統開發，使用JAVA程式設計語言。\n"+"(2)Unity：使用PTC提供的Vuforia套件進行AR的開發，使用C#程式設計語言。\n"+"(3)Adobe Illustrator：手機介面美術製作。\n"+"(4)Adobe Photoshop：手機介面美術製作。\n"+"(5)Autodesk Remake：餐點立體圖像建模。")
    message3 = ImageSendMessage(
    original_content_url='https://i.imgur.com/OfK3cFH.png',
    preview_image_url='https://i.imgur.com/OfK3cFH.png')

    line_bot_api.reply_message(
        reply_token,
        [message1,message2,message3])     
"""def TA(reply_token):
    image_url1 = createUri('/static/pics/TA.jpg')
    
    line_bot_api.reply_message(reply_token, template_message)"""

def TA(reply_token):
    message1 = TextMessage(text="office商業軟體應用這堂課主要教授PowePoint、Word、Access、Excel等的使用，擔任課程助教協助上課時各個示範使用步驟的操作，以及在上課期間巡堂看看班上的同學有沒有操作上的問題，並教導他們如何操作。在上課前我會自行研讀office的相關教授書籍以熟悉各軟體內不同的功能的使用方式，並且在期中期末考結束後負責在講台向全班解說各個題目在不同情境時如何在商業軟體上進行操作。")
    line_bot_api.reply_message(reply_token, message1)

def intern(reply_token):
    message1 = TextMessage(text="主要工作內容:\n"+"1.分析部門內不同服務的營收，並製成視覺化的Excel報表\n"+"2.部門內紙本流程系統化專案，了解系統功能需求並協助設計系統功能\n"+"3.維護及測試風險管理表單系統，參與該系統修改的專案\n"+"4.年度Kick-Off Team Building活動籌辦、協尋活動場地\n"+"5.製作部門內每月的Newsletter電子報")
    
    line_bot_api.reply_message(reply_token, message1)

def comp(reply_token):
    message1 = TextMessage(text="參賽經歷:\n"+"1.2017第22屆全國大專校院資訊應用服務創新競賽產學合作組:入圍\n"+"2.東吳大學資管系畢業專題競賽:佳作\n"+"3.東吳大學商學院創意競賽-資訊應用組:佳作")
    message2 = ImageSendMessage(
    original_content_url='https://i.imgur.com/2tS85NP.jpg',
    preview_image_url='https://i.imgur.com/2tS85NP.jpg')
    message3 = ImageSendMessage(
    original_content_url='https://i.imgur.com/vgJFiIN.jpg',
    preview_image_url='https://i.imgur.com/vgJFiIN.jpg')
    message4 = ImageSendMessage(
    original_content_url='https://i.imgur.com/asn356V.jpg',
    preview_image_url='https://i.imgur.com/asn356V.jpg')
    line_bot_api.reply_message(reply_token, [message1,message2,message3,message4])



def education(reply_token):
    message1 = TextSendMessage(text="(1)大學:大學我就讀東吳大學資訊管理學系，大學期間我沒有缺席過任何一堂課，每件事都用心做到最好，我在大二時考取了多益英語能力檢定855分接近金色證書的成績，我也曾獲得了學期總成績全班第三名；系統分析與設計課程第一名、資料庫管理課程第二名的佳績。除了本科系所學，我也不限制自己發展的領域，對外國語言充滿熱情的我，在大學期間曾經輔系日文系以及修習實用英語學程，並且利用大二暑期的時間參加東吳大學所辦理的海外研修專題-附昆士蘭大學海外研習活動，因此在大學時認識了許多來自不同科系、專業的朋友。")

    message3 = TextSendMessage(text="(2)研究所:研究所時我以考試入學第一名的成績進入了國立台灣科技大學資訊管理研究所，並且加入了黃世禎教授指導的軟體工程與管理實驗室。碩一上學期作過比較印象深刻的專案是多媒體系統這堂課的Final Project，我們使用Python語言，透過CNN工具及TensorFlow框架、VGG 19模型，來實作“Style transfer”。此專案以機器學習的方式訓練圖片學習另一種畫風並轉換。研究所的期間我也會努力再學習更多的技術。")

    
    line_bot_api.reply_message(reply_token, [message1, message3])


def default(reply_token):
    message1 = TextMessage(text="請輸入下列關鍵字或點選圖文選單來更認識品瑄：\n"+
                                "「自我介紹」\n"+
                                "「工作經歷」\n"+
                                "「求學歷程」\n"+
                                "「大學專題」\n"+
                                "「得獎經歷」\n"+"「參賽經歷」")
    sticker1 = StickerSendMessage(
        package_id='2',
        sticker_id='164')
    
    line_bot_api.reply_message(
        reply_token,
        [message1,
        sticker1])

def createUri(pathName):
    return 'https://'+appName+'.herokuapp.com'+pathName
    

@handler.add(FollowEvent)
def handle_follow(event):
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text='嗨' + profile.display_name+ '，歡迎加入這個Line bot來認識黃品瑄Pin-Shiuan！\n'+
                                                                                 "請輸入下列關鍵字或點選圖文選單來更認識品瑄：\n"+
                                "「自我介紹」\n"+
                                "「工作經歷」\n"+
                                "「求學歷程」\n"+
                                "「大學專題」\n"+
                                "「得獎經歷」\n"+"「參賽經歷」"))

import os
if __name__ == "__main__":
    app.run(debug=True,port=5000)

