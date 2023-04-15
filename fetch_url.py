import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import time

confluence_url=""
sso_login_url=""
# https://pfedprod.wal-mart.com/idp/pJIii/resumeSAML20/idp/SSO.ping
# https://pfedprod.wal-mart.com/idp/L4T19/resumeSAML20/idp/SSO.ping
#send a get request to confluence to get the SSO redirected URL
# auth=('p0k01v9@homeoffice.wal-mart.com','****')

session=requests.session()
response = session.get(confluence_url)


# <html><head><script>window.location.href="https://pfedprod.wal-mart.com/idp/SSO.saml2?SAMLRequest=jZLLbtswFER%2FheBeol51JcJy4MQIaiBNjEjJIpuApq4SAhSp8uGkf19aqgt3UaNbcu6ZuUMurz4HiQ5grNCqxmmcYASK606otxo%2FtbdRia9WS8sGOdK1d%2B%2FqEX54sA6FOWXpdFFjbxTVzApLFRvAUsdps%2F5%2BR7M4oaPRTnMtMVpbC8YFoxutrB%2FANGAOgsPT412N350bLSWEa9VLHzJA%2FMHkwIyLuR7IKP2bUJYEwkGCI0djwkIgjDYhjlDMTRucMGMPXXDujpDoD0V0I2mah%2Fg4nWG03dT4tUrKqsr3%2BzJf9EVeLKoiKZM0Z4uKf4UyLYLMWg9bZR1TrsZZkuVRUkRJ2aY5LSr6pYizsnzBaPd702uh5v4u1bKfRZZ%2Ba9tdtHtoWoyeT%2B8QBHhunU7m5qzuy1h26hivLje6JGf42Ssb6X0Abjc7LQX%2FeeaZ%2Ff8bS6k%2FbgwwBzV2xgNGt9oMzP0bkMbpdCK6qJ%2Bk1Cs7Ahe9gA6T1Zz07%2B%2B3%2BgU%3D&RelayState=%252Flogin.action%253Fos_destination%253D%25252Fpages%25252Fviewpage.action%25253FspaceKey%25253DASDAENG%252526title%25253DFY23%25252B-%25252BQuarterly%25252BPQA%25252BEnv%25252BIssues%2526permissionViolation%253Dtrue&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=tZZHyEMTVDngXD%2FN%2BLmD2EfdH1QE6Y6G0iwPdQPduubpkbAuZwQ6fMNwYNOQ2wSIxDb2Vv%2FQaC8D%0AWZXVU48qJSPfGIxCdRDPyOoxvZqvxMsjOw3aamyoY6%2FI%2B04X%2B%2BVbR%2BXUDTIbNP5Fa%2BegPwIuHyp0%0AtWddoW64WdJckVxyYq1EuPN4eiCfACx7%2B6kX%2BWXlcHN5xqciUjocghuSQObeZl0B9aj56x5Do%2Bzi%0AHUzqa66UYomfuRgKCb233bHnNHuCg2jvBzSVwZIIMz3FtWfhbnzTeKaioUV5OfqCW4rHxXwiBJvQ%0A6BuhYBHNy3Sw9liRFHpz4uUM7hFcF%2BRKUDIemOj3HaxzmedfPuum4uTjxaOUXEaMWrrdSjqWs%2B6t%0AiKcZUECkTc%2FI7I9%2FjuD9%2BF8sGj5DYo97BuQaZ16hpv%2B33C%2B0RHtefM8kR9US0MWgEtX%2B1eS0nIoE%0AFxWOFnVaeugzZPMVb5ndmXcW2RH6JTNP5YdL7QbRg0omvizkpk4iVMAA2%2Bb4ULbtuJvRmtzxAIr4%0AiMG1YAnkwn94%2BwIicbDZPbuunZqycACIMfnUjb8LF2QoCDsNEtRNVtjluTrC42%2Bj5XGq%2Fve2CXuX%0A%2FUOpGa3i%2FRMjZFpcfihK01VVUBKdabGhWv%2BA16rX5dvA%2ByZP7aKl88RYX3skDi%2BLTbh48UsLTa0%3D"
# </script></head><body>Please wait...</body></html>

print(response.url)
time.sleep(60)

response = session.get(response.url)

print(response.text)
# redirect_url=response.url
# redirect_url=auth=re.search(r"href=\"([^\">]+)\"", response.text)[1]
# print()
# print("the redirected url is ",redirect_url)
# # print(response.text)
#
# response = requests.get(redirect_url)
# print("the response from redirect url is ",response.text)
# print()
#
# #send a get request to SSO login page to get the SAML response form
# response=requests.get(sso_login_url)
# # print(response.text)
# soup=BeautifulSoup(response.text,"html.parser")
# # print(soup)
# saml_form=soup.find("form")
# # print(saml_form)
#
# #extract the SAML form fileds
# saml_request=saml_form.find("input",{"name":"SAMLRequest"})["value"]
# relay_state=saml_form.find("input",{"name":"RelayState"})["value"]
#
# #build the payload dictionary with the SAML form fields
# payload={
# "SAMLRequest":saml_request,
# "RelayState":relay_state,
#         }
#
# # send a POST request to SSO login page to authenticate
# response=requests.post(sso_login_url,data=payload)
# redirect_url=response.url
#
# # send a GET request to redirected url to get the confluence page
# response=requests.get(redirect_url)
# confluence_content=response.text

# print(f.text)
# parsed_html = BeautifulSoup(f.text)
# print(parsed_html)
# auth=re.search(r"href=\"([^\">]+)\"", f.text)[1]
# print(re.search(r"href=\"([^\">]+)\"", f.text)[1])
# f = requests.get(auth)
# print(f.text)
#
# link="https://confluence.walmart.com/pages/viewpage.action?spaceKey=ASDAENG&title=FY23+-+Quarterly+PQA+Env+Issues"
# f1= requests.get(link)
# print(f1.text)


# from urllib.request import urlopen
#
#
# f = urlopen(link)
# myfile = f.read()
# print(myfile)