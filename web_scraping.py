import requests
from bs4 import BeautifulSoup

http_error = """
<h1>HTTP ERROR!!!</h1>
<p>{}</p>
"""

conn_error = """
<h1>CONNECTION ERROR!!!</h1>
<p>{}</p>
"""

timeout_error = """
<h1>TIMEOUT ERROR!!!</h1>
<p>{}</p>
"""

def get_html():
    session = requests.Session()
    url = 'http://192.168.1.4/bWAPP/training.php'
    try:
        content = session.get(url)
        write_html = content.content
    except requests.HTTPError as e:
        write_html = str.encode(http_error.format(e))
    except requests.ConnectionError as e:
        write_html = str.encode(conn_error.format(e))
    except requests.Timeout as e:
        write_html = str.encode(timeout_error.format(e))
    finally:
        with open('my_html.html', 'wb') as w:
            temp = w.write(write_html)
        return write_html

def get_list(content):
    parsed_content = BeautifulSoup(content, 'html.parser')
    content_list = parsed_content('li')
    temp = []
    for each in content_list:
        temp.append(each.get_text())
    return temp

if __name__ == '__main__':
    content = get_html()
    content_list = get_list(content)
    print(content_list)