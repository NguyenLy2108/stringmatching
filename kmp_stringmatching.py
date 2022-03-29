def KMPSearch(pat, txt):
	M = len(pat)
	N = len(txt)
	lps = [0]*M
	j = 0 

	computeLPSArray(pat, M, lps)
	i = 0 
	while i < N:
		if pat[j] == txt[i]:
			i += 1
			j += 1
		if j == M:
			print ("Found ” + pat + “ at index " + str(i-j))
			j = lps[j-1]	
		elif i < N and pat[j] != txt[i]:		
			if j != 0:
				j = lps[j-1]
			else:
				i += 1

def computeLPSArray(pat, M, lps):
	j = 0 
	lps[0] 
	i = 1
	while i < M:
		if pat[i]== pat[j]:
			j += 1
			lps[i] = j
			i += 1
		else:			
			if j != 0:
				j = lps[j-1]
			else:
				lps[i] = 0
				i += 1
#Test	
txt = "Hi, người đẹp. Gửi tôi ảnh ảnh sản phẩm trước nhé. Gửi tôi ảnh nude được không?"
pat_list= ["Gửi tôi ảnh nude","bán hàng online"]

for pat in pat_list:
	KMPSearch(r.lower(), txt.lower())
