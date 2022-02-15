"""
    views.py
"""
import tensorflow as tf

from django.shortcuts import render
from sampleSite.forms import IndexForm
from sampleSite.models import Kweet
from sampleSite.models import Kakeibo
from sampleSite.forms import KakeiboForm
from sampleSite.forms import Application1Form
from sampleSite.forms import Application2Form
from sampleSite.forms import Application4Form
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http.response import JsonResponse

#mac用 ssl通信系のエラーが発生した場合は、下のコメントを外す
#import ssl
#ssl._create_default_https_context = ssl._create_unverified_context
vgg16model = tf.keras.applications.vgg16.VGG16(weights='imagenet',include_top=True)

messageList = []
kakeiboList=[]
kakeibo=[]
num1 = 0
num2 = 0

def graph(request):
    return render(request,'graph.html')

def get_graph_data(request):
    allInoutData = Kakeibo.objects.values('opt').annotate(
        total=Sum('suuji')
    )
    return JsonResponse(list(allInoutData),safe=False)

def index(request):
    form = IndexForm(request.POST or None)
    message = form["message"].data or ''

    if message != '':
        #メッセージの内容をDBに登録
        kweetModel = Kweet(message=message)
        kweetModel.save()
    #Kweetの内容をすべて取得
    kweetList = Kweet.objects.all()
    dbData={
        "id": 123,
        "name": "name",
        "form": form,
        "kweetList": kweetList
    }
    return render(request, 'index.html', dbData)

@login_required(login_url='/login/')
def page2(request):
    return render(request, 'page2.html')

def application1(request):
    form = Application1Form(request.POST or None)
    num1 = form['num1'].data or 0
    num2 = form['num2'].data or 0
    sisoku = form['sisoku'].data or 0
    result = ''

    print(str(num1))
    print(str(num2))
    print(str(sisoku))
    if form['sisoku'].data == "+":
            result= int(num1) + int(num2)
    if form['sisoku'].data == "-":
            result=  int(num1) - int(num2)
    if form['sisoku'].data == "*":
            result=  int(num1) * int(num2)
    if form['sisoku'].data == "/":
            result=  int(num1) / int(num2)

    return render(request, 'application1.html', {
        "result":result
    })

mondai=["アプリ開発講座"]
score = [0]
def application2(request):
    
    form = Application2Form(request.POST or None)
    if form['text'].data != None:
        if mondai[0] ==form['text'].data:
            score +=1
    return render(request,'application2.html',{
        "mondai":mondai[0],
        "score":score
    })

def application4(request):
    global Vgg16model
    # tf.keras.backend.clear_session()
    # tf.keras.backend.set_learning_phase(0)
    # formからPOSTしてきた情報を、Application4Formクラスに設定。データがなければNoneを設定。
    form = Application4Form
    results = None

    if request.method =='POST':
        form = Application4Form(request.POST, request.FILES)
        if not form.is_valid():
            raise ValueError
        form.save()

        # アップロードした画像ファイルを読み込み、224x224にリサイズする
        img_pil = tf.keras.preprocessing.image.load_img(form.cleaned_data['gazou'], target_size=(224, 224))
        # 読み込んだ画像をarrayに変換
        img = tf.keras.preprocessing.image.img_to_array(img_pil)
        # 3次元テンソル（rows, cols, channels) を
        # 4次元テンソル (samples, rows, cols, channels) に変換
        # 入力画像は1枚なのでsamples=1でよい
        img = img[tf.newaxis, ...]
        # 画像をVGG16の事前学習時と同じ状態に合わせて変換
        # (入力値から学習時の平均値を引いて平均を0に変換する中心化とRGB⇒BGRへの変換を行う)
        img_preprocessed = tf.keras.applications.vgg16.preprocess_input(img)
        # 予測値を算出し、Top5のクラスを表示する
        preds = vgg16model.predict(img_preprocessed)
        results = tf.keras.applications.vgg16.decode_predictions(preds, top=5)[0]
        for result in results:
            print(result)

    dbData = {
        "id":123,
        "name":"name",
        "form":form,
        "results":results
    }
    return render(request,'application4.html',dbData)


def kakeibo(request):
    sum = 0
    money=0
    suuji=0
    form = KakeiboForm(request.POST or None)
    #それぞれに値を代入
    date = form["date"].data or ''
    opt = form["opt"].data or ''
    message = form["message"].data or ''
    suuji = form["suuji"].data or ''
    #いったん表示はいりまーす
    print(str(date))
    print(str(opt))
    print(str(message))
    print(str(suuji))
    
    if suuji != '':
        kakeiboModel = Kakeibo(date=date, opt=opt,message=message,suuji=suuji)
        kakeiboModel.save()
    #kakeiboの内容をすべて取得
    kakeiboList = Kakeibo.objects.all()

    for kakeibo in kakeiboList:
        #print(str(kakeibo.suuji))
        money=kakeibo.suuji
        sum+=money
        #print(sum)

    print(form)
    
    dbData={
        "id": 123,
        "name": "name",
        "form":form,
        "kakeiboList": kakeiboList,
        "sum":sum
    }
    return render(request, 'kakeibo.html',dbData)
