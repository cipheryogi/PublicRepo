import webbrowser

def goto_url(url):
    print(f"Navigating to: {url}")
    webbrowser.open(url)

s = ""
a = 3
while a != 1:
    s += str(a)
    if a % 2 == 0:
        a //= 2  # Using floor division to keep 'a' as an integer
    else:
        a = 3 * a + 1

goto_url("http://www.multisoft.se/" + s)