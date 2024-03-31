# AutoDriverCopy
在学校中，由于需要课后将上课老师所展示的PPT内容进行复习，因此经常需要向老师索要PPT文件。然而，有时老师会拒绝提供文件，这就造成了一些困扰。  
为了解决这个问题，开发了 AutoDriverCopy 工具。它可以在老师插入U盘后自动读取其中的文件，并将后缀为 `.ppt` 或 `.pptx` 的文件复制到指定目录下。  

## 使用方法

1. 运行程序后，会弹出一个TK窗口，用于设置最近文件个数和要检测的盘符。  
2. 在弹出的窗口中，输入要获取的最近文件的数量和要检测的盘符，然后点击“确定并运行”按钮。点击后窗口会消失并在后台运行。  
3. 在老师插入U盘后，程序会自动将PPT文件复制到指定目录下。
4. 下课后，打开目录`D:\getfromusb`即可查看复制的文件。`D:\getfromusb\lastlog.txt`是本次复制任务的日志文件。

**注意：**
- 在运行程序前，需要将自己的U盘插入计算机，并注意其驱动器头（如"E"、"U"、"F"等）。  
- 确保程序在后台运行，以便在老师插入U盘后自动执行复制操作。  

## 运行原理

1. 用户通过TK窗口设置要获取的最近文件的数量和要检测的盘符。  
2. 程序在后台不断检测系统中插入的U盘。  
3. 当检测到U盘插入时，程序会自动将其中的PPT文件复制到指定目录下。  

## TODO
- [x] 可自定义最近文件复制个数
- [ ] 可自定义复制的文件后缀

