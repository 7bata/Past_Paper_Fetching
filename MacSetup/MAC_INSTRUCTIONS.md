# 在Mac上构建和运行独立应用程序

## 构建步骤

### 1. 准备工作
确保你的Mac上已安装Python 3。打开终端并运行以下命令来检查：
```bash
python3 --version
```

### 2. 安装必要的工具
```bash
# 安装项目依赖
pip3 install requests lxml

# 安装py2app（Mac专用打包工具）
pip3 install py2app
```

### 3. 构建AS和A Level下载器
```bash
# 进入ASALEVEL_Project目录
cd ASALEVEL_Project

# 构建应用
python3 setup.py py2app
```
构建完成后，应用将位于`dist`文件夹中，名为`ASALEVEL.app`。

### 4. 构建IGCSE下载器
```bash
# 进入IGCSE_Project目录
cd ../IGCSE_Project

# 构建应用
python3 setup.py py2app
```
构建完成后，应用将位于`dist`文件夹中，名为`IGCSE.app`。

## 使用应用程序

1. 在Finder中打开相应的`dist`文件夹。
2. 双击`.app`文件运行应用程序。
3. 根据提示选择要下载的科目组。
4. 文件将下载到应用程序创建的`downloads`文件夹中。

## 故障排除

- 如果遇到"未识别的开发者"警告，请按住Control键并点击应用程序图标，然后选择"打开"。
- 如果应用无法启动，请尝试在终端中通过以下命令运行：
  ```bash
  open -a /path/to/your/app
  ```
- 下载大量文件可能需要较长时间，请保持耐心。

## 注意

- 应用程序会在当前目录创建`downloads`和`logs`文件夹。
- 请尊重XtremePapers网站的资源，避免频繁下载。 