password = 'a123456'
try_time = 3
while try_time > 0:
	ans = input('請輸入密碼:')
	if ans == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!還有',try_time-1,'次機會')
	try_time = try_time-1
	if try_time == 0:
		print('您已達到本日錯誤上限，請明天再嘗試')
