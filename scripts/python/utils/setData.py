# pixmap支持的格式
pixmap_exts = [
    "bmp",
    "cur",
    "gif",
    "icns",
    "ico",
    "jpeg",
    "jpg",
    "pbm",
    "pdf",
    "pgm",
    "png",
    "ppm",
    "svg",
    "tga",
    "tiff",
    "tif",
    "xbm",
    "xpm",
]

# 图片格式

# 图片格式
img_formats = [
    "jpg",
    "jpeg",
    "png",
    "tif",
    "tiff",
    "exr",
    "hdr",
    "psd",
    "tx",
    "tga",
    "rat",
    "xbm",
    "xpm",
    "ppm",
    "svg",
    "pbm",
    "pdf",
    "bmp",
    "cur",
    "gif",
    "icns",
    "ico",
]

# 代码消息
code_dict = {
    "1301": {"en": "Bind success", "zh": "绑定成功"},
    "1302": {
        "en": "This email or CDKey is incorrect, please check your email and CDKey.",
        "zh": "该邮箱或CDKey不正确,请检查邮箱和CDKey.",
    },
    "1304": {
        "en": "The CDKey has expired, please apply for a new one.",
        "zh": "CDKey已过期,请申请新CDKey.",
    },
    "1305": {
        "en": "This device has been bound, the CDKey still has {count} times left for rebind.",
        "zh": "此设备已绑定,CDKey还有{count}次重新绑定机会.",
    },
    "1309": {
        "en": "The CDKey has been used beyond the limit, please apply for a new one.",
        "zh": "CDKey已超过使用次数,请申请新CDKey.",
    },
    "3001": {
        "en": "Server connection failed, please contact: 723120326@qq.com",
        "zh": "服务器连接失败,请联系: 723120326@qq.com",
    },
    "3002": {
        "en": "Failed to get device ID, please contact: 723120326@qq.com",
        "zh": "获取设备ID失败,请联系: 723120326@qq.com",
    },
    "3003": {
        "en": "Signature generation failed, please contact: 723120326@qq.com",
        "zh": "签名生成失败,请联系: 723120326@qq.com",
    },
    "3004": {"en": "Invalid email format", "zh": "邮箱格式无效"},
}


SETDATA = {
    "pixmap_exts": pixmap_exts,
    "img_formats": img_formats,
    "code_dict": code_dict,
}
