import re

#reads html Itemlist and returns it in json format
def html_to_id_name_dict_simple(html_content):
    id_to_name = {}
    
    # Pattern to match table rows and extract ID and name
    pattern = r'<tr>\s*<td>(\d+)</td>.*?<td>(.*?)</td>\s*</tr>'
    
    matches = re.findall(pattern, html_content, re.DOTALL)
    
    for item_id, item_name in matches:
        # Clean up the name (remove any HTML tags)
        clean_name = re.sub(r'<[^>]+>', '', item_name).strip()
        id_to_name[int(item_id)] = clean_name
    

    return id_to_name


with open('ItemList', 'r') as file:
        htmlcontent = file.read()
        
if __name__== '__main__':
    item_dict = html_to_id_name_dict_simple(htmlcontent)

    print(item_dict)