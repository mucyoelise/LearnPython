import re

def main():
    print(parse(input("HTML: ")))


def parse(s:str):
    attr_list = s.split(' ')
    for attr in attr_list:
        if attr.startswith('src'):
            if url := re.search(r'("https?://(?:www\.)?youtube\.com/.+")', attr):
                return format_url(url.group(1))
            return None

def format_url(url:str):
    url = url.replace('"', '').replace('youtube.com', 'youtu.be')
    url = url.replace('http:','https:').replace('/embed','').replace('www.','')
    return url

if __name__ == "__main__":
    main()