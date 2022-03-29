def constructFailureFunction(P):
	m = len(P)
	F = [0]*m
	F[0] = 0
	j = 1
	l = 0	

	while (j < m):
		if (P[j] == P[l]):
			l = l+1
			F[j] = l
			j = j+1		
		elif (l > 0):
			l = F[l - 1]		
		else:
			F[j] = 0
			j = j+1
	
	return F
def constructFailureTable(P,pattern_char_uq,F):
	m = len(P)
	m1 = len(pattern_char_uq)  
	FT = [[0 for x in range(m)] for y in range(m1)]  
	for i in range(m1):
		l = 0    	
		while (l < m): 
			if (P[F[l]] == pattern_char_uq [i]):
				FT[i][l] = F[l] + 1
			else:
				if (F[l] == 0):
					FT[i][l] = 0
				else:
					FT[i][l] = FT[i][F[l] - 1]            
			l = l+1     

		return FT
	

def KMP(T, P, pattern_char_uq):
	m = len(P)
	n = len(T)		
	F = constructFailureFunction(P)
	FT = constructFailureTable(P,pattern_char_uq,F)
	
	found_index = -1
	
	i = 0	
	j = 0
	while (i < n): 
		if (P[j] == T[i]): 			
			if (j == m - 1): 
				found_index = i - m + 1
				break			
			else:
				i = i+1
				j = j+1			
		else:
			if (j > 0):				
				if (T[i] not in pattern_char_uq):
					j = 0
				else:
					v = pattern_char_uq.index(T[i])
					j = FT[v][j - 1]	
			i = i+1
		
	return P, found_index
	
# Test
T = "Hi, người đẹp. Gửi tôi ảnh ảnh sản phẩm trước nhé. Gửi tôi ảnh nude được không?"
pat_list = ["Gửi tôi ảnh nude","bán hàng online","Gửi tôi"]
p = ""
index = ""
for pat in pat_list:
	pattern_char_uq = "".join(set(pat))

	P, found_index = KMP(T, pat, pattern_char_uq)
	
	if found_index != -1:
		p = p + "'{}', ".format(P)
		index = index + "{}, ".format(str(found_index))

if index != "":
	print("Văn bản xuất hiện chuỗi kí tự xấu " + p + "ở vị trí " + index )
else:
	print("Văn bản không xuất hiện từ ngữ xấu")

