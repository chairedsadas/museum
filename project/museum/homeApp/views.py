from django.shortcuts import render
from newsApp.models import MyNew
from django.db.models import Q
from collectionApp.models import Product


def home(request):
    # 新闻展报
    newList = MyNew.objects.all().filter(~Q(
        newType='通知公告')).order_by('-publishDate')
    postList = set()
    postNum = 0
    for s in newList:
        if s.photo:
            postList.add(s)
            postNum += 1
        if postNum == 3:  # 只截取最近的3个展报
            break

    # 新闻列表
    if (len(newList) > 7):
        newList = newList[0:7]

        # 产品中心
    productList = Product.objects.all().order_by('-views')
    if (len(productList) > 4):
        productList = productList[0:4]

    return render(request, 'home.html', {
        'active_menu': 'home',
        'postList': postList,
        'newList': newList,
    })
