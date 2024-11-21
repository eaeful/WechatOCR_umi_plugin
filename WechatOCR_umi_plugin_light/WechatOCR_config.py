from plugin_i18n import Translator

# UI翻译
tr = Translator(__file__, "i18n.csv")

globalOptions = {
    "title": tr("微信OCR(不自带模型，请填写自己的路径)"),
    "type": "group",
    "wechat_ocr_dir": {
        "title": tr("WeChatOCR.exe 文件路径"),
        "toolTip": tr(
            "WeChatOCR.exe 的文件路径。"
        ),
        "default": "",
    },
    "wechat_dir": {
        "title": tr("微信的完整安装路径"),
        "toolTip": tr(
            "微信的完整安装路径，例如：C:\\Program Files (x86)\\Tencent\\WeChat\\[3.9.8.25]。"
        ),
        "default": "",
    },
}

localOptions = {
    "title": tr("微信OCR(不自带模型，请填写自己的路径)"),
    "type": "group",
}
