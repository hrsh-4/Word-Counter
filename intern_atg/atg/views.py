from django.shortcuts import render
from .forms import URLForm
from .models import URLInformation
import requests
from collections import defaultdict
import string
from bs4 import BeautifulSoup as bs
from django.shortcuts import redirect
# Create your views here.
def frequency(request):
	if request.method == 'POST':
		form = URLForm(request.POST)
		if form.is_valid():
			url = form.cleaned_data.get('url')
			# data = requests.get(data).text
			post = form.save(commit=False)
			post.save()
			print(data)
			return redirect('result')
	else:
		form = URLForm()
	context = {'form':form}
	return render(request,'request.html',context)

def result(request):
	url = request.POST['url']
	common_words = ['the','to','of','and','a',
'in',
'that',
'have',
'I',
'it',
'for',
'not',
'on',
'with',
'he',
'as',
'you',
'do',
'at',
'this',
'but',
'his',
'by',
'from',
'they',
'we',
'say',
'her',
'she',
'or',
'an',
'will',
'my',
'one',
'all',
'would',
'there',
'their',
'what',
'so',
'up',
'out',
'if',
'about',
'who',
'get',
'which'
'go',
'me',
'when',
'make',
'can',
'like',
'time',
'no',
'just',
'him','know',
'take',
'people',
'into',
'year',
'your',
'good','some',
'could','them',
'see',
'other',
'than',
'then',
'now',
'look',
'only',
'come',
'its',
'over',
'think','also','back',
'after',
'use',
'two',
'how',
'our',
'work',
'first',
'well',
'way',
'even',
'new',
'want',
'because',
'any',
'these',
'give',
'day',
'most',
'us',
'is',
'are'
]
	# if (URLInformation.objects.get(url!=url)):
	# 	new_url = URLInformation(
	#         url=url,
	# 		is_saved = True
	#         )
	# 	new_url.save()
	url_qs = URLInformation.objects.filter(url=url, is_saved=True)

	d = defaultdict(int)
	if url_qs.exists():
		# if url_qs.result:
		# x = ""
		# data = requests.get(url)
		# soup = bs(data.text,"lxml")
		# allLines = soup.text.split('\n')
		# for line in allLines:
		# 	x += line
		# for i in x.split():
		# 	if i not in common_words:
		# 		d[i] += 1
		# y = sorted(d.items(), key =
        #      lambda kv:(kv[1], kv[0]),reverse=True)[:10]
		# r = ""
		# for j in y:
		# 	r += j
		# s = URLInformation.objects.filter(url=url,is_saved=True)
		# s.result = r
		# s.save()
		#
		print(url_qs)
		print(url_qs[0])
		# print(url_qs.url)
		# print(url_qs.values('result'))
		r = url_qs.values('result')
		print(r)
		print(type(r))
		z = [j for j in r]
		# print(url_qs[1])
		# print(url_qs[2])
		return render(request,'stored_result.html',{'data':z})
	else:

		x = ""

		data = requests.get(url)
		soup = bs(data.text,"lxml")
		for tag in soup.find_all('script'):
			tag.clear()

# Clear every style tag
		for tag in soup.find_all('style'):
			tag.clear()

		allLines = soup.text.split('\n')
		for line in allLines:
			x += line
		for i in x.split():
			if i not in common_words:
				d[i] += 1
		y = sorted(d.items(), key =
             lambda kv:(kv[1], kv[0]),reverse=True)[:10]
		# r = ""
		# for j in y:
		# 	r += j
		new_url = URLInformation(
		        url=url,
				is_saved = True,
				result = y
		        )
		new_url.save()

		return render(request,'new_result.html',{'data':y})
