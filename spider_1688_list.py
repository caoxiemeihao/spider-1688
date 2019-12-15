import json
import re
from request import get_with_ua


def get_html(keywords):
    url = 'https://p4psearch.1688.com/p4p114/p4psearch/offer.htm?keywords={}'.format(keywords)
    html = get_with_ua(url)
    with open('./raw/list.html', 'w', encoding='utf8') as f:
        f.write(html.text)
    data = re.findall(r'<script.*?>(.*?)</script>', html.text, re.S)
    # filter(lambda txt:'pageConfig' in txt, data)
    # print(data)
    data = list(filter(filter_data, data))
    data = data[0] if len(data) else ''
    # data = data.replace('var pageConfig = ', '').rstrip(';')
    data = re.findall(r'"listOffer":(.*),[\n\s]*"relativeWords"', data)
    # print(data[0])
    data = data[0] if len(data) else ''
    print(data)
    data = json.loads(data)
    print(json.dumps(data, indent=4, ensure_ascii=False))
    with open('./raw/list.json', 'w', encoding='utf8') as f2:
        json.dump(data, f2, indent=4, ensure_ascii=False)


def filter_data(txt):
    # print(txt)
    return 'pageConfig' in txt


if __name__ == "__main__":
    get_html('手机壳')
