# ThemeMaker

CH | [EN](https://github.com/exthmui/ThemeMaker/blob/master/README_en.md)

本工具用于制作 `exTHmUI` 的主题

`template` 文件夹为主题模板

## License
- Apache Version 2.0

## Requirements
- x86_64 enviroment (Windows Or Linux)
- Python 3
- JRE

## Usage
`make.py <src> <out> [resource packages]`

### 示例
- `./make.py template/ template.apk`
- `./make.py template/ template.apk framework-res.apk SystemUI.apk`

## Note
- 在使用前请先使用 `get_resapk` 工具获取 `framework-res.apk`
- 根据主题中包含的 `overlay`，可能还需要手动提取 *目标apk* 加入 `resource packages`
- `bin` 文件夹下的所有文件来自 [Android SDK Build Tools](https://android.googlesource.com/platform/prebuilts/fullsdk/build-tools/)

# 主题制作

## 工作原理
exTHmUI 主题使用了与 [Substratum](https://github.com/substratum/) 类似的方案，通过控制叠加层来进行系统资源的修改

对于字体和开机动画，exTHmUI 使用定制的解析方法。

## 主题模板结构
```
/
├── AndroidManifest.xml
├── assets
│   ├── backgrounds           <--- 壁纸与锁屏壁纸
│   ├── fonts                 <--- 字体与字体配置文件
│   ├── media                 <--- 开机动画(包含亮色与暗色)
│   ├── previews              <--- 主题预览图
│   └── sounds                <--- 声音 (来电铃声、通知提示与闹钟)
├── overlay                   <--- 存放叠加层
└── res
    ├── drawable
    │   ├── theme_banner      <--- 主题预览页的横幅
    │   ├── theme_icon        <--- 主题图标
    │   └── theme_image       <--- 主题选择界面的图像
    ├── values
    │   ├── bools.xml         <--- 包含部分配置
    │   └── strings.xml       <--- 包含主题名称与作者
    └── xml
        └── theme_data.xml    <--- 主题资源配置
```

## 主题模板
请参考 `template` 文件夹

## 自签名
如果想要将主题上架到应用市场，则需要使用自己的证书对 apk 进行签名。

只需将 `testkey.pk8` 和 `testkey.x509.pem` 替换为自己的公钥和私钥。

视情况可能需要修改 `make.py` 中的签名参数
