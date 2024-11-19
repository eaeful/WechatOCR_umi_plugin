# 适用于 Umi-OCR 文字识别工具 的 WeChatOCR 插件


WeChatOCR 是一款专为 [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR) 设计的文字识别插件。

---

## 插件介绍

通过将 WeChatOCR 插件加载到 Umi-OCR，可以直接使用微信 OCR 的强大功能来识别文字。

### 与其他插件（如 PaddleOCR）的对比优势

- 👍**精准度更高**：对生僻字和使用频率较低的字符识别效果优于 PaddleOCR。
- 👍**速度略胜一筹**：识别速度相比 PaddleOCR 略快。
- 👍**多语言支持**：支持中文、英文、日语等多语言的自动识别，无需手动切换语言模型。
- 👍**智能换行**：当排版解析方案设置为 “不处理” 时，识别内容会根据输出结果自动换行。如果不需要换行，可将排版解析方案设置为 “单栏-无换行”。

---
试一试用WeChatOCR和PaddleOCR识别下面这个图：
![18-230537](https://github.com/user-attachments/assets/4f13b12f-c09e-4566-b859-306dddd49944)
![对比](https://github.com/user-attachments/assets/186c4900-7c37-4beb-b0f7-9ec97c2cb226)



## 插件版本说明

WeChatOCR 插件提供以下两种版本，供用户选择：

### 1. 微信本地 OCR 模型版本

- 插件内置了关键文件：`wechatocr.exe`、`wechat` 文件夹、`mmmojo.dll` 和 `mmmojo_64.dll`等。
- **无需安装微信，也无需运行微信**，即可直接调用微信 OCR 功能完成文字识别。

### 2. 微信 OCR 用户自定义路径版本

- 用户需在 Umi-OCR 的全局设置中，手动填写以下路径：
  - 微信安装目录的完整路径。
  - `WeChatOCR.exe` 文件路径。

  **要使用此版本，您需要准备以下内容：**

  - **`wechatocr.exe`**：例如  
    `C:\Users\![18-230537](https://github.com/user-attachments/assets/fd707587-7bd2-4f09-87b6-8c46e7106d5d)
yourname\AppData\Roaming\Tencent\WeChat\XPlugin\Plugins\WeChatOCR\7061\extracted\WeChatOCR.exe`
  - **`wechat` 文件夹**：例如  
    `C:\Program Files (x86)\Tencent\WeChat\[3.9.8.25]`

  配置完成后，即可调用本地微信进行文字识别。

---

## 两个版本的区别

| 特性               | 微信本地 OCR 模型版本           | 微信 OCR 用户自定义路径版本    |
|--------------------|---------------------------------|--------------------------------|
| **初次识别速度**   | 可能首次加载稍慢（多约数百毫秒），后续识别正常    | 可能首次加载稍慢（多约数百毫秒），后续识别正常   |
| **使用便捷性**     | 更加便捷，无需额外配置          | 需手动配置路径，稍微复杂       |
| **版权与 LICENSE** | 可能涉及版权和 LICENSE 风险     | 用户自行选择路径，版权更灵活，建议选择这个版本   |

---

## 使用说明

1. 下载并解压插件包，放入 Umi-OCR/UmiOCR-data/plugins 文件夹中。。
2. 打开 Umi-OCR，并加载 WeChatOCR 插件。
3. （可选）根据版本选择是否配置路径：
   - **本地 OCR 模型版本**：无需额外配置，直接使用。
   - **用户自定义路径版本**：在 Umi-OCR 设置中填写对应路径，并准备所需文件和文件夹。
4. 开始识别文字！

---

## 注意事项

- 两个版本在首次加载时可能会有轻微的延迟，但后续识别速度无差异。
- 使用本地 OCR 模型版本时，请确保遵循相关版权协议和 LICENSE 要求。

---

## 感谢
- https://github.com/kanadeblisst00/wechat_ocr
- https://github.com/EEEEhex/QQImpl
- https://github.com/swigger/wechat-ocr
- https://www.52pojie.cn/thread-1959012-1-1.html
- https://www.52pojie.cn/thread-1958424-1-1.html

---

欢迎通过 Issue 或 Pull Request 提交建议和改进意见！ 🎉
