fonts

这里放置字体文件和字体配置(fonts_customization.xml)
注意：这里的字体文件都是空文件，不可直接应用！

字体配置文件的编写和Magisk字体模块类似，但又有所不同。主要体现在xml根节点由 <familyset> 变成了 <fonts-modification>
同时，在每个family节点中都增加了 customizationType 属性，它的值可以为 new-named-family 或者 new-fallback
new-named-family 表示这是一个新增的字体家族，或者是已有字体家族的扩充
new-fallback 表示这是对一个字体家族的 fallback 的扩充
对于指定为 new-fallback 的字体家族，它的 name 属性将会被忽略

具体的编写方法可以参考本文件夹下的 fonts.xml 和 fonts_customization.xml (由 fonts.xml 提取有用的部分转换而来)

