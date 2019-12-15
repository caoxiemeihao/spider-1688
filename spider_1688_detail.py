from request import get_with_ua
from lxml import html


def get_detail():
    url = 'https://detail.1688.com/offer/564393823842.html'
    text = get_with_ua(url).text
    # print(text)
    with open('./raw/detail.html', 'w') as f:
        f.write(text)
    xpath = '//div[@class="tab-pane"]//img/@src'
    selector = html.fromstring(text)
    res = selector.xpath(xpath)
    src = (res[0] if len(res) else '').replace('.400x400', '')
    # print(src)
    img = get_with_ua(src)
    with open('./data/{}'.format(src.split('/')[-1]), 'wb') as f:
        f.write(img.content)


if __name__ == '__main__':
    get_detail()