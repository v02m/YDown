import wx
import wx.lib.agw.advprogressbar as PB
from core.yt_downloader import download_video

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Ввод ссылки на видео
        self.url_label = wx.StaticText(self.panel, label="Введите ссылку на YouTube:")
        self.sizer.Add(self.url_label, 0, wx.ALL, 5)
        self.url_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.url_input, 0, wx.ALL | wx.EXPAND, 5)

        # Выбор папки
        self.path_label = wx.StaticText(self.panel, label="Выберите папку для сохранения:")
        self.sizer.Add(self.path_label, 0, wx.ALL, 5)
        self.path_input = wx.TextCtrl(self.panel, style=wx.TE_READONLY)
        self.sizer.Add(self.path_input, 0, wx.ALL | wx.EXPAND, 5)
        self.path_button = wx.Button(self.panel, label="Выбрать папку")
        self.path_button.Bind(wx.EVT_BUTTON, self.on_select_folder)
        self.sizer.Add(self.path_button, 0, wx.ALL, 5)

        # Выбор качества
        self.quality_label = wx.StaticText(self.panel, label="Выберите качество:")
        self.sizer.Add(self.quality_label, 0, wx.ALL, 5)
        self.quality_choice = wx.Choice(self.panel, choices=["Наилучшее качество", "1080p", "720p", "480p", "Только аудио (MP3)"])
        self.sizer.Add(self.quality_choice, 0, wx.ALL, 5)

        # Прогресс-бар
        self.progress_bar = PB.AdvProgressBar(self.panel)
        self.sizer.Add(self.progress_bar, 0, wx.ALL | wx.EXPAND, 5)

        # Статус загрузки
        self.status_label = wx.StaticText(self.panel, label="")
        self.sizer.Add(self.status_label, 0, wx.ALL, 5)

        # Кнопка "Скачать"
        self.download_button = wx.Button(self.panel, label="Скачать")
        self.download_button.Bind(wx.EVT_BUTTON, self.on_download)
        self.sizer.Add(self.download_button, 0, wx.ALL, 5)

        self.panel.SetSizer(self.sizer)

    def on_select_folder(self, event):
        with wx.DirDialog(self, "Выберите папку для сохранения", style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.path_input.SetValue(dialog.GetPath())

    def on_download(self, event):
        url = self.url_input.GetValue()
        path = self.path_input.GetValue()
        quality = self.quality_choice.GetStringSelection()

        download_video(url, path, quality, self.progress_bar, self.status_label, self)

def create_form():
    app = wx.App(False)
    frame = MyFrame(None, title="YouTube Downloader", size=(500, 300))
    frame.Show()
    app.MainLoop()
