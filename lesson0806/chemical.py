import requests
from bs4 import BeautifulSoup

def fetch_element_table():
    # Wikipedia 頁面的 URL
    url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"

    # 發送請求並獲取頁面內容
    response = requests.get(url)
    response.raise_for_status()  # 確保請求成功

    # 解析 HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到化學元素表格
    table = soup.find("table", {"class": "wikitable"})

    # 提取表頭
    th_tags = table.find_all("th")
    headers = [th.text.strip() for th in th_tags]

    # 提取表格數據
    elements = []
    for row in table.find_all("tr")[1:]:  # 跳過表頭
        cols = row.find_all("td")
        if len(cols) > 1:
            element_data = [col.text.strip() for col in cols]
            elements.append(element_data)

    return headers, elements

def print_element_table(headers, elements):
    # 打印表頭
    print(f"{' | '.join(headers)}")
    print("-" * 100)

    # 打印每一行數據
    for element in elements:
        print(f"{' | '.join(element)}")

def main():
    headers, elements = fetch_element_table()
    print_element_table(headers, elements)

if __name__ == "__main__":
    main()
