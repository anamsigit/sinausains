import streamlit as st
from pathlib import Path
import base64
import re
import os

setsituasi1 = 0

def markdown_images(markdown):
    images = re.findall(r'(!\[(?P<image_title>[^\]]+)\]\((?P<image_path>[^\)"\s]+)\s*([^\)]*)\))', markdown)
    return images

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def img_to_html(img_path, img_alt):
    img_format = img_path.split(".")[-1]
    img_html = f'<img src="data:image/{img_format.lower()};base64,{img_to_bytes(img_path)}" alt="{img_alt}" style="max-width: 100%;">'
    return img_html

def markdown_insert_images(markdown):
    images = markdown_images(markdown)
    for image in images:
        image_markdown = image[0]
        image_alt = image[1]
        image_path = image[2]
        image_path = image_path.replace("../", "")
        if os.path.exists(image_path):
            markdown = markdown.replace(image_markdown, img_to_html(image_path, image_alt))
    return markdown

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def display_article(article):
    st.write(f"# {article['title']}")
    with st.container():
        st.markdown(markdown_insert_images(read_markdown_file(article['content'])), unsafe_allow_html=True)

def listdirektori(dirpath):
    listing = []
    for root, dirs, files in os.walk(f"NOTEBOOKS/{dirpath}"):
        for file in files:
            listing.append(os.path.join(root, file))
    return listing

def contents(dirdisiplin, indexdisiplin):
    for item in listdirektori(dirdisiplin):
        judul, _ = os.path.splitext(os.path.basename(item))
        indexdisiplin.append({"title": judul, "content": item})

indexmatematika = []
indexfisika = []
indexkimia = []
indexbiologi = []

if setsituasi1 == 0:
    contents("FISIKA", indexfisika)
    contents("MATEMATIKA", indexmatematika)
    contents("KIMIA", indexkimia)
    contents("BIOLOGI", indexbiologi)

def main():
    article_titles_matematika = [article['title'] for article in indexmatematika]
    article_titles_fisika = [article['title'] for article in indexfisika]
    article_titles_kimia = [article['title'] for article in indexkimia]
    article_titles_biologi = [article['title'] for article in indexbiologi]

    with st.sidebar:
        st.title("⚛ sinausains")
        st.markdown("## ilmu alam dan turunanya")

    disiplin_pilihan = st.sidebar.selectbox("disiplin", ["Matematika", "Fisika", "Kimia", "Biologi"])

    if disiplin_pilihan == "Matematika":
        artikel_pilihan = st.sidebar.selectbox("konten", article_titles_matematika)
        selected_article_index = next((index for index, article in enumerate(indexmatematika) if article['title'] == artikel_pilihan), None)
    elif disiplin_pilihan == "Fisika":
        artikel_pilihan = st.sidebar.selectbox("konten", article_titles_fisika)
        selected_article_index = next((index for index, article in enumerate(indexfisika) if article['title'] == artikel_pilihan), None)
    elif disiplin_pilihan == "Kimia":
        artikel_pilihan = st.sidebar.selectbox("konten", article_titles_kimia)
        selected_article_index = next((index for index, article in enumerate(indexkimia) if article['title'] == artikel_pilihan), None)
    elif disiplin_pilihan == "Biologi":
        artikel_pilihan = st.sidebar.selectbox("konten", article_titles_biologi)
        selected_article_index = next((index for index, article in enumerate(indexbiologi) if article['title'] == artikel_pilihan), None)
    else:
        selected_article_index = None
            
    if selected_article_index is not None:
        disiplin_articles = {
            "Matematika": indexmatematika,
            "Fisika": indexfisika,
            "Kimia": indexkimia,
            "Biologi": indexbiologi
        }

        selected_article = disiplin_articles[disiplin_pilihan][selected_article_index]
        display_article(selected_article)

    print(artikel_pilihan)


if __name__ == "__main__":
    main()
