# -*- coding: utf-8 -*-
import os
import wx
import wx.xrc
from ReSizer import ReSizer
import tensorflow as tf
import numpy as np
from keras.models import load_model
import cv2
cloth_dict={
0	:'牛仔裤',
1	:'鞋子',
2	:'双肩背包',
3   :'长袖外套',
4   :'鸭舌帽',
5   :'连衣裙'
}
model = load_model('my_model.h5')
wildcard = "jpg source (*.jpg)|*.jpg|"     \
           "png source (*.png)|*.png|" \
           "All files (*.*)|*.*"

class MyFrame1 ( wx.Frame ):
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1200,560 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gSizer1 = wx.GridSizer( 1, 2, 0, 0 )

        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        #
        # image = wx.Image('1-2.jpg', wx.BITMAP_TYPE_JPEG)
        # temp = image.ConvertToBitmap()
        #
        # self.bmp = wx.StaticBitmap(parent=self.m_panel2, bitmap=temp,size=(400,400))
        example_bmp1 = wx.Bitmap('1-2.jpg')
        # 图片
        name =  "Bitmap"
        m_bitmap1 = wx.StaticBitmap(self.m_panel2, wx.ID_ANY, example_bmp1, wx.DefaultPosition, (220, 220), 0, name)

        bSizer2.Add(m_bitmap1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"加载照片", wx.DefaultPosition, (200,50), 0 )
        bSizer2.Add( self.m_button1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
        self.m_button1.Bind(wx.EVT_BUTTON, self.OnButton1)


        self.m_panel2.SetSizer( bSizer2 )
        self.m_panel2.Layout()
        bSizer2.Fit( self.m_panel2 )
        gSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )

        sizer3=wx.BoxSizer( wx.VERTICAL )
        self.m_scrolledWindow1 = wx.ScrolledWindow(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                   wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        # self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer1.Add(self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
        self.RecipesSizer = ReSizer(self.m_scrolledWindow1, "FeaturedRecipes")
        self.picSizer = self.RecipesSizer.getSizer()
        sizer3.Add(self.picSizer, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        self.m_scrolledWindow1.SetSizer(sizer3)
        self.m_scrolledWindow1.Layout()
        # self.picSizer.Fit(self.m_panel3)
        # gSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass

    def OnButton1(self, evt):
        print("CWD: %s\n" % os.getcwd())

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(),
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_MULTIPLE |
                  wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST |
                  wx.FD_PREVIEW
        )

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()

            print('You selected %d files:' % len(paths))

            for path in paths:
                file_path=path

        # Compare this with the debug above; did we change working dirs?
        path_=os.getcwd()

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()

        # image = wx.Image(file_path, wx.BITMAP_TYPE_JPEG)
        # temp = image.ConvertToBitmap()
        # self.bmp = wx.StaticBitmap(parent=self.m_panel2, bitmap=temp, size=(300, 300))
        bmp = wx.Bitmap('C:/Users/zx/Desktop/ClothingRetrieval/picture/null.jpg')
        # 图片
        name = "Bitmap"
        RecipesBitmap = wx.FindWindowByName(name=name)
        RecipesBitmap.SetBitmap(bmp)
        bmp = wx.Bitmap(file_path)
        # 图片
        name = "Bitmap"
        RecipesBitmap = wx.FindWindowByName(name=name)
        RecipesBitmap.SetBitmap(bmp)

        img = cv2.imread(file_path )
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (220, 220))
        gray = gray.reshape(-1, 1, 220, 220) / 255.
        answer=int(np.argmax(model.predict(gray), axis=1))
        print("预测值  ：", cloth_dict[int(np.argmax(model.predict(gray), axis=1))])

        self.RecipesSizer.changeSizer(answer,path_)
        # self.picSizer = self.RecipesSizer.getSizer()
        print(answer)


class MyApp(wx.App):
    def OnInit(self):
        mainwin = MyFrame1(None)
        mainwin.CenterOnParent(wx.BOTH)
        mainwin.Show()
        mainwin.Center(wx.BOTH)
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()