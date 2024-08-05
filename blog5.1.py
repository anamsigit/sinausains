import streamlit as st
from pathlib import Path
import base64
import re
import os
import streamlit_antd_components as sac

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

def build_tree_structure(base_path):
    def add_folder_to_tree(path):
        folder_name = os.path.basename(path)
        children = []
        for entry in os.listdir(path):
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                children.append(add_folder_to_tree(full_path))
            elif entry.endswith('.md'):
                # Tambahkan file Markdown sebagai node
                children.append(sac.TreeItem(entry, icon="dash"))
        return sac.TreeItem(folder_name, children=children)
    
    base_dir = os.path.join(base_path, 'Notebooks')
    
    tree_items = []
    for folder_name in os.listdir(base_dir):
        full_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(full_path):
            tree_items.append(add_folder_to_tree(full_path))
    
    return tree_items

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def display_article(article):
    st.write(f"# {article['title']}")
    with st.container():
        st.markdown(markdown_insert_images(read_markdown_file(article['content'])), unsafe_allow_html=True)

def find_file(nama_file):
    for root, dirs, files in os.walk("NOTEBOOKS"):
        if nama_file in files:
            return os.path.join(root, nama_file)


def main():
    with st.sidebar:
        st.title("⚛ sinausains")
        st.markdown("## ilmu alam dan turunanya")

        selected = sac.tree(items=build_tree_structure("."), 
                        label='Notebooks', 
                        index=0, 
                        align='left', 
                        size='md',
                        icon='box', 
                        open_all=True, 
                        checkbox=False, 
                        key="selectedhierarki")


    filemd = st.session_state['selectedhierarki']
    if '.md' in filemd:
        titlemd = filemd.removesuffix('.md')


        file = find_file(filemd)
        dictfrmt = {'title': titlemd,
                    'content': file}
        
        # dictfrmt = {'title': 'Antioksidan', 
        #             'content': 'NOTEBOOKS/KIMIA\\Antioksidan.md'}
        print(file)

        display_article(dictfrmt)
        #{'title': 'Antioksidan', 'content': 'NOTEBOOKS/KIMIA\\Antioksidan.md'}


if __name__ == "__main__":
    main()
