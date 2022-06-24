
url = input()
site = url.replace("http://", "")
site = site[:site.index(".")]
pwd = site[:3]+str(len(site))+str(site.count("e"))+"!"
print(f"{url}의 비밀번호는 {pwd}입니다.")
