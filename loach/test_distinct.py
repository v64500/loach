# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open("I:\\fiddlerlog\\response\douyin.txt", mode='r') as f1:
        uids= set(f1.readlines())

    with open("I:\\fiddlerlog\\response\douyin_distinct.txt", mode="w") as f2:
        f2.writelines(uids)