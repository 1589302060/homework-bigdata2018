import requests#因为空间不多了，不想重复下载，所以没有再多测试一遍，相信大家手里都有数据吧
import os
r = requests.get('http://yang.lzu.edu.cn/data/index.txt')
content = r.text.splitlines(False) #按换行符分割
paths = []
for path in content:
    if path.endswith("json"):
        path = path.lstrip('./')
        paths.append(path)
file_names = [path.split('/')[-1] for path in paths]
urls = list(map(lambda x: r'http://yang.lzu.edu.cn/data/'+x,paths))
file_path = r'C:\Users\15893\Desktop\320180941141-juyida\homework10'#还要改路径，很麻烦的啊
url_files = dict(zip(urls,file_names))
for url , file_name in url_files.items():
    try:
        r = requests.get(url)
    except:
        print('访问失败,file_name未保存')
    with open(os.path.join(file_path,file_name),'w') as f:
        f.write(r.text)
        f.close()
        print(file_name+'已保存')
print('已完成')