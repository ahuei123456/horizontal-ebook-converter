import bs4


def edit_html(filenames):
    for filename in filenames:
        soup = _open_file(filename)
        _remove_vertical(soup)
        _remove_furigana(soup)
        _remove_spaces(soup)
        _write_file(filename, soup)


def _open_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        soup = _soup_file(file)

    return soup


def _soup_file(file):
    soup = bs4.BeautifulSoup(file, 'html.parser')

    return soup


def _write_file(filename, soup):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


def _remove_vertical(soup):
    tag = soup.find(class_='vrtl')
    if tag is None:
        return
    if ('vrtl' in tag['class']):
        del tag['class']
    else:
        tag['class'] = tag['class'].remove('vrtl')


def _remove_furigana(soup):
    tags = soup.find_all('rt')
    for tag in tags:
        tag.decompose()


def _remove_spaces(soup):
    tags = soup.find_all('p')
    for tag in tags:
        if 'class' not in tag and tag.contents[0].name != 'a':
            line = ''
            for string in tag.stripped_strings:
                line += string
            if line is '':
                continue
            tag.clear()
            tag.append(line)
