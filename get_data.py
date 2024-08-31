import re
import csv

with open('profile_page.txt', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'"buddy_id":"(\d+)","user":\{"id":"(\d+)","__isProfile":"User","name":"([^"]*)'

matches = re.findall(pattern, content)

def decode_name(name):
    return name.encode('utf-8').decode('unicode_escape')

unique_entries = {}
for match in matches:
    user_id = match[1]
    user_name = decode_name(match[2])
    if user_id not in unique_entries:
        unique_entries[user_id] = user_name

with open('result1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['stt', 'user_id', 'user_name', 'link_profile']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i, (user_id, user_name) in enumerate(unique_entries.items(), start=1):
        link_profile = 'https://www.facebook.com/' + user_id
        writer.writerow({'stt': i, 'user_id': user_id, 'user_name': user_name, 'link_profile': link_profile})

print("Dữ liệu đã được lưu vào tệp result.csv")
