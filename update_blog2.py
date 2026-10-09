with open("index.html", "r") as f:
    content = f.read()

# Replace the date and author for the second blog
content = content.replace(
    "slug: 'aluminium-vs-steel-handles-for-new-home',\n                title: 'Why We Choose Aluminium Handles Over Steel Handles for a New Home',\n                date: 'October 5, 2026',\n                author: 'RISHABH VIRANI',",
    "slug: 'aluminium-vs-steel-handles-for-new-home',\n                title: 'Why We Choose Aluminium Handles Over Steel Handles for a New Home',\n                date: 'September 15, 2026',\n                author: 'Ronak Vekariya',"
)

# Replace the signature at the bottom of the second blog
content = content.replace(
    "Written by RISHABH VIRANI</p>\n                `,\n                image: 'assets/blog_kitchen.jpg'\n            },",
    "Written by Ronak Vekariya</p>\n                `,\n                image: 'assets/blog_kitchen.jpg'\n            },"
)

with open("index.html", "w") as f:
    f.write(content)

print("Blog 2 updated successfully.")
