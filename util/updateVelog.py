import requests
import re
import os

CONST_URL = "https://velog.io/@hyeok_1212"
CONST_COUNT = 3

def make_latest_blog(url, conut):
    latest_blog = ""
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.text

        matches = re.findall(r'"url_slug":"(.*?)"', data)
        if matches:
            count = 0
            for match in matches:
                url_slug = match.replace("\\", "")
                if count >= 3:
                    break
                latest_blog += "- [" + f"{url_slug}" + "]" + "(" + url + "/" + f"{url_slug}" + ")</br>"
                count += 1
            return latest_blog
        else:
            print("No match found")
    else:
        print("Request failed with status code:", response.status_code)

def make_readme(latest_blogs):
    return f"""## Yehyeok Bang
 Hi I'm Yehyeok 👋</br>
 Growing Backend Developer🌱
 
<h3>I'm studying 📖</h3>
<div style="display:inline">
<img src="https://img.shields.io/badge/Java-007396?style=for-the-badge&logo=OpenJDK&logoColor=white"/> 
<img src="https://img.shields.io/badge/spring-6DB33F?style=for-the-badge&logo=spring&logoColor=white"> <img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <br />
</div>

<h3>Welcome my 🙌</h3>
<a href="https://velog.io/@hyeok_1212" target="_blank"><img src="https://img.shields.io/badge/velog-99FFCC?style=for-the-badge&logo=VELOG&logoColor=003300"/></a>
<a href="mailto:qkddpgur318@gmail.com"><img src="https://img.shields.io/badge/Gmail-D0A9F5?style=for-the-badge&logo=Gmail&logoColor=white&link=mailto:wonjongah@gmail.com"/></a>

<h3>Algorithm ✏️</h3>
 
[![Solved.ac Profile](http://mazassumnida.wtf/api/generate_badge?boj=aksk333)](https://solved.ac/aksk333)

<!-- <h3>GitHub stats :seedling:</h3>

![YehyeokBang's GitHub stats](https://github-readme-stats.vercel.app/api?username=YehyeokBang&show_icons=true&theme=gruvbox)
-->
<h3>Most Used Languages 🥇</h3>

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=YehyeokBang&layout=compact&theme=dark)](https://github.com/jogilsang/jogilsang)  

<h3>Latest Blogs 😄</h3>
{latest_blogs}

"""

if __name__ == "__main__":
    readme = make_readme(make_latest_blog(CONST_URL, CONST_COUNT))
    parent_dir = os.path.dirname(os.getcwd())
    readme_path = os.path.join(parent_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme)




