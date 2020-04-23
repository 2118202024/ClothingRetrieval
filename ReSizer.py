import os

import wx
import random
class ReSizer():
    def __init__(self,plane, num):
        self.planeName=num # RecipesBitmap 名称
        self.sizer = wx.FlexGridSizer(6, 2, hgap=15, vgap=10)
        for x in range(12):
            bSizer1 = wx.BoxSizer(wx.VERTICAL)
            example_bmp1 = wx.Bitmap('1-2.jpg')
            # 图片
            name = self.planeName+"Bitmap" + str(x)
            m_bitmap1 = wx.StaticBitmap(plane,wx.ID_ANY, example_bmp1, wx.DefaultPosition, (220, 220), 0, name)
            bSizer1.Add(m_bitmap1, 0, wx.ALL, 5)
            # 菜名
            name = self.planeName+"Name" + str(x)
            m_staticText1 = wx.StaticText(plane, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0, name)
            m_staticText1.Wrap(1)

            self.sizer.Add(bSizer1, 0, wx.EXPAND, 5)
    def getSizer(self):
        return self.sizer
    def sizerClear(self):
        # 容器初始化，每次上图的时候调用
        for x in range(12):
            bmp = wx.Bitmap('C:/Users/zx/Desktop/ClothingRetrieval/picture/null.jpg')
            # 图片
            name = self.planeName + "Bitmap" + str(x)
            RecipesBitmap = wx.FindWindowByName(name=name)
            RecipesBitmap.SetBitmap(bmp)
            # 菜名
            name = self.planeName + "Name" + str(x)
            RecipesName = wx.FindWindowByName(name=name)
            RecipesName.LabelText = ""

    def changeSizer(self,label,path):
        # self.sizerClear()
        road = os.path.exists(path)
        pic_path = 'C:/Users/zx/Desktop/ClothingRetrieval/picture/%s/' % (label)
        path_list = os.listdir(pic_path)
        pic_list = random.sample(path_list, 12)
        for i in range(12):
            # road = os.path.exists("./picture/"+str(result)+"/1-"+str(i)+".jpg")

            if road:
                bmp = wx.Bitmap(pic_path+pic_list[i])
                # bmp = wx.Bitmap('picture/'+str(result)+'/1-%s.jpg' % str(i))
                # 图片
                name = self.planeName + "Bitmap" + str(i)
                RecipesBitmap = wx.FindWindowByName(name=name)
                RecipesBitmap.SetBitmap(bmp)
                # RecipesBitmap.SetToolTip(result[i][0])
            else:
                print('不存在')
