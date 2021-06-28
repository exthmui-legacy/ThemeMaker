# ThemeMaker

[CH](https://github.com/exthmui/ThemeMaker/blob/master/README.md) | EN

This tool is used to make themes for `exTHmUI`.

`template` folder is a template for themes.

## License
- Apache Version 2.0

## Requirements
- x86_64 enviroment (Windows Or Linux)
- Python 3
- JRE

## Usage
`make.py <src> <out> [resource packages]`

### Examples
- `./make.py template/ template.apk`
- `./make.py template/ template.apk framework-res.apk SystemUI.apk`

## Note
- Before using, please use the tool named `get_resapk` to get `framework-res.apk`.
- According to the `overlay` that is used in the target theme, you might need to acquire *target apk* into the `resource packages`.
- All files in the `bin` folder come from [Android SDK Build Tools](https://android.googlesource.com/platform/prebuilts/fullsdk/build-tools/)

# Making themes

## How does it work?
exTHmUI theme engine uses methods similar to [Substratum](https://github.com/substratum/), editing the system resources by controlling the overlay.

For fonts and boot animation, exTHmUI uses custom resolving ways.

## Theme template structure
```
/
├── AndroidManifest.xml
├── assets
│   ├── backgrounds           <--- Wallpapers(lockscreen)
│   ├── fonts                 <--- Fonts and font configuration
│   ├── media                 <--- Boot animation(light and dark included)
│   ├── previews              <--- Theme preview
│   └── sounds                <--- Sounds(notification, alarm, etc)
├── overlay                   <--- Overlay
└── res
    ├── drawable
    │   ├── theme_banner      <--- Banner for the theme preview
    │   ├── theme_icon        <--- Theme icons
    │   └── theme_image       <--- Pictures of the configuration page
    ├── values
    │   ├── bools.xml         <--- Part of the configuration
    │   └── strings.xml       <--- Theme name and author
    └── xml
        └── theme_data.xml    <--- Configuration of theme resources
```

## Theme template
Please refer to the `template` folder.

## Signing
If you want to sign your theme,

You just need to replace `testkey.pk8` and `testkey.x509.pem` with your own keys.

You might need to edit `make.py` for signing configurations.
