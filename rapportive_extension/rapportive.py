import urllib2
from xml.dom import minidom


def name2email(fn, ln, domain):
    list = ["{fn}", '{ln}', '{fn}{ln}', '{fn}.{ln}', '{fi}{ln}', '{fi}.{ln}', '{fn}{li}', '{fn}.{li}', '{fi}{li}',
            '{fi}.{li}', '{ln}{fn}', '{ln}.{fn}', '{ln}{fi}', '{ln}.{fi}', '{li}{fn}', '{li}.{fn}', '{li}{fi}',
            '{li}.{fi}', '{fn}-{ln}', '{fi}-{ln}', '{fn}-{li}', '{fi}-{li}', '{ln}-{fn}', '{ln}-{fi}', '{li}-{fn}',
            '{li}-{fi}', '{fn}_{ln}', '{fi}_{ln}', '{fn}_{li}', '{fi}_{li}', '{ln}_{fn}', '{ln}_{fi}', '{li}_{fn}',
            '{li}_{fi}']
    emails = [];

    fi = fn[0]
    li = ln[0]

    for i in list:
        for a in [("{fn}", fn), ("{ln}", ln), ("{fi}", fi), ("{li}", li)]:
            i = i.replace(a[0], a[1])
        emails.append(i + "@" + domain)
    return emails


def get_oauth(cookie_li_at):
    opener = urllib2.build_opener()
    opener.addheaders.append(('cookie', 'li_at=' + cookie_li_at))
    opener.addheaders.append(('referer', 'https://mail.google.com/mail/u/0/'))
    f = opener.open(
        "https://www.linkedin.com/uas/js/userspace?v=0.0.2000-RC8.53856-1429&apiKey=4XZcfCb3djUl-DHJSFYd1l0ULtgSPl9sXXNGbTKT2e003WAeT6c2AqayNTIN5T1s&onLoad=linkedInAPILoaded612163388635963&authorize=true&credentialsCookie=true&secure=1&")

    for line in f.readlines():
        if "oauth_token" in line:
            return line.split('"')[1]


def checkEmailExistance(oauth_token, email_list, fn, ln):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie', ''))
    opener.addheaders.append(('oauth_token', oauth_token))
    opener.addheaders.append(('referer', 'https://api.linkedin.com/uas/js/xdrpc.html?v=0.0.2000-RC8.53856-1429'))

    checked = []

    for i in email_list:

        try:
            f = opener.open(
                "https://api.linkedin.com/v1/people/email=" + i + ":(first-name,last-name,public-profile-url)")
        except urllib2.HTTPError:
            checked.append([i, 0])
        else:
            xml_parsed = minidom.parseString(f.read())
            parsed_first_name = xml_parsed.getElementsByTagName('first-name')[0].childNodes[0].nodeValue
            parsed_last_name = xml_parsed.getElementsByTagName('first-name')[0].childNodes[0].nodeValue
            parsed_link = xml_parsed.getElementsByTagName('public-profile-url')[0].childNodes[0].nodeValue

            # False-Positive Check

            v = 2 if parsed_first_name.lower() != fn and parsed_last_name.lower() != ln else 1
            checked.append([i, v, parsed_link])

    return checked
