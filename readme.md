# HenianSB STG

<p align="center">
  <br><br>
  <img width="33.3%" src="docs/images/readme/heniansb.jpg">
  <br><br><br><br>
</p>

天依的一款弹幕设计游戏，使用Python和Pygame开发

**仅供娱乐！！！！！！！**

## 安装
此项目支持 x86-64 架构的 Windows、Linux、MacOS 操作系统，暂不支持 ARM 架构的设备 (M1/M2 的 Apple 设备可以使用转译)。

请前往 GitHub Release 页面下载最新版本的安装包。

## 开发

开发环境要求：
 - Python 3.9～3.11
 - PDM 2.8.x

您可以运行以下命令安装 PDM：

**Linux/MacOS**
```shell
curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
```

**Windows (PowerShell)**
```powershell
(Invoke-WebRequest -Uri https://pdm.fming.dev/install-pdm.py -UseBasicParsing).Content | python -
```
请在 PowerShell 中运行上述命令，不要在 cmd 中运行。

然后您需要安装依赖：
```shell
git clone https://github.com/Catfootbeats/HenianSB_STG.git
cd HenianSB_STG
pdm install
```

您可以使用以下命令运行游戏：
```shell
pdm run start
```

## 编译
您可以使用以下命令编译游戏：
```shell
pdm run build
```

编译后的文件位于 `dist` 文件夹中，由于 pyinstaller 不支持交叉编译，故只能编译当前平台的可执行文件。

