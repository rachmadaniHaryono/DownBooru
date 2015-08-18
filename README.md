# DownBooru ![](https://img.shields.io/badge/Python-3.4-blue.svg?style=flat-square)
###### Formerly known as GelDown

Simple Imageboard CLI Downloader.

**Supported imageboards**:
* Danbooru
* Gelbooru
* Safebooru
* Rule34
* Yande.re
* Konachan

**Usage**

```python
usage: main.py [-h] [--dir DIR] <tags> <limit> <booru>
```

Argument  | Description
------------- | -------------
| Tags  | Tags can be as simple as character name (e.g. misaka_mikoto, uzumaki_naruto) or by adding extra tag wrapped in quotation mark (e.g. "shana short_hair"). |
| Limit | Enter how much limit of images to download. |
| Booru | Enter imageboard you prefer to use. Refer to [list of supported keywords](https://github.com/Zerocchi/DownBooru/blob/master/docs/supported.md) |
| dir | Download folder |
**Dependencies**:
* BeautifulSoup4
