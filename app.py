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

#user傳以下文字的話會跳到各個不同的def
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
    elif text.find("我要記帳") != -1:
        acc(event.reply_token)     
    elif text.find("食") != -1:
        food(event.reply_token)
    elif text.find("行") != -1:
        trans(event.reply_token) 
    elif text.find("樂") != -1:
        fun(event.reply_token)
    elif text.find("其他") != -1:
        other(event.reply_token)
    elif text.find("心理測驗") != -1:
        test(event.reply_token)  
    elif text.find("1.A") != -1:
        test2(event.reply_token)
    elif text.find("1.B") != -1:
        test2(event.reply_token) 
    elif text.find("1.C") != -1:
        test2(event.reply_token)               
    elif text.find("2.A") != -1:
        test3(event.reply_token)   
    elif text.find("2.B") != -1:
        test3(event.reply_token)  
    elif text.find("2.C") != -1:
        test3(event.reply_token)       
    elif text.find("3.A") != -1:
        test4(event.reply_token)
    elif text.find("3.B") != -1:
        test4(event.reply_token)
    elif text.find("3.C") != -1:
        test4(event.reply_token)
    elif text.find("4.A") != -1:
        test5(event.reply_token)
    elif text.find("4.B") != -1:
        test5(event.reply_token) 
    elif text.find("4.C") != -1:
        test5(event.reply_token)    
        pass
    else:
        default(event.reply_token)

#左右滑
def acc(reply_token):

    carousel_template = CarouselTemplate(columns=[

        CarouselColumn(text='食物', title='食',thumbnail_image_url='https://i.imgur.com/1HwOvRC.png', 

            actions=[

                MessageTemplateAction(

                    label='食', text='食')

        ]),

        CarouselColumn(text='交通', title='行',thumbnail_image_url='https://i.imgur.com/SmrcGt4.png', 

            actions=[

                MessageTemplateAction(

                    label='行', text='行')

        ]),

        CarouselColumn(text='娛樂', title='樂',thumbnail_image_url='https://i.imgur.com/3PKG2Lj.png',

            actions=[

                MessageTemplateAction(

                    label='樂', text='樂')

        ]),

        CarouselColumn(text='其他項目', title='其他',thumbnail_image_url='https://i.imgur.com/GtWspZb.png', 

            actions=[

                MessageTemplateAction(

                    label='其他', text='其他')

        ])

    ])

    template_message = TemplateSendMessage(

        alt_text='我要記帳', template=carousel_template)

    

    line_bot_api.reply_message(reply_token, template_message)

   #食 
def food(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='食', text='請選擇下方分類',
        #按鈕區域的圖片
        thumbnail_image_url = 'https://i.imgur.com/1HwOvRC.png', 
        #兩個按鈕
        actions=[
            MessageTemplateAction(label='「早餐」', text='早餐'),
            MessageTemplateAction(label='「午餐」', text='午餐'),
            MessageTemplateAction(label='「晚餐」', text='晚餐')
        ])
    template_message = TemplateSendMessage(
        alt_text='食', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)
#行 
def trans(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='行', text='請選擇下方分類',
        #按鈕區域的圖片
        thumbnail_image_url = 'https://i.imgur.com/SmrcGt4.png', 
        #兩個按鈕
        actions=[
            MessageTemplateAction(label='「公車」', text='公車'),
            MessageTemplateAction(label='「捷運」', text='捷運')
        ])
    template_message = TemplateSendMessage(
        alt_text='行', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)
#樂 
def fun(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='樂', text='請選擇下方分類',
        #按鈕區域的圖片
        thumbnail_image_url = 'https://i.imgur.com/3PKG2Lj.png', 
        #兩個按鈕
        actions=[
            MessageTemplateAction(label='「唱歌」', text='唱歌'),
            MessageTemplateAction(label='「玩桌遊」', text='玩桌遊'),
            MessageTemplateAction(label='「看電影」', text='看電影')
        ])
    template_message = TemplateSendMessage(
        alt_text='樂', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)
#其他
def other(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='其他', text='請選擇下方分類',
        #按鈕區域的圖片
        thumbnail_image_url = 'https://i.imgur.com/GtWspZb.png', 
        #兩個按鈕
        actions=[
            MessageTemplateAction(label='「影印」', text='影印'),
            MessageTemplateAction(label='「日常用品」', text='日常用品'),
            MessageTemplateAction(label='「雜支」', text='雜支')
        ])
    template_message = TemplateSendMessage(
        alt_text='其他', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)
#心理測驗&第一題
def test(reply_token):
    message1 = TextMessage(text="來測驗自己適合甚麼方法投資吧!")
    
    buttons_template = ButtonsTemplate(
        title='1.假如你的朋友找你一起創業，你會？', text='請選擇以下按鈕',
        actions=[

            MessageTemplateAction(label='A.當然要把握機會！', text='1.A'),
            MessageTemplateAction(label='B.再回去思考一下', text='1.B'),
            MessageTemplateAction(label='C.算了，我不想要虧錢', text='1.C')

        ])

    template_message = TemplateSendMessage(
        alt_text='心理測驗', template=buttons_template)
    line_bot_api.reply_message(
        reply_token,
        [message1,template_message])        

#心理測驗第二題
def test2(reply_token):
   
    buttons_template = ButtonsTemplate(
        title='2.與朋友出去玩，活動都是由誰決定？', text='請選擇以下按鈕',
        actions=[

            MessageTemplateAction(label='A.幾乎都是以我的意見為主', text='2.A'),
            MessageTemplateAction(label='B.大家一起討論並尋求共識', text='2.B'),
            MessageTemplateAction(label='C.我不喜歡出主意', text='2.C')

        ])

    template_message = TemplateSendMessage(
        alt_text='第二題', template=buttons_template)
    line_bot_api.reply_message(
        reply_token,
        template_message)      

#心理測驗第三題
def test3(reply_token):
   
    buttons_template = ButtonsTemplate(
        title='3.某公司正在打折，滿五千元才有贈品，你會？', text='請選擇以下按鈕',
        actions=[

            MessageTemplateAction(label='A.馬上行動', text='3.A'),
            MessageTemplateAction(label='B.看看贈品是甚麼再決定', text='3.B'),
            MessageTemplateAction(label='C.完全不會心動', text='3.C')

        ])

    template_message = TemplateSendMessage(
        alt_text='第三題', template=buttons_template)
    line_bot_api.reply_message(
        reply_token,
        template_message)    
#心理測驗第四題
def test4(reply_token):
   
    buttons_template = ButtonsTemplate(
        title='4.工作時遇到麻煩都是如何處置？', text='請選擇以下按鈕',
        actions=[

            MessageTemplateAction(label='A.自己趕快想辦法解決啊', text='4.A'),
            MessageTemplateAction(label='B.聽聽看別人的意見', text='4.B'),
            MessageTemplateAction(label='C.慢慢思考後再解決', text='4.C')

        ])

    template_message = TemplateSendMessage(
        alt_text='第四題', template=buttons_template)
    line_bot_api.reply_message(
        reply_token,
        template_message)        

#心理測驗第五題
def test5(reply_token):
   
    buttons_template = ButtonsTemplate(
        title='5.如果有人報你明牌，即將大漲，你會？', text='請選擇以下按鈕',
        actions=[

            MessageTemplateAction(label='A.趕快湊錢買上幾張', text='5.A'),
            MessageTemplateAction(label='B.找來股價走勢圖並評估', text='5.B'),
            MessageTemplateAction(label='C.不相信有這麼好康的事情', text='5.C')

        ])

    template_message = TemplateSendMessage(
        alt_text='第五題', template=buttons_template)
    line_bot_api.reply_message(
        reply_token,
        template_message) 

#自我介紹(文字+貼圖+圖片)
# customize function
def selfIntroduction(reply_token):
    message1 = TextMessage(text="我是黃品瑄，現在就讀於台灣科技大學資管所碩士班一年級。我的個性穩重、善解人意，事認真負責。我喜歡與夥伴溝通，在待人我處事上總是可以尊重、聽取他人的想法。我的興趣是旅行與攝影，回憶旅行中的任何大小事是我平常最喜歡的紓壓方式。")
    #image_url1 = createUri('/static/pics/ya-wen.png')
    #image1 = ImageSendMessage(original_content_url=image_url1,preview_image_url=image_url1)
    message2 = ImageSendMessage(
        #傳圖片
    original_content_url='https://i.imgur.com/E1sszHt.jpg',
    preview_image_url='https://i.imgur.com/E1sszHt.jpg')
    #傳貼圖，網路上可以查到不同貼圖的id
    sticker1 = StickerSendMessage(
        package_id='3',
        sticker_id='247')
    
    line_bot_api.reply_message(
        reply_token,
        [message1,sticker1,message2])
#得獎經歷(純文字)
def prize(reply_token):
    message1 = TextMessage(text="2018/台灣科技大學邁向頂尖大學計畫/資管系碩士班優秀新生/獲獎\n"+"2017/東吳大學修讀學士學位優秀學生/第三名\n"+"2016/東吳大學資訊管理學系學科獎/系統分析與設計科目/第一名\n"+"2016/東吳資管第二屆系服設計大賽/第一名\n"+"2015/東吳資管朱賢泓系友優秀學生獎學金")
    
    line_bot_api.reply_message(
        reply_token,
        message1)        


#工作經歷(按鈕兩個，點下去都是傳文字)
def workExperience(reply_token):
    
    buttons_template = ButtonsTemplate(
        title='工作經歷', text='請選擇下方按鍵來了解更多：',
        #按鈕區域的圖片
        thumbnail_image_url = 'https://i.imgur.com/KHmX12t.jpg', 
        #兩個按鈕
        actions=[
            MessageTemplateAction(label='「勤業眾信風險諮詢實習」', text='勤業眾信風險諮詢實習'),
            MessageTemplateAction(label='「東吳大學課程助教」', text='東吳大學課程助教')
        ])
    template_message = TemplateSendMessage(
        alt_text='工作經歷', template=buttons_template)
    
    line_bot_api.reply_message(reply_token, template_message)
#大學專題(按鈕兩個，點第一個是傳文字+圖片，第二個是youtube的連結)
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
#大學專題-專題介紹
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

#工作經歷-東吳大學課程助教
def TA(reply_token):
    message1 = TextMessage(text="office商業軟體應用這堂課主要教授PowePoint、Word、Access、Excel等的使用，擔任課程助教協助上課時各個示範使用步驟的操作，以及在上課期間巡堂看看班上的同學有沒有操作上的問題，並教導他們如何操作。在上課前我會自行研讀office的相關教授書籍以熟悉各軟體內不同的功能的使用方式，並且在期中期末考結束後負責在講台向全班解說各個題目在不同情境時如何在商業軟體上進行操作。")
    line_bot_api.reply_message(reply_token, message1)
#工作經歷-勤業
def intern(reply_token):
    message1 = TextMessage(text="主要工作內容:\n"+"1.分析部門內不同服務的營收，並製成視覺化的Excel報表\n"+"2.部門內紙本流程系統化專案，了解系統功能需求並協助設計系統功能\n"+"3.維護及測試風險管理表單系統，參與該系統修改的專案\n"+"4.年度Kick-Off Team Building活動籌辦、協尋活動場地\n"+"5.製作部門內每月的Newsletter電子報")
    
    line_bot_api.reply_message(reply_token, message1)
#參賽經歷(傳文字跟三張照片)
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


#求學歷程(傳文字)
def education(reply_token):
    message1 = TextSendMessage(text="(1)大學:大學我就讀東吳大學資訊管理學系，大學期間我沒有缺席過任何一堂課，每件事都用心做到最好，我在大二時考取了多益英語能力檢定855分接近金色證書的成績，我也曾獲得了學期總成績全班第三名；系統分析與設計課程第一名、資料庫管理課程第二名的佳績。除了本科系所學，我也不限制自己發展的領域，對外國語言充滿熱情的我，在大學期間曾經輔系日文系以及修習實用英語學程，並且利用大二暑期的時間參加東吳大學所辦理的海外研修專題-附昆士蘭大學海外研習活動，因此在大學時認識了許多來自不同科系、專業的朋友。")

    message3 = TextSendMessage(text="(2)研究所:研究所時我以考試入學第一名的成績進入了國立台灣科技大學資訊管理研究所，並且加入了黃世禎教授指導的軟體工程與管理實驗室。碩一上學期作過比較印象深刻的專案是多媒體系統這堂課的Final Project，我們使用Python語言，透過CNN工具及TensorFlow框架、VGG 19模型，來實作“Style transfer”。此專案以機器學習的方式訓練圖片學習另一種畫風並轉換。研究所的期間我也會努力再學習更多的技術。")

    
    line_bot_api.reply_message(reply_token, [message1, message3])

#傳任意文字會出現的回覆(文字與貼圖)
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
#這沒用到
def createUri(pathName):
    return 'https://'+appName+'.herokuapp.com'+pathName
    
#加入好友的歡迎訊息，profile.display_name會抓使用者的名字
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
#port=5000是我在ngrok上的port
import os
if __name__ == "__main__":
    app.run(debug=True,port=5000)

