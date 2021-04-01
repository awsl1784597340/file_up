# Title

![logoo](/assert/logoo.png)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)



## Table of Contents

- [Introduction](#Introduction)
- [Install](#install)
- [Usage](#usage)
- [API](#api)

## Introduction

本项目为微信小程序的配套后端图床服务器项目，用于部署在网页上以及本地服务器上。

运行安装API见下文

## Install

```shell
pip install -r requirements.txt
```

## Usage

```shell
python3 app.py
```

## API

#### GET /list

返回图片列表，返回一个list

example return

```javascript
{"code": 200, "filelist": ["-336b16b38c468f1f.jpg", "177bb999267d9a88.jpg", "-1c76b09a93d5f2c3.jpg", "03.jpg", "01.jpg", "-1f6ca453ab94199a.jpg"]}
```

#### GET /uploads/\<filename>

filename 为上一个请求中的图片名称

返回一张图片

本请求可以作为一个图片url插入html的src链接中

示例：

https://file-up.vercel.app/uploads/-336b16b38c468f1f.jpg 