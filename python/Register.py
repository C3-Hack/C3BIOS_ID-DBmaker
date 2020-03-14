import wx
import csv
import pprint

####エラー画面のクラス
class Error(wx.Frame):
    def __init__(self,parent):
        ##フレーム
        wx.Frame.__init__(self,parent,-1,"エラー",pos=(100,100),size=(600,300))
        panel = wx.Panel(self)

        ##テキスト
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.errortext = wx.StaticText(panel,-1, 'すでに登録されています！',pos=(50,100))
        self.errortext.SetFont(font)
        ##閉じるボタン
        self.exitBtn = wx.Button(panel,label="卵で閉じる",pos=(500,250))
        self.Bind(wx.EVT_BUTTON,self.exit,self.exitBtn)

    ##ボタン実装
    def exit(self,event):
        self.Close(True)

####登録完了の画面
class tourokuC(wx.Frame):
    def __init__(self,parent):
        ##ファイル読み込み
        with open('data.csv','r') as file:
            self.lines=file.readlines()
        row=self.lines[-1].split(',')

        ##フレーム
        wx.Frame.__init__(self,parent,1,"登録完了",pos=(300,300),size=(600,300))
        panel = wx.Panel(self)

        ##テキスト
        font = wx.Font(20, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.tourokuCtext = wx.StaticText(panel,-1, '登録完了！',pos=(50,50))
        self.tourokuCtext.SetFont(font)

        ##IDm,SDI,HNテキスト
        self.IDm_C_text = wx.StaticText(panel,-1, "IDm:"+row[0],pos=(50,100))
        self.SDI_C_text = wx.StaticText(panel,-1, "SID:"+row[1],pos=(50,120))
        self.tourokuCtext = wx.StaticText(panel,-1,"HN:"+row[2].strip(),pos=(50,140))
        ##閉じるボタン
        self.exitBtn = wx.Button(panel,label="息の根を止める",pos=(500,250))
        self.Bind(wx.EVT_BUTTON,self.exit,self.exitBtn)

    def exit(self,event):
        self.Close(True)

####登録画面のクラス
class Touroku(wx.Frame):
    def __init__(self,parent,id):
        ##IDmの読み込み
        with open('data1.csv', 'r') as file:
            self.lines=file.readlines()
        ##フレーム
        wx.Frame.__init__(self,parent,id,"登録画面",size=(600,600))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('#AFAFAF')
        font = wx.Font(40, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font1=wx.Font(20, wx.FONTFAMILY_DEFAULT,wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        ##テキスト
        self.studentnumbertext=wx.StaticText(panel,-1, 'SID',pos=(50,200))
        self.handlenametext=wx.StaticText(panel,-1, 'HN',pos=(50,300))

        self.studentnumbertext.SetFont(font)
        self.handlenametext.SetFont(font)

        ##IDmのテキスト
        self.IDmnumbertext=wx.StaticText(panel,-1, "IDm  "+self.lines[-1].strip(),pos=(50,100))
        self.IDmnumbertext.SetFont(font)
        ##入力フォーム
        #self.IDm= wx.TextCtrl(panel, -1,pos=(150,100),size=(300,60))
        self.studentnumber = wx.TextCtrl(panel, -1,pos=(150,200),size=(300,60))
        self.handlename= wx.TextCtrl(panel, -1,pos=(150,300),size=(300,60))

        #self.IDm.SetFont(font)
        self.studentnumber.SetFont(font)
        self.handlename.SetFont(font)



        ##ボタン
        self.button_1 = wx.Button(panel,-1, '登録する',pos=(500,500))
        self.Bind(wx.EVT_BUTTON,self.check,self.button_1)

    def check(self,event):
         ##入力を取得
        #self.IDm1=self.IDm.GetValue()
        self.studentnumber1=self.studentnumber.GetValue()
        self.handlename1=self.handlename.GetValue()
        ## csvの読み込み
        flag=0
        with open('data.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                ##登録されているか検査
                if(row[1]==self.studentnumber1):
                    flag=-1
                    break
                else:
                    if(row[2]==self.handlename1):
                        flag=-1
                        break
                    else:
                        flag=1
            ##エラー検出
            if(flag<0):
                self.showChild(self)
            ##登録
            elif(flag==1):
            ##csvに書き込む
                with open('data.csv','a') as f:
                    writer = csv.writer(f)
                    writer.writerow([self.lines[-1].strip(),self.studentnumber1,self.handlename1])
                self.showChild2(self)

    def showChild(self,event):
        childFrame = Error(self)
        childID = childFrame.Show()

    def showChild2(self,event):
        childFrame2=tourokuC(self)
        childID2=childFrame2.Show()


####実装
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Touroku(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
