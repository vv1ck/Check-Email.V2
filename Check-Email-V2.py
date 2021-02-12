import secrets, time,user_agent
import random , requests , uuid , sys
from time import sleep

uuid = uuid.uuid4() 
cokie  = secrets.token_hex(8)*2
r = requests.session()
def ketik(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(50. / 700)

print("""
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗    
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    
██║     ███████║█████╗  ██║ V2  █████╔╝     
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝""")
ketik("""
[1]> Check Insta    [2]> Check Twitter
        
       [3]> List list maker email
By JOKER / t.uo
""")


joker = input('Enter number : ')

if joker == '1':
	print('\n━━━━━━━━━━━━━━━ INSTA ━━━━━━━━━━━━━━━━')
	sl = int(input('[+] Enter sleep [ 3 / 7 ] : '))
	
	def yho():
		url = 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com'
	
		headers = {
			
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Connection': 'keep-alive',
			'Content-Length': '1415',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie': 'B=134vcn5g2bbpe&b=3&s=qj; GUC=AQEBAQFgJwBgL0IbewRH; A1=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A3=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A1S=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE&j=US; APID=UP41556690-6cb8-11eb-b3a4-0efff797295b; AS=v=1&s=6TWShzYC&d=A60274359|fsC2pD_.2SrPGM4_bsUz35krL9lhVhDkgjs9oXhsOxLn_6Pc8hBjqHW0tTZUOKxW1Y1zSIIqV8njXb.PBOrxDRrXfhwt_k3YX3tVb81JTLriH_Tszus2YORvYGHtNqXPE9F3yHfGj1tRrEMx3QS.xMnEUgRFk9i7ryR0Yf4bO6UwBY4r9bm8AQ.ASviERdysUeNgsFL6cnVVXVGvohfu9Bixh1Dhcc.hiQbM3oiuT6i1Guq0OA.B.gbjd5uXDRZWa0TyIcA8o9NWtu4Xwkod651B5mJVX7OKf8dgbZ.WuLfII7hGEuJIQumcrF0lYSa00bdoHOJITDfIdrZsEOMwapuC8PgyQ7TdTSE7Se2StSmyHt_OHimT4ok1EBYs7obzq9djkL8sdqhQN09zuM.P0vAZbVbbRKNm26l4_7tX8TvedU5dU.XVEOaEfsRKNGvwIhGRO2q7Moz548rof9QZ2j0UkWnjxx4gsEg_63pSZBdZdOiTfkYVYG.D0NO9AWtKGxpheNXOVt8Wxbx_140af0gQ5xSP1cnJU0SjUmj5Ru9doNFEZRGBniEM5cgPEB35OJH3.53XBu52SHyBa7AyJb7eedqqLgadHLn0SmgY8MX56DWB81WOIquyAgMknkBsf6MztjUZISotk83.TPxF93mIfVUWGQ2JsLKC1y_HFDE5JKNx0zoUs7X4MGDCZOQ6jHxB_Ay5TL_vBBZNiWTPzx1WZqow478Le27Q1YoypN5DY_eUfEtfvRJYPtgkHTyS3vABoI8FDC8sLMuuGhc_UjISybNAec2MNdBue96hR8Ni_B1GtP9Vcxfb18x4aZPan.j5.SP4jIYb_wIaIzxjVWYQ6sAJ5NKWWkzHpvxLEinGMde9mfqfBhcOk_rsAEf8XvNv3Ng-~A|C6027014a|FdYuFQD.2Ro5V4q.0EICg_TJUsTz2fCnS0hMzUGvjdLSyX_oe5h3q4pMKSj6upQIIsoS4ZGwTPbxmSx2tRJ7K0ASoA8nNws0p1Qhj7VLTdCTg0zvsfWcgRbzmA0TsCev.pDmairFLmKeHRGB5KsiPOQ1gp3gE_uYOCsMI_X.u.j0p70ia_YSl2jN04k3C50BMKFnfHloILTsDqu87JQF3xDv1LQS8fZICBqfQFEKsUHiRG6L.RCDLHle6V7Zfw170TuTyk5RojQHApkSAGNxyjuSyogaUBcO78_7DlZ3sH4jPeT5poE5M7vi1iyKDS0J0cLHV3kvaJJ_BwY.5pSMfl3XFl.tXlGZQ46RNXoffG7JkBPIQIqLtdiBRA5CU7oVKHFNVQzr24hOhTBx1H9nSeIbniTdnMA214dJ0yxQaxJ7m99RBq8O0vRzqSUmJ2rwSJZREkF3WIk7YAk4GB1BBDle91xLMqMqneJV3PmeTeRjIebH5fFQXjtek3lm1TkRJtt8XUU0U8Lpb5tjHE.LCN9rI_e..bLssuRUZXPZPMqE.8.abHk_VgDnsFf3hn81hopLbddNv11YkwAYO3m7bZQ8Ac5ko9eGUMQA5seI1nLX2ePDXp48qW__nG2e4r0BcevG68vtN4oezAS9W.k4prsy3fLEZiIeLgOcij_18OJAdEZsz.5keMZpxnlwmg5vZL.65dP5gFMfhd9WfgPSBLUM4DS7FiN.R9QgqfR.MD8MSI.yA27JorZqNyCZvBonkFkdv_SjVx67wmwsD0ExysXXz13W12.pAHKPD6HXWhvEw7VAJFPTV_vJm6p3Th8OPrgKgLhgqzwZgeM4ST0gOXwJfuIaspB2zJkjL7ZaZ_RMYsp7nuc29Qmx6k.y.lTVDwCCJzF70A5tQxKPRUMZPJCW8xRlpev2uzp3RbE_0qxPFogAdpqdxn.hZD10GT_fkZfQdNOwT99g87NCV1gQ79GDE_K41cynxh1acViZYWjJUOps8rIO2.MUgbMJiK5URAhdUKU9x7dYN9ozxrMJDDMLdx2iQGm1UJWfz7PBkEVZhJD1SDH2uvBhbn6tLhhU0tIylDoJkRXMPZgW3II-~A; APIDTS=1613099483',
			'Host': 'login.yahoo.com',
			'Origin': 'https://login.yahoo.com',
			'Referer': 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest'	
		}
		
	
		
		data = {
			'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":0,"timezone":"UTC","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":10,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1456","h":"818"},"availableResolution":{"w":"778","h":"1456"},"ts":{"serve":1613099481853,"render":1613099482712}}',
			'crumb': 'uQN26u0FMre',
			'acrumb': '6TWShzYC',
			'sessionIndex': 'QQ--',
			'displayName': '',
			'deviceCapability': '{"pa":{"status":false}}',
			'username': f'{eml}',
			'passwd': '',
			'signin': 'Berikutnya',
			'persistent': 'y'}
		
		
		req = r.post(url,headers=headers,data=data).text
		
		if '"error":"messages.INVALID_USERNAME"' in req:
			print(f'[Yho]> Available : \n{eml}')
			with open ('[$] Available.txt', 'a') as x:
				x.write ('[yahoo]> '+ eml + '\n')
		
		else:
			print(f'[Yho]> Not Available : \n{eml}')
		
		
	
	def html():
		url3 = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
		payload = ''
		headers3 = {
			"Accept": "*/*",
			"Content-Type": "application/x-www-form-urlencoded",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
			"Connection": "close",
			"Host": "odc.officeapps.live.com",
			"Accept-Encoding": "gzip, deflate",
			"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
			"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
			"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
			"uaid": "d06e1498e7ed4def9078bd46883f187b",
			"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
			
		req3 = r.get(url3, data=payload, headers=headers3)
		
		if "Neither" in req3.text:
			print(f'[Html]> Available >> \n{eml}\n')
			
			with open ('[$] Available.txt', 'a') as x:
				x.write ('[hotmail]> ' + eml + '\n')
		else:
			print(f'[Html] Not Available >> \n{eml}\n')
	
	def gml():
			
		url2 = "https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=404581&rt=j"
	
	
		headers2 = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '3893',
			'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
			'cookie': cokie,
			'google-accounts-xsrf': '1',
			'origin': 'https://accounts.google.com',
			'referer': 'https://accounts.google.com/AddSession/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
			'x-chrome-id-consistency-request': '',
			'x-client-data': 'CI22yQEIorbJAQjBtskBCKmdygEIlqzKAQj4x8oBCKTNygEI3NXKAQj69coBCKicywEI1ZzLAQjknMsBCKmdywEIj57LARj6uMoBGNrDygE=',
			'Decoded': 'message ClientVariations{//Active client experiment variation IDs.repeated int32 variation_id = [3300109, 3300130, 3300161, 3313321, 3315222, 3318776, 3319460, 3320540, 3324666, 3329576, 3329621, 3329636, 3329705, 3329807];// Active client experiment variation IDs that trigger server-side behavior.repeated int32 trigger_variation_id = [3316858, 3318234];',
			'x-same-domain': '1'}
		
		data2 = {
			'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue',
			'service': 'accountsettings',
			'f.req': f'["{eml}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{eml}",null,null,null,true,true,[]]',
			'bgRequest': '["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]',
			'at': 'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804',
			'azt': 'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]',
			'gmscoreversion': 'undefined',
			'checkConnection': 'youtube:353:0',
			'checkedDomains': 'youtube',
			'pstMsg': '1'}
		
		
		req2 = r.post(url2,data=data2,headers=headers2).text
		if ',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]' in req:
			print(f'[Gml]> Available >> \n{eml}\n')
			
			with open ('[$] Available.txt', 'a') as x:
				x.write ('[gmail]> '+ eml + '\n')
		else:
			print(f'[Gml] Not Available >> \n{eml}\n')
			
	
	
	ins = 'email.txt'
	
	file = open(ins, "r")
	
	while True:
		eml = file.readline().split('\n')[0]
		if eml == '':
			break
		url = 'https://i.instagram.com/accounts/account_recovery_send_ajax/'
		
		headers = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'en-US,en;q=0.9',
			'content-length': '88',
			'content-type': 'application/x-www-form-urlencoded',
			'cookie': cokie,
			'origin': 'https://i.instagram.com',
			'referer': 'https://i.instagram.com/accounts/password/reset/',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': '',
			'x-csrftoken': 'missing',
			'x-ig-app-id': '936619743392459',
			'x-ig-www-claim': '0',
			'x-instagram-ajax': '5282d9579ee4',
			'x-requested-with': 'XMLHttpRequest'}
		
		data = {
			'email_or_username': eml,
			'recaptcha_challenge_field': '', 
			'app_id': '',
			'flow': '',
			'source_account_id': ''}
		
		req = r.post(url, headers=headers, data=data)
		
		
		if '"can_recover_with_code":false' in req.text:
			print(f'Done insta>> {eml} ')
			
			if 'gmail' in eml:
				time.sleep(1)
				gml()
			
			elif 'hotmail' in eml:
				time.sleep(1)
				html()
			
			elif 'yahoo' in eml:
				time.sleep(1)
				yho()
			
			else:
				print('\n[-] Domain does not exist\n')
		
		
		else:
			print(f'Not linked to an account >> \n{eml}\n')
		time.sleep(sl)


elif joker == '2':
	print('\n━━━━━━━━━━━━━━━ TWITTER ━━━━━━━━━━━━━━━━')
	sl = int(input('[+] Enter sleep [ 3 / 7 ] : '))
	print(' ')
	def yho():
		url = 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com'
	
		headers = {
			
			'Accept': '*/*',
			'Accept-Encoding': 'gzip, deflate, br',
			'Accept-Language': 'en-US,en;q=0.9',
			'Connection': 'keep-alive',
			'Content-Length': '1415',
			'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'Cookie': 'B=134vcn5g2bbpe&b=3&s=qj; GUC=AQEBAQFgJwBgL0IbewRH; A1=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A3=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE; A1S=d=AQABBC6vJWACEP3J2yDNTyPDcwvbCLnskxEFEgEBAQEAJ2AvYAAAAAAA_SMAAAcILq8lYLnskxE&S=AQAAAqvidgG6yaSrmxk9va8BlxE&j=US; APID=UP41556690-6cb8-11eb-b3a4-0efff797295b; AS=v=1&s=6TWShzYC&d=A60274359|fsC2pD_.2SrPGM4_bsUz35krL9lhVhDkgjs9oXhsOxLn_6Pc8hBjqHW0tTZUOKxW1Y1zSIIqV8njXb.PBOrxDRrXfhwt_k3YX3tVb81JTLriH_Tszus2YORvYGHtNqXPE9F3yHfGj1tRrEMx3QS.xMnEUgRFk9i7ryR0Yf4bO6UwBY4r9bm8AQ.ASviERdysUeNgsFL6cnVVXVGvohfu9Bixh1Dhcc.hiQbM3oiuT6i1Guq0OA.B.gbjd5uXDRZWa0TyIcA8o9NWtu4Xwkod651B5mJVX7OKf8dgbZ.WuLfII7hGEuJIQumcrF0lYSa00bdoHOJITDfIdrZsEOMwapuC8PgyQ7TdTSE7Se2StSmyHt_OHimT4ok1EBYs7obzq9djkL8sdqhQN09zuM.P0vAZbVbbRKNm26l4_7tX8TvedU5dU.XVEOaEfsRKNGvwIhGRO2q7Moz548rof9QZ2j0UkWnjxx4gsEg_63pSZBdZdOiTfkYVYG.D0NO9AWtKGxpheNXOVt8Wxbx_140af0gQ5xSP1cnJU0SjUmj5Ru9doNFEZRGBniEM5cgPEB35OJH3.53XBu52SHyBa7AyJb7eedqqLgadHLn0SmgY8MX56DWB81WOIquyAgMknkBsf6MztjUZISotk83.TPxF93mIfVUWGQ2JsLKC1y_HFDE5JKNx0zoUs7X4MGDCZOQ6jHxB_Ay5TL_vBBZNiWTPzx1WZqow478Le27Q1YoypN5DY_eUfEtfvRJYPtgkHTyS3vABoI8FDC8sLMuuGhc_UjISybNAec2MNdBue96hR8Ni_B1GtP9Vcxfb18x4aZPan.j5.SP4jIYb_wIaIzxjVWYQ6sAJ5NKWWkzHpvxLEinGMde9mfqfBhcOk_rsAEf8XvNv3Ng-~A|C6027014a|FdYuFQD.2Ro5V4q.0EICg_TJUsTz2fCnS0hMzUGvjdLSyX_oe5h3q4pMKSj6upQIIsoS4ZGwTPbxmSx2tRJ7K0ASoA8nNws0p1Qhj7VLTdCTg0zvsfWcgRbzmA0TsCev.pDmairFLmKeHRGB5KsiPOQ1gp3gE_uYOCsMI_X.u.j0p70ia_YSl2jN04k3C50BMKFnfHloILTsDqu87JQF3xDv1LQS8fZICBqfQFEKsUHiRG6L.RCDLHle6V7Zfw170TuTyk5RojQHApkSAGNxyjuSyogaUBcO78_7DlZ3sH4jPeT5poE5M7vi1iyKDS0J0cLHV3kvaJJ_BwY.5pSMfl3XFl.tXlGZQ46RNXoffG7JkBPIQIqLtdiBRA5CU7oVKHFNVQzr24hOhTBx1H9nSeIbniTdnMA214dJ0yxQaxJ7m99RBq8O0vRzqSUmJ2rwSJZREkF3WIk7YAk4GB1BBDle91xLMqMqneJV3PmeTeRjIebH5fFQXjtek3lm1TkRJtt8XUU0U8Lpb5tjHE.LCN9rI_e..bLssuRUZXPZPMqE.8.abHk_VgDnsFf3hn81hopLbddNv11YkwAYO3m7bZQ8Ac5ko9eGUMQA5seI1nLX2ePDXp48qW__nG2e4r0BcevG68vtN4oezAS9W.k4prsy3fLEZiIeLgOcij_18OJAdEZsz.5keMZpxnlwmg5vZL.65dP5gFMfhd9WfgPSBLUM4DS7FiN.R9QgqfR.MD8MSI.yA27JorZqNyCZvBonkFkdv_SjVx67wmwsD0ExysXXz13W12.pAHKPD6HXWhvEw7VAJFPTV_vJm6p3Th8OPrgKgLhgqzwZgeM4ST0gOXwJfuIaspB2zJkjL7ZaZ_RMYsp7nuc29Qmx6k.y.lTVDwCCJzF70A5tQxKPRUMZPJCW8xRlpev2uzp3RbE_0qxPFogAdpqdxn.hZD10GT_fkZfQdNOwT99g87NCV1gQ79GDE_K41cynxh1acViZYWjJUOps8rIO2.MUgbMJiK5URAhdUKU9x7dYN9ozxrMJDDMLdx2iQGm1UJWfz7PBkEVZhJD1SDH2uvBhbn6tLhhU0tIylDoJkRXMPZgW3II-~A; APIDTS=1613099483',
			'Host': 'login.yahoo.com',
			'Origin': 'https://login.yahoo.com',
			'Referer': 'https://login.yahoo.com/?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com',
			'Sec-Fetch-Dest': 'empty',
			'Sec-Fetch-Mode': 'cors',
			'Sec-Fetch-Site': 'same-origin',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
			'X-Requested-With': 'XMLHttpRequest'	
		}
		
	
		
		data = {
			'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":0,"timezone":"UTC","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":10,"event":0,"start":0},"fonts":{"count":33,"hash":"edeefd360161b4bf944ac045e41d0b21"},"audio":"124.04347527516074","resolution":{"w":"1456","h":"818"},"availableResolution":{"w":"778","h":"1456"},"ts":{"serve":1613099481853,"render":1613099482712}}',
			'crumb': 'uQN26u0FMre',
			'acrumb': '6TWShzYC',
			'sessionIndex': 'QQ--',
			'displayName': '',
			'deviceCapability': '{"pa":{"status":false}}',
			'username': f'{eml}',
			'passwd': '',
			'signin': 'Berikutnya',
			'persistent': 'y'}
		
		
		req = r.post(url,headers=headers,data=data).text
		
		if '"error":"messages.INVALID_USERNAME"' in req:
			print(f'[Yho]> Available : \n{eml}')
			with open ('[$] Available.txt', 'a') as x:
				x.write ('[yahoo]> '+ eml + '\n')
		
		else:
			print(f'[Yho]> Not Available : \n{eml}')
		
		
	
	def html():
		url3 = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + eml + "&_=1604288577990"
		payload = ''
		headers3 = {
			"Accept": "*/*",
			"Content-Type": "application/x-www-form-urlencoded",
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
			"Connection": "close",
			"Host": "odc.officeapps.live.com",
			"Accept-Encoding": "gzip, deflate",
			"Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
			"Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
			"canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
			"uaid": "d06e1498e7ed4def9078bd46883f187b",
			"Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
			
		req3 = r.get(url3, data=payload, headers=headers3)
		
		if "Neither" in req3.text:
			print(f'[Html]> Available >> \n{eml}\n')
			
			with open ('[$] Available.txt', 'a') as x:
				x.write ('[hotmail]> ' + eml + '\n')
		else:
			print(f'[Html] Not Available >> \n{eml}\n')
	
	def gml():
			
		url2 = "https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=404581&rt=j"
	
	
		headers2 = {
			'accept': '*/*',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
			'content-length': '3893',
			'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
			'cookie': cokie,
			'google-accounts-xsrf': '1',
			'origin': 'https://accounts.google.com',
			'referer': 'https://accounts.google.com/AddSession/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
			'x-chrome-id-consistency-request': '',
			'x-client-data': 'CI22yQEIorbJAQjBtskBCKmdygEIlqzKAQj4x8oBCKTNygEI3NXKAQj69coBCKicywEI1ZzLAQjknMsBCKmdywEIj57LARj6uMoBGNrDygE=',
			'Decoded': 'message ClientVariations{//Active client experiment variation IDs.repeated int32 variation_id = [3300109, 3300130, 3300161, 3313321, 3315222, 3318776, 3319460, 3320540, 3324666, 3329576, 3329621, 3329636, 3329705, 3329807];// Active client experiment variation IDs that trigger server-side behavior.repeated int32 trigger_variation_id = [3316858, 3318234];',
			'x-same-domain': '1'}
		
		data2 = {
			'continue': 'https://myaccount.google.com/?utm_source=sign_in_no_continue',
			'service': 'accountsettings',
			'f.req': f'["{eml}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{eml}",null,null,null,true,true,[]]',
			'bgRequest': '["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]',
			'at': 'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804',
			'azt': 'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805',
			'cookiesDisabled': 'false',
			'deviceinfo': '[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]',
			'gmscoreversion': 'undefined',
			'checkConnection': 'youtube:353:0',
			'checkedDomains': 'youtube',
			'pstMsg': '1'}
		
		
		req2 = r.post(url2,data=data2,headers=headers2).text
		if ',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]' in req:
			print(f'[Gml]> Available >> \n{eml}\n')
			
			with open ('[$] Available.txt', 'a') as x:
				x.write ('[gmail]> '+ eml + '\n')
		else:
			print(f'[Gml] Not Available >> \n{eml}\n')
	
	ins = 'email.txt'
	file = open(ins, "r")
		
	
	while True:
		eml = file.readline().split('\n')[0]
		if eml == '':
			break
		url = "https://twitter.com/users/email_available?email="
		
		headers = {
			'Host': 'twitter.com',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
			'Cookie': 'personalization_id="v1_6TNKT0FSMkPP7CfzL5Rkfg=="; guest_id=v1%3A159789135703778252; _ga=GA1.2.490437195.1597891367'}
		
		
		req = r.get(f'{url}{eml}',headers=headers).text
		
		if '"taken":false' in req:
			print(f'Not linked to an account >> \n{eml}\n')
			
		else:
			print(f'Done twiterr > {eml}')
			if 'gmail' in eml:
				time.sleep(1)
				gml()
			
			elif 'hotmail' in eml:
				time.sleep(1)
				html()
			
			elif 'yahoo' in eml:
				time.sleep(1)
				yho()
			
			else:
				print('\n[-] Domain does not exist\n')
		time.sleep(sl)

elif joker == '3':
	print("""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Type in the domain you want :""")
	ketik(' 	[ gmail / yahoo / hotmail ]')

	domen = input('Enter domen : @')
	usr = 'zaqxswcdevfrbgtnhymjukilop'
	how = input('\nHow many email do you want? : ')
	how = int(how)
	
	hrf = input('\nHow many letters? : ')
	hrf = int(hrf)
	
	for email in range(how):
		email = ''
		for item in range(hrf):
			email = ''
		for item in range(hrf):
			email += random.choice(usr)
		print (email+'@'+domen+'.com')
		with open('email.txt', 'a') as x:
			x.write(email+'@'+domen+'.com\n')
